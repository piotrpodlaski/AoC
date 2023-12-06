import numpy as np
import math

def readData(fname):
	xRange=[]
	yRange=[]
	with open(fname) as f:
		y=0
		l =f.readlines()[0]
		l=l.split(': ')[1].split(', ')
		[xRange,yRange]=[x[2:].split('..') for x in l]
		xRange=[int(x) for x in xRange]
		yRange=[int(x) for x in yRange]
	return xRange,yRange

def checkInTarget(x,y,xRange,yRange):
	if x>=xRange[0] and x<=xRange[1] and y>=yRange[0] and y<=yRange[1]:
		return True
	else:
		return False

def simulateProbe(xRange,yRange,vx,vy):
	x=0
	y=0
	xx=[]
	t=0
	while x<xRange[1] and y>yRange[0]:
		x+=vx
		if vx!=0:
			vx-=vx/abs(vx)
		y+=vy
		vy-=1
		xx.append(x)
		if checkInTarget(x,y,xRange,yRange):
			return True
	return False

def checkVelocities(xRange,yRange):
	vyVec=[]
	vxVec=[]
	n=0
	for vx in range(0,xRange[1]+1):
		for vy in range(-abs(yRange[0]),abs(yRange[0])):
			if(simulateProbe(xRange,yRange,vx,vy)):
				n+=1
	print(n)



ranges=readData('in.txt')

yy=[]
y=0
vy=abs(ranges[1][0])-1
while y>=0:
	y+=vy
	vy-=1
	yy.append(y)
print(max(yy))


checkVelocities(ranges[0],ranges[1])