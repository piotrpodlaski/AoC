import math

def run(a):
    i=0
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
            n=int(input("please provide parameter "))
            a[a[i+1]]=n
            jump=2
        elif opcode==4:
            if modes[0]==1:
                print "output:", a[i+1]
            else:
                print "output:",a[a[i+1]]
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
            break
        i=i+jump
    return a[0]


a=[]
with open("in.txt") as f:
    for line in f.readlines():
        aa=[int(x) for x in line.split(',')]

run(aa)
