import numpy as np

def readData(fname):
	a=[]
	with open(fname) as f:
		for l in f.readlines():
			command, depth = l.split(' ')
			a.append((command,int(depth)))
	return a

def steerTheBoat(cmds):
	depth=0
	x=0;
	for cmd, adv in cmds:
		if cmd=='up':
			depth-=adv
		elif cmd=='down':
			depth+=adv
		elif cmd=='forward':
			x+=adv
	return depth,x

def steerTheBoat2(cmds):
	depth=0
	x=0
	aim=0
	for cmd, adv in cmds:
		if cmd=='up':
			aim-=adv
		elif cmd=='down':
			aim+=adv
		elif cmd=='forward':
			x+=adv
			depth+=aim*adv
	return depth,x


data=readData('in.txt')
depth,x=steerTheBoat(data)
print(depth*x)
depth,x=steerTheBoat2(data)
print(depth*x)