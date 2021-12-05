def readData(fname):
	lines=[]
	with open(fname) as f:
		for l in f.readlines():
			l=l.split('->')
			start=[int(x) for x in l[0].split(',')]
			stop=[int(x) for x in l[1].split(',')]
			lines.append([start,stop])
		return lines


def markLines(lines, bypassHV=False):
	diagram={}
	for l in lines:
		[x0,y0]=l[0]
		[x1,y1]=l[1]
		dx=x1-x0
		dy=y1-y0
		if dx!=0:
			dx=dx/abs(dx)
		if dy!=0:
			dy=dy/abs(dy)
		if dx*dy==0 or bypassHV:
			# print("start:",x0,y0,dx,dy)
			x=x0
			y=y0
			while True:
				diagram[(x,y)]=diagram.get((x,y),0)+1
				if x==x1 and y==y1:
					break
				x+=dx
				y+=dy
				# print(x,y)
	return diagram

def countMultiples(diagram):
	return len([x for x in diagram.values() if x>1])


lines=readData('in.txt')
print(countMultiples(markLines(lines)))
print(countMultiples(markLines(lines,True)))