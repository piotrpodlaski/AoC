def readData(fname):
	data=[]
	insertions={}
	template=[]
	with open(fname) as f:
		lines = f.readlines()
		template=list(lines[0][:-1])
		for l in lines[1:]:
			if l[-1]=='\n':
				l=l[:-1]
			if len(l)==0:
				continue
			l=l.split(' -> ')
			insertions[l[0]]=l[1]

	return template, insertions

def countElements(pairs, polymer):
	numElements={}
	for p in pairs:
		[a,b]=p
		numElements[a]=numElements.get(a,0)+pairs[p]
		numElements[b]=numElements.get(b,0)+pairs[p]
	for n in numElements:
		if n == polymer[0] or n==polymer[-1]:
			numElements[n]+=1
		numElements[n]//=2
	return numElements

def run(nIters, polymer, pattern):
	pairs={}
	for i in range(len(polymer)-1):
		a=''.join(polymer[i:i+2])
		pairs[a]=pairs.get(a,0)+1
	for i in range(nIters):
		pairs2={}
		for p in pairs:
			if p in pattern:
				a=p[0]+pattern[p]
				pairs2[a]=pairs2.get(a,0)+pairs[p]
				a=pattern[p]+p[1]
				pairs2[a]=pairs2.get(a,0)+pairs[p]
			else:
				pairs2[p]=pairs2.get(p,0)+pairs[p]
		pairs=pairs2
	n=countElements(pairs,polymer).values()
	return max(n)-min(n)

polymer,pattern=readData('in.txt')
print(run(10, polymer, pattern))
print(run(40, polymer, pattern))