import math

def test(a,x,y):
    a[1]=x
    a[2]=y
    i=0
    while True:
        if a[i]==1:
            #print "instruction:",a[i],a[i+1],a[i+2],a[i+3]
            a[a[i+3]]=a[a[i+1]]+a[a[i+2]]
        elif a[i]==2:
            #print "instruction:",a[i],a[i+1],a[i+2],a[i+3]
            a[a[i+3]]=a[a[i+1]]*a[a[i+2]]
        elif a[i]==99:
            #print "instruction:",a[i]
            #print "END!"
            break
        i=i+4
    return a[0]


a=[]
with open("in.txt") as f:
    for line in f.readlines():
        aa=[int(x) for x in line.split(',')]

for x in range(0,100):
    for y in range(0,100):
        b=aa[:]
        if test(b,x,y)==19690720:
            print 100*x+y

