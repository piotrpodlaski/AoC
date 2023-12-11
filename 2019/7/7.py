import math
import itertools

def run_single(a,params,i):
    out=0
    while True:
        jump=4
        modes=[]
        digits=[int(x) for x in list(str(a[i]))]
        opcode=int(str(a[i])[-2:])
        digits=digits[::-1]
        if len(digits)>2:
            for d in digits[2:]:
                modes.append(d)
        modes.extend([0]*(3-len(modes)))
#        print modes,opcode
        
        if opcode==1:
            #print "instruction:",a[i],a[i+1],a[i+2],a[i+3]
           x=0
           y=0
           if modes[0]==1:
                x=a[i+1]
           else:
                x=a[a[i+1]]
            
           if modes[1]==1:
                y=a[i+2]
           else:
                y=a[a[i+2]]
           a[a[i+3]]=x+y
        if opcode==2:
            #print "instruction:",a[i],a[i+1],a[i+2],a[i+3]
           x=0
           y=0
           if modes[0]==1:
                x=a[i+1]
           else:
                x=a[a[i+1]]
            
           if modes[1]==1:
                y=a[i+2]
           else:
                y=a[a[i+2]]
           a[a[i+3]]=x*y
        elif opcode==3:
            #n=int(input("please provide parameter "))
            #print params
            n=params[-1]
            params.pop()
            a[a[i+1]]=n
            jump=2
        elif opcode==4:
            if modes[0]==1:
                out=a[i+1]
                #print "output:", a[i+1]
            else:
                out=a[a[i+1]]
                #print "output:",a[a[i+1]]
            i+=2
            return out,i
            jump=2
        elif opcode==5:
           x=0
           y=0
           if modes[0]==1:
                x=a[i+1]
           else:
                x=a[a[i+1]]
           if modes[1]==1:
                y=a[i+2]
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
           else:
                x=a[a[i+1]]
           if modes[1]==1:
                y=a[i+2]
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
           else:
                x=a[a[i+1]]
           if modes[1]==1:
                y=a[i+2]
           else:
                y=a[a[i+2]]
           if x<y:
               a[a[i+3]]=1
           else:
               a[a[i+3]]=0
        elif opcode==8:
           x=0
           y=0
           if modes[0]==1:
                x=a[i+1]
           else:
                x=a[a[i+1]]
           if modes[1]==1:
                y=a[i+2]
           else:
                y=a[a[i+2]]
           if x==y:
               a[a[i+3]]=1
           else:
               a[a[i+3]]=0
            
        elif opcode==99:
            #print "instruction:",a[i]
            #print "END!"
            return "END",0
            break
        i=i+jump
    return out


def run_all(mems, phase):
    out=0
    i=0
    pcs=[0,0,0,0,0]
    #print run_single(mems[0],[out,phase[0]],pcs[0])
    #print pcs
    for k in range(0,5):
        #print pcs,k
        tmp=[out,phase[k]][:]
        o,pcs[k]=run_single(mems[k],tmp,pcs[k])
        out=o
    #print pcs
    #return
    while True:
        #print pcs,i
        tmp=[out,phase[i]][:]
        o,pcs[i]=run_single(mems[i],[out],pcs[i])
        if o=="END":
            break
        out=o
        if i==4:
            i=0
        else:
            i+=1
    return out


a=[]
with open("in.txt") as f:
    for line in f.readlines():
        aa=[int(x) for x in line.split(',')]


rng=range(0,5)


test= list(itertools.permutations(range(5,10)))

mems=[]


#print run_all(mems,[9,7,8,5,6])

#exit()

out=[]
for c in test:
    mems=[]
    for i in range(0,5):
        mems.append(aa[::])
    out.append(run_all(mems,c))

print max(out)

