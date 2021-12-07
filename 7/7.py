import time
import matplotlib.pyplot as plt
import math

def readData(fname):
	with open(fname) as f:
		return [int(x) for x in f.readlines()[0].split(',')]
		
def calculateFuel(poss,partTwo=False):
	fuel=[]
	xmin=min(poss)
	xmax=max(poss)
	for p in range(xmin,xmax):
		f=0
		for r in poss:
			x=abs(p-r)
			if partTwo:
				x=int(x*(x+1)/2)
			f+=x
		fuel.append(f)
	return min(fuel),fuel

positions=readData('in.txt')
minFuel1,fuel1=calculateFuel(positions)
minFuel2,fuel2=calculateFuel(positions,True)
print(minFuel1)
print(minFuel2)
plt.plot(fuel1,label="part 1")
plt.plot(fuel2,label="part 2")
plt.yscale('log')
plt.legend()
plt.show()

