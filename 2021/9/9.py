
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

def findLowSpots(data):
	lowSpots={}
	for loc in data:
		val=data[loc]
		isLow=True
		for adj in (-1,0),(1,0),(0,-1),(0,1):
			adjVal=data.get(tuple(map(operator.add, loc, adj)),9)
			if val>=adjVal:
				isLow=False
		if isLow:
			lowSpots[loc]=val
	return lowSpots

def checkAdjacent(loc,checked=set()):
	goodPoints=set()
	for adj in (0,0),(-1,0),(1,0),(0,-1),(0,1):
		pos=tuple(map(operator.add, loc, adj))
		if pos in checked:
			continue
		adjVal=data.get(pos,9)
		checked.add(pos)
		if adjVal!=9:
			goodPoints.add(pos)
			good, checked = checkAdjacent(pos, checked)
			goodPoints=set.union(good,goodPoints)
	return goodPoints,checked


def findBasins(data,lowSpots):
	b=[]
	for pos in lowSpots:
		good,_=checkAdjacent(pos)
		b.append(len(good))
	return b


data=readData('in.txt')
lowSpots=findLowSpots(data)
print(sum(lowSpots.values())+len(lowSpots))
b=findBasins(data, lowSpots)
b.sort()
print(b[-1]*b[-2]*b[-3])