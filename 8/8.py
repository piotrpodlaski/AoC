from itertools import permutations

def decodeDigit(segments):
	s=set(segments)
	if s == set({'a','b','c','e','f','g'}):
		return 0
	elif s == set({'c','f'}):
		return 1
	elif s== set({'a','c','d','e','g'}):
		return 2
	elif s == set({'a','c','d','f','g'}):
		return 3
	elif s == set({'b','c','d','f'}):
		return 4
	elif s == set({'a','b','d','f','g'}):
		return 5
	elif s == set({'a','b','d','e','f','g'}):
		return 6
	elif s == set({'a','c','f'}):
		return 7
	elif s == set({'a','b','c','d','e','f','g'}):
		return 8
	elif s == set({'a','b','c','d','f','g'}):
		return 9
	else:
		return -1
	return m

def applyWireMapping(signals,mapping):
		a=['a','b','c','d','e','f','g']
		m={}
		for i in range(len(a)):
			m[a[i]]=mapping[i]
		return ''.join([m[x] for x in signals])

def readData(fname):
	data=[]
	with open(fname) as f:
		for l in f.readlines():
			if l[-1]=='\n':
				l=l[:-1]
			l=l.split('|')
			signals=l[0][:-1].split(" ") #remove spaces
			digits=l[1][1:].split(" ") #remove spaces
			data.append((signals,digits))
	return data

def calculateLen(data):
	lens={}
	for _,a in data:
		for d in a:
			l=len(d)
			lens[l]=lens.get(l,0)+1

	return lens

def checkPerm(digits, perm):
	for d in digits:
		dig=applyWireMapping(d,perm)
		l=len(d)
		if decodeDigit(dig)==-1:
			return False
		if l ==2 and decodeDigit(dig) != 1:
			return False
		if l ==3 and decodeDigit(dig) != 7:
			return False
		if l ==4 and decodeDigit(dig) != 4:
			return False
	return True


def bruteForcePermutation(display):
	perms=[''.join(p) for p in permutations('abcdefg')]
	results=[]
	for p in perms:
		r=checkPerm(display,p)
		if r:
			return p
		
def solveProblem2(data):
	s=0
	for digits,display in data:
		p=bruteForcePermutation(digits)
		nums=[decodeDigit(applyWireMapping(d,p)) for d in display]
		for i in range(4):
			s+=nums[i]*(10**(3-i))
	return s




data=readData('in.txt')
lens=calculateLen(data)
print(lens[2]+lens[3]+lens[4]+lens[7])
print(solveProblem2(data))
