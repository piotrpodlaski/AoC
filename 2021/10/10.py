
op={'(':')','[':']','{':'}','<':'>'}
scores={')':3,']':57,'}':1197,'>':25137}
scores2={')':1,']':2,'}':3,'>':4}


import operator
def readData(fname):
	data=[]
	with open(fname) as f:
		for l in f.readlines():
			if l[-1]=='\n':
				l=l[:-1]
			data.append(list(l))
	return data

def checkLineCorrupted(line):
	parenth=[line[0]]
	for c in line[1:]:
		if c in op:
			parenth.append(c)
		else:
			last=parenth[-1]
			if c != op[last]:
				return scores[c],[]
			parenth.pop()
	return 0,parenth

def calculateScore2(delims):
	sc=[]
	for d in delims:
		d.reverse()
		d=[op[x] for x in d]
		partScore=0
		for x in d:
			partScore*=5
			partScore+=scores2[x]
		sc.append(partScore)
	sc.sort()
	return(sc[len(sc)//2])

data=readData('in.txt')
n=0
incomplete=[]
for d in data:
	sc,par=checkLineCorrupted(d)
	if sc==0:
		incomplete.append(par)
	n+=sc
print(n)
print(calculateScore2(incomplete))