def readData(fname):
	folds=[]
	dots=set()

	with open(fname) as f:
		for l in f.readlines():
			if l[-1]=='\n':
				l=l[:-1]
			if len(l)==0:
				continue
			if l[0]=='f':
				l=l.split(' ')[-1]
				if l[0]=='x':
					folds.append((int(l[2:]),0))
				if l[0]=='y':
					folds.append((0,int(l[2:])))
			else:
				l=tuple(int(x) for x in l.split(','))
				dots.add(l)

	return dots,folds

def doOneFold(dots,fold):
	xFold=fold[0]
	yFold=fold[1]
	behindFold=set()
	for d in dots:
		if (d[0]>xFold and xFold>0) or (d[1]>yFold and yFold>0):
			behindFold.add(d)
	dots=dots-behindFold
	for d in behindFold:
		if xFold>0:
			dots.add((2*xFold-d[0],d[1]))
		elif yFold>0:
			dots.add((d[0],2*yFold-d[1]))
	return dots


def drawDots(dots):
	xmax=max([x[0] for x in dots])+1
	ymax=max([x[1] for x in dots])+1
	for y in range(ymax):
		l=""
		for x in range(xmax):
			if (x,y) in dots:
				l+= u"\u2588"
			else:
				l+=" "
		print(l)

dots,folds=readData('in.txt')
dots=doOneFold(dots,folds[0])
print(len(dots))
for f in folds[1:]:
	dots=doOneFold(dots,f)

drawDots(dots)