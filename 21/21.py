import numpy as np
import math
import itertools

def readData(fname):
	key=""
	image={}
	with open(fname) as f:
		lines=f.readlines()
		x=int(lines[0].split(':')[1])
		y=int(lines[1].split(':')[1])
		return x,y

def playTheGame1(x,y):
	i=0
	n=0
	xScore=0
	yScore=0
	while True:
		dieSum=0
		for j in range(3):
			dieSum+=i%100+1
			i+=1
			n+=1
		x+=dieSum
		x=(x-1)%10+1
		xScore+=x
		if xScore>=1000:
			print(yScore*n)
			break
		dieSum=0
		for j in range(3):
			dieSum+=i%100+1
			i+=1
			n+=1
		y+=dieSum
		y=(y-1)%10+1
		yScore+=y
		if yScore>=1000:
			print(xScore*n)
			break
		#break
global nums
nums={}
for x in list(itertools.product(range(1,4),repeat=3)):
	x=sum(x)
	nums[x]=nums.get(x,0)+1


def countWinningSchemes(x,winScheme,loseScheme,xScore=0,n=1,d=0):
	for i in range(3,10):
		xNew=(x+i-1)%10+1
		xScoreNew=xScore+xNew
		if xScoreNew>=21:
			winScheme[d]=winScheme.get(d,0)+n*nums[i]
		else:
			loseScheme[d]=loseScheme.get(d,0)+n*nums[i]
			countWinningSchemes(xNew,winScheme,loseScheme,xScoreNew,n*nums[i],d+1)



x,y=readData('in.txt')
playTheGame1(x, y)
winSch1={}
winSch2={}

loseSch1={}
loseSch2={}

countWinningSchemes(x,winSch1,loseSch1)
countWinningSchemes(y,winSch2,loseSch2)
xWin=0
yWin=0
for d in set(winSch1.keys()).union(set(winSch2.keys())).union(set(loseSch1.keys())).union(set(loseSch2.keys())):
	x=winSch1.get(d,0)
	y=winSch2.get(d,0)
	xWin+=x*loseSch2.get(d-1,0)
	yWin+=y*loseSch1.get(d,0)

print(max(xWin,yWin))