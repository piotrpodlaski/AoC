

with open("in.txt") as f:
    for line in f.readlines():
        a=[int(x) for x in line[:-1]]


nx=25
ny=6
n=nx*ny

layers=[a[i:i+n] for i in range(0,len(a),n)]

print len(layers)


zeros=[x.count(0) for x in layers]
k= zeros.index(min(zeros))

print layers[k].count(1)*layers[k].count(2)

a=layers[0]

for l in layers:
    for i in range(0,len(l)):
            if a[i]==2:
                a[i]=l[i]
s=""
for x in a:
    if x==1:
        s+="X"
    else:
        s+=" "



for i in range(0,ny):
    print s[i*nx:i*nx+nx]
