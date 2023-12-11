import math
from operator import add

def run(a,param,i):
    #print param,i
    #i=0
    rel_base=run.r_b
    while True:
        jump=4
        modes=[]
        #print i
        digits=[int(x) for x in list(str(a[i]))]
        opcode=int(str(a[i])[-2:])
        digits=digits[::-1]
        if len(digits)>2:
            for d in digits[2:]:
                modes.append(d)
        modes.extend([0]*(3-len(modes)))
        #print modes,opcode,rel_base, i
        #print "instruction:",a[i],a[i+1],a[i+2],a[i+3]
        
        if opcode==1:
           x=0
           y=0
           if modes[0]==1:
                x=a[i+1]
           elif modes[0]==2:
                x=a[a[i+1]+rel_base]
           else:
                x=a[a[i+1]]
            
           if modes[1]==1:
                y=a[i+2]
           elif modes[1]==2:
                y=a[a[i+2]+rel_base]
           else:
                y=a[a[i+2]]
           
           if modes[2]==2:
                a[a[i+3]+rel_base]=x+y
           else:
                a[a[i+3]]=x+y
        if opcode==2:
            #print "instruction:",a[i],a[i+1],a[i+2],a[i+3]
           x=0
           y=0
           if modes[0]==1:
                x=a[i+1]
           elif modes[0]==2:
                x=a[a[i+1]+rel_base]
           else:
                x=a[a[i+1]]
            
           if modes[1]==1:
                y=a[i+2]
           elif modes[1]==2:
                y=a[a[i+2]+rel_base]
           else:
                y=a[a[i+2]]
           
           if modes[2]==2:
                a[a[i+3]+rel_base]=x*y
           else:
                a[a[i+3]]=x*y
        elif opcode==3:
            #n=int(input("please provide parameter "))
            n=param
            if modes[0]==2:
                a[a[i+1]+rel_base]=n
            else:
                a[a[i+1]]=n
            jump=2
        elif opcode==4:
            if modes[0]==1:
                #print "output:", a[i+1]
                return a[i+1],i+2
            elif modes[0]==2:
                #print "output:", a[a[i+1]+rel_base]
                return a[a[i+1]+rel_base],i+2
            else:
                #print "output:",a[a[i+1]]
                return a[a[i+1]],i+2
            jump=2
        elif opcode==5:
           x=0
           y=0
           if modes[0]==1:
                x=a[i+1]
           elif modes[0]==2:
                x=a[a[i+1]+rel_base]
           else:
                x=a[a[i+1]]
           if modes[1]==1:
                y=a[i+2]
           elif modes[1]==2:
                y=a[a[i+2]+rel_base]
           else:
                y=a[a[i+2]]
           if x!=0:
               i=y
               jump=0
           else:
               jump=3
        
        elif opcode==6:
           x=0
           y=0
           if modes[0]==1:
                x=a[i+1]
           elif modes[0]==2:
                x=a[a[i+1]+rel_base]
           else:
                x=a[a[i+1]]
           if modes[1]==1:
                y=a[i+2]
           elif modes[1]==2:
                y=a[a[i+2]+rel_base]
           else:
                y=a[a[i+2]]
           if x==0:
               i=y
               jump=0
           else:
               jump=3
        
        elif opcode==7:
           x=0
           y=0
           if modes[0]==1:
                x=a[i+1]
           elif modes[0]==2:
                x=a[a[i+1]+rel_base]
           else:
                x=a[a[i+1]]
           if modes[1]==1:
                y=a[i+2]
           elif modes[1]==2:
                y=a[a[i+2]+rel_base]
           else:
                y=a[a[i+2]]
           if x<y:
               if modes[2]==2:
                   a[a[i+3]+rel_base]=1
               else:
                   a[a[i+3]]=1
           else:
               if modes[2]==2:
                   a[a[i+3]+rel_base]=0
               else:
                   a[a[i+3]]=0
        elif opcode==8:
           x=0
           y=0
           if modes[0]==1:
                x=a[i+1]
           elif modes[0]==2:
                x=a[a[i+1]+rel_base]
           else:
                x=a[a[i+1]]
           if modes[1]==1:
                y=a[i+2]
           elif modes[1]==2:
                y=a[a[i+2]+rel_base]
           else:
                y=a[a[i+2]]
           if x==y:
               if modes[2]==2:
                   a[a[i+3]+rel_base]=1
               else:
                   a[a[i+3]]=1
           else:
               if modes[2]==2:
                   a[a[i+3]+rel_base]=0
               else:
                   a[a[i+3]]=0

        elif opcode==9:
            x=0
            if modes[0]==0:
                x=a[a[i+1]]
            elif modes[0]==1:
                x=a[i+1]
            elif modes[0]==2:
                x=a[a[i+1]+rel_base]

            rel_base+=x
            run.r_b=rel_base
            jump=2
        elif opcode==99:
            #print "instruction:",a[i]
            #print "END!"
            return "END",""
            break
        i=i+jump
    return a[0]

run.r_b=0

def single(aa,i,param):
    o1,i=run(aa,param,i)
    if o1=="END":
        return "END",""
    o2,i=run(aa,param,i)
    return [o1,o2],i

a=[]
with open("in.txt") as f:
    for line in f.readlines():
        aa=[int(x) for x in line.split(',')]

aa.extend(2000*[0])


colors={}
d=[0,1]
pos=(0,0)
o,i= single(aa,0,1)
if o[1]==0:
    d=[-d[1],d[0]]
else:
    d=[d[1],-d[0]]
#print o,d
colors[pos]=o[0]
pos=(pos[0]+d[0],pos[1]+d[1])

while True:
    if pos in colors:
        col=colors[pos]
    else:
        col=0
    o,i= single(aa,i,col)
    if o=="END":
        break
    if o[1]==0:
        d=[-d[1],d[0]]
    else:
        d=[d[1],-d[0]]
    #print o,d
    colors[pos]=o[0]
    pos=(pos[0]+d[0],pos[1]+d[1])

x=[]
y=[]
for a in colors:
    if colors[a]==1:
        x.append(a[0])
        y.append(a[1])

s=[]
for k in range(0,6):
    ss=""
    for l in range(0,40):
        if (l,-k) in colors and colors[(l,-k)]==1:
            ss+="X"
        else:
            ss+=" "
    print ss

print "min:"
print min(x),min(y)
print "max:"
print max(x),max(y)

print len(colors)
