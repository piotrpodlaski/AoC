import numpy as np
import math
import itertools

def findMatchingPar(s,pos):
	d=0
	dAtPos=0
	if s[pos]=='[':
		for i in range(len(s)):
			c=s[i]
			if i==pos:
				dAtPos=d
			if c=='[':
				d+=1
			if c==']':
				d-=1
			if dAtPos==d:
				return i
	else:
		for i in reversed(range(len(s))):
			c=s[i]
			if i==pos:
				dAtPos=d
			if c==']':
				d+=1
			if c=='[':
				d-=1
			if dAtPos==d:
				return i

def readData(fname):
	numbers=[]
	with open(fname) as f:
		for l in f.readlines():
			if l[-1]=='\n':
				l=l[:-1]
			numbers.append(l)
	return numbers

def explode(s):
	d=0
	for i in range(len(s)):
		c=s[i]
		if c=='[':
			d+=1
		elif c==']':
			d-=1
		if d==5:
			start=i
			stop=findMatchingPar(s,i)+1
			
			x=s[start+1:stop-1].split(',')
			left = int(x[0])
			right= int(x[1])
			leftString=s[:start]
			rightString=s[stop:]
			for j in range(len(rightString)):
				if rightString[j] not in ['[',']',',']:
					ss=""
					k=0
					while rightString[j+k] not in ['[',']',',']:
						ss=ss+rightString[j+k]
						k+=1
					val=int(ss)
					rightString=rightString[:j]+str(val+right)+rightString[j+k:]
					break
			for j in reversed(range(len(leftString))):
				if leftString[j] not in ['[',']',',']:
					ss=""
					k=0
					while leftString[j-k] not in ['[',']',',']:
						ss=leftString[j-k]+ss
						k+=1
					val=int(ss)
					leftString=leftString[:j-k+1]+str(val+left)+leftString[j+1:]
					break
			return leftString+"0"+rightString, True
	return s, False

def split(s):
	for i in range(len(s)):
		pars=['[',']',',']
		if s[i] not in pars and s[i+1] not in pars:
			adv=0
			for c in s[i:]:
				adv+=1
				if c in pars:
					break
			leftString=s[:i]
			rightString=s[i+adv-1:]
			val=int(s[i:i+2])
			newPair="["+str(val//2)+","+str(int(math.ceil(val/2)))+"]"
			s=leftString+newPair+rightString
			return s,True
	return s, False

def reduce(s):
	somethingWasDone=True
	while somethingWasDone:
		somethingWasDone=False
		wasExploded=True
		while wasExploded:
			s,wasExploded=explode(s)
			if wasExploded:
				somethingWasDone=True
		
		wasSplit=True
		s,wasSplit=split(s)
		if wasSplit:
			somethingWasDone=True
	return s

def add(a,b):
	s="["+a+","+b+"]"
	return(reduce(s))

def calculateMagnitude(number):
	left=0
	right=0
	if isinstance(number[0], list):
		left=calculateMagnitude(number[0])
	else:
		left=number[0]

	if isinstance(number[1], list):
		right=calculateMagnitude(number[1])
	else:
		right=number[1]
	return 3*left+2*right


numbers=readData('in.txt')
s=numbers[0]
for n in numbers[1:]:
	s=add(s, n)
print(calculateMagnitude(eval(s)))

pairs=list(itertools.combinations(numbers, 2))
nums=[]
for p in pairs:
	n1=calculateMagnitude(eval(add(p[0],p[1])))
	n2=calculateMagnitude(eval(add(p[1],p[0])))
	nums.append(n1)
	nums.append(n2)

print(max(nums))