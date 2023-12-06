import numpy as np
import math
import itertools

def readData(fname):
	scanners=[]
	becs=[]
	with open(fname) as f:
		for l in f.readlines():
			if l[-1]=='\n':
				l=l[:-1]
			if len(l)==0:
				continue
			if l[0:3]=='---':
				if len(becs)>0:
					scanners.append(becs)
				becs=[]
				continue
			becs.append(np.array([int(x) for x in l.split(',')]))
		scanners.append(becs)
	return scanners

def findAllRotations():
	r=[]
	xRot=np.array([[1,0,0],[0,0,-1],[0,1,0]])
	yRot=np.array([[0,0,1],[0,1,0],[-1,0,0]])
	for p in list(itertools.product(range(4),repeat=4)):
		m=np.linalg.matrix_power(xRot, p[0])
		m=m@np.linalg.matrix_power(yRot, p[1])
		m=m@np.linalg.matrix_power(xRot, p[2])
		m=m@np.linalg.matrix_power(yRot, p[3])
		
		if len(list(filter (lambda x : (x == m).all(), r)))==0:
			r.append(m)
	return r

def findCommon(s1,s2):
	c=[]
	s1Set=set(map(tuple, s1))
	for b1 in s1:
		for b2 in s2:
			delta=b1-b2
			newS2=[x+delta for x in s2]
			newS2=set(map(tuple,newS2))
			if len(s1Set.intersection(newS2))>=12:
				return True, delta
	return False, np.array([0,0,0])


def rotateBeacons(becs,r,offset=0):
	res=[]
	for b in becs:
		res.append(r@b+offset)
	return res

def compareTwoScanners(s1,s2,rots):
	for r in rots:
		found,delta=findCommon(s1, rotateBeacons(s2, r))
		if found:
			return r,delta,True
	return 0,0,False

def buildFullMap(scanners):
	m=scanners[0]
	used=[0]
	rots=findAllRotations()
	mSet=set(map(tuple,scanners[0]))
	positions=[]
	
	while len(used)<len(scanners):
		for i in range(len(scanners)):
			if i in used:
				continue
			r,d,f=compareTwoScanners(m, scanners[i], rots)
			if f:
				used.append(i)
				mSet=mSet.union(set(map(tuple,rotateBeacons(scanners[i], r, d))))
				m=[np.array(x) for x in mSet]
				positions.append(d)
				break
	return m,positions

scanners=readData('in.txt')
fullMap,positions=buildFullMap(scanners)

m=0
for b1,b2 in itertools.combinations(positions, 2):
	dst=sum(abs(b1-b2))
	if dst>m:
		m=dst
print(len(fullMap))
print(m)