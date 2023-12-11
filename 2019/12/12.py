import numpy as np
from copy import deepcopy

def print_single(aa):
    print "pos <x={},y={},z={}>\tvel<x={},y={},z={}>".format(aa[0][0],aa[0][1],aa[0][2],aa[1][0],aa[1][1],aa[1][2])

def print_all(a):
    for aa in a:
        print_single(aa)
a=[]
with open('in.txt') as f:
    for l in f.readlines():
        a.append([int(x[2:]) for x in l[1:-2].split(', ')])

a=[[np.array(x),np.array([0,0,0])] for x in a]

print "Iteration {}:".format(0)
print_all(a)
a0=deepcopy(a)

i=0
while True:
    #print
    #print "Iteration {}:".format(i)
    aa=deepcopy(a)
    for j in range(0,len(a)):
        for k in range(0,len(a)):
            moon1=aa[j]
            moon2=aa[k]
            if j==1 and False:
                print moon1[0],moon2[0]
            for l in range(0,3):
                if moon1[0][l]>moon2[0][l]:
                    a[j][1][l]-=1
                elif moon1[0][l]<moon2[0][l]:
                    a[j][1][l]+=1
        if j==1 and False:
            print a[j][1]
        a[j][0]+=a[j][1]

    #print_all(a)
    i+=1
    
    eq=True
    for j in range(0,len(a)):
        v=a0[j][0]==a[j][0]
        v2=a0[j][1]==a[j][1]
        if v.all()==False or v2.all()==False:
            eq=False
            break

    if i%100000==0:
        print i
        break
    if eq:
        print i
        break

en=0
for aa in a:
    pot=sum([abs(x) for x in aa[0]])
    kin=sum([abs(x) for x in aa[1]])
    en+=kin*pot

print en
