import math

def get_nodes(arr):
    x=0
    y=0
    out=[]
    for a in arr:
        d=a[0]
        l=int(a[1:])
        if d=='R':
            for i in range(l):
                x+=1
                out.append([x,y])
        elif d=='L':
            for i in range(l):
                x-=1
                out.append([x,y])
        elif d=='U':
            for i in range(l):
                y+=1
                out.append([x,y])
        elif d=='D':
            for i in range(l):
                y-=1
                out.append([x,y])
    return out

def get_nodes2(arr):
    x=0
    y=0
    out=[]
    for a in arr:
        d=a[0]
        l=int(a[1:])
        if d=='R':
            out.append([x,y,x+l,y])
            x+=l
        elif d=='L':
            out.append([x,y,x-l,y])
            x-=l
        elif d=='U':
            out.append([x,y,x,y+l])
            y+=l
        elif d=='D':
            out.append([x,y,x,y-l])
            y-=l
    return out



def parse():
    with open("in.txt") as f:
        a=f.readline().split(",")
        b=f.readline().split(",")
    one=get_nodes2(a)
    two=get_nodes2(b)
    return one,two
    

a,b= parse()

print a,b

print len(a), len(b)

print " "

out=[]
out2=[]
l1=0
l2=0
for aa in a:
    l1+=abs(aa[0]-aa[2])+abs(aa[1]-aa[3])
    l2=0
    for bb in b:
        l2+=abs(bb[0]-bb[2])+abs(bb[1]-bb[3])
        print l1, l2
        if aa[0]==aa[2] and bb[1]==bb[3]:
            if aa[0]<max(bb[0],bb[2]) and aa[0]>min(bb[0],bb[2]) and bb[1]<max(aa[1],aa[3]) and bb[1]>min(aa[1],aa[3]):
                out.append(abs(aa[0])+abs(bb[1]))
                out2.append(l1-abs(bb[3]-aa[3])+l2-abs(aa[2]-bb[2]))
                print aa,bb,aa[0],bb[1]
        if bb[0]==bb[2] and aa[1]==aa[3]:
            if bb[0]<max(aa[0],aa[2]) and bb[0]>min(aa[0],aa[2]) and aa[1]<max(bb[1],bb[3]) and aa[1]>min(bb[1],bb[3]):
                out.append(abs(bb[0])+abs(aa[1]))
                out2.append(l1-abs(aa[2]-bb[2])+l2-abs(bb[3]-aa[3]))
                print aa,bb,bb[0],aa[1]

print min(out2)

#intersec=[x for x in a if x in b]
#dists=[abs(x)+abs(y) for x,y in intersec]
#print min(dists)
