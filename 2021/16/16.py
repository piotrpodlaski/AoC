import numpy as np
import math

def readData(fname):
	risk={}
	with open(fname) as f:
		y=0
		l =f.readlines()[0]
		result=""
		for x in l:
			i=int(x,16)
			result+="{0:04b}".format(i)
	return result

global a
a=0

def parsePacket(packet,res=[],decodeMax=math.inf):
	version=int(packet[0:3],2)
	global a
	a+=version
	typeID=int(packet[3:6],2)
	cursor=0
	if typeID==4:
		#print("LITERAL")
		i=6
		result=""
		while True:
			prefix=packet[i]
			result+=packet[i+1:i+5]
			cursor=i+5
			if prefix=='0':
				break
			i+=5
		result=int(result,2)
		res.append(result)
	else:
		lenTypeId=int(packet[6],2)
		r=[]
		if lenTypeId==0:
			subLen=int(packet[7:7+15],2)
			#print("OPERATOR LEN", subLen)
			parsePacket(packet[7+15:7+15+subLen],r)
			cursor=7+15+subLen
		else:
			nPackets=int(packet[7:7+11],2)
			#print("OPERATOR NUM", nPackets)
			cursor=7+11+parsePacket(packet[7+11:],r,nPackets-1)
		if typeID==0:
			res.append(sum(r))
		elif typeID==1:
			res.append(np.prod(r))
		elif typeID==2:
			res.append(min(r))
		elif typeID==3:
			res.append(max(r))
		elif typeID==5:
			if r[0]>r[1]:
				res.append(1)
			else:
				res.append(0)
		elif typeID==6:
			if r[1]>r[0]:
				res.append(1)
			else:
				res.append(0)
		elif typeID==7:
			if r[1]==r[0]:
				res.append(1)
			else:
				res.append(0)
	packetLength=len(packet[cursor:])
	if packetLength>0 and decodeMax>0:
		if int(packet[cursor:],2)!=0:
			cursor+=parsePacket(packet[cursor:],res,decodeMax-1)
	return cursor

packet=readData('in.txt')
r=[]
parsePacket(packet,r)
print(a)
print(r[0])