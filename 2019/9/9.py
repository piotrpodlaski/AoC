import math

def run(a):
    i=0
    rel_base=0
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
            n=int(input("please provide parameter "))
            if modes[0]==2:
                a[a[i+1]+rel_base]=n
            else:
                a[a[i+1]]=n
            jump=2
        elif opcode==4:
            if modes[0]==1:
                print "output:", a[i+1]
            if modes[0]==2:
                print "output:", a[a[i+1]+rel_base]
            else:
                print "output:",a[a[i+1]]
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
            jump=2
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

aa.extend(200*[0])
run(aa)
