import math
import itertools
import operator
import matplotlib.pyplot as plt

def readData(fname):
	risk={}
	with open(fname) as f:
		y=0
		for l in f.readlines():
			if l[-1]=='\n':
				l=l[:-1]
			x=0
			for r in l:
				risk[x,y]=int(r)
				x+=1
			y+=1

	return risk,y

def checkAdj(pos, risk, dst,update=False):
	dst0=dst[pos]
	better=[]
	for adj in (-1,0),(1,0),(0,-1),(0,1):
		adjPos=tuple(map(operator.add, pos, adj))
		if adjPos not in risk:
			continue
		if update and adjPos not in dst:
			continue
		dstAdjOld=dst.get(adjPos,math.inf)
		dstAdj=dst0+risk[adjPos]
		#print(adjPos, dstAdj,dstAdjOld)
		if(dstAdj<dstAdjOld):
			dst[adjPos]=dstAdj
			if dstAdjOld!=math.inf:
				better.append(adjPos)
		#print(better)
	for p in better:
		checkAdj(p,risk,dst,True)
	

def pathFinder(risk,size):
	dst={(0,0):0}
	for x in range(size):
		for y in range(size):
			checkAdj((x,y),risk,dst)
	return dst

def enlargeCave(risk,size,n=5):
	for x in range(size):
		for y in range(size):
			for i in range(n):
				old=risk[x,y]
				new=old+i
				if new>9:
					new=new-9
				risk[x+i*size,y]=new
	for x in range(n*size):
		for y in range(size):
			for i in range(n):
				old=risk[x,y]
				new=old+i
				if new>9:
					new=new-9
				risk[x,y+i*size]=new

def findPathPoints(dst, size):
	path=[]
	d=dst[size-1,size-1]
	p=(size-1,size-1)
	while d!=0:
		path.append(p)
		p1=p
		for adj in (-1,0),(1,0),(0,-1),(0,1):
			adjPos=tuple(map(operator.add, p, adj))
			if adjPos in dst:
				dstAdj=dst[adjPos]
				if dstAdj<d:
					d=dstAdj
					p1=adjPos
		p=p1
	path.append((0,0))
	xPath=[x[0] for x in path]
	yPath=[size-x[1] for x in path]
	return xPath, yPath


risk, size=readData('in.txt')


dst=pathFinder(risk,size)
print(dst[size-1,size-1])

enlargeCave(risk,size)
dst=pathFinder(risk,5*size)
print(dst[5*size-1,5*size-1])

xPath,yPath=findPathPoints(dst,5*size)
plt.plot(xPath,yPath)
plt.show()