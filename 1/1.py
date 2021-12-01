import numpy as np

def readData(fname):
	a=[]
	with open(fname) as f:
		for l in f.readlines():
			a.append(int(l))
	return a

def filter(data):
	return np.convolve(data,np.ones(3), mode='valid')

def countInc(data):
	n=0
	prev=data[0];
	for i in data[1:]:
		if(i-prev>0):
			n+=1
		prev=i
	return n


data=readData('in.txt')
print(countInc(data))
print(countInc(filter(data)))
