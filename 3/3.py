import numpy as np


def bin2dec(num):
	l=len(num)
	n=0
	for i in range(l):
		n+=(num[l-i-1]<<i)
	return n,(~n)& ((1<<l)-1)




def readData(fname):
	a=[]
	with open(fname) as f:
		for l in f.readlines():
			b=[]
			for ch in l:
				if ch!='\n':
					b.append(int(ch))
			a.append(b)
	return a

def transpose(arr):
	a=[]
	rows=len(arr)
	cols=len(arr[0])
	for c in range(cols):
		b=[]
		for r in range(rows):
			b.append(arr[r][c])
		a.append(b)
	return a

def calculate(arr):
	l=len(arr[0])
	a=[int(sum(col)>=l/2.) for col in arr]
	n, xn=bin2dec(a)
	return a,n,xn

def filter(data, cmp=True):
	nums=data
	it=0
	while len(nums)>1:
		comm,_,_=calculate(transpose(nums))
		nums_mod=[n for n in nums if (n[it]==comm[it])==cmp]
		nums=nums_mod
		it+=1

	n,xn=bin2dec(nums[0])
	return n


data=readData('in.txt')
_,e,g=calculate(transpose(data))
print(e*g)
print(filter(data)*filter(data,False))
