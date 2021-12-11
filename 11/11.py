import itertools
import operator

def readData(fname):
	data={}
	with open(fname) as f:
		y=0
		for l in f.readlines():
			x=0
			if l[-1]=='\n':
				l=l[:-1]
			for h in list(l):
				data[(x,y)]=int(h)
				x+=1
			y+=1
	return data


def printNice(data):
	for y in range(10):
		l=""
		for x in range(10):
			l+=str(data[x,y])
		print(l)

def flash(data,flashedPos=set()):
	flashed=False
	for o in data:
		if data[o]>9 and o not in flashedPos:
			data[o]=0
			flashedPos.add(o)
			for adj in list(itertools.product([-1, 0, 1], [-1, 0, 1])):
				if adj==(0,0):
					continue
				adjPos=tuple(map(operator.add, o, adj))
				if adjPos not in data:
					continue
				data[adjPos]+=1
			flashed=True
	for o in flashedPos:
		data[o]=0
	return data,flashed,flashedPos

def doOneStep(data):
	for o in data:
		data[o]+=1
	flashed=True
	flashedPos=set()
	while flashed:
		data,flashed,flashedPos=flash(data,flashedPos)
	return data,len(flashedPos)

data=readData('in.txt')
print()
n=0
for i in range(100):
	data,nFlash=doOneStep(data)
	n+=nFlash
print(n)
n=0
data=readData('in.txt')
while True:
	n+=1
	data,nFlash=doOneStep(data)
	if nFlash==100:
		break
print(n)