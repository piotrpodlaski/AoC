import itertools
import operator
import copy

global a
a=0
global pa
pa=[]

def readData(fname):
	data=[]
	with open(fname) as f:
		for l in f.readlines():
			if l[-1]=='\n':
				l=l[:-1]

			l=l.split('-')
			data.append((l[0],l[1]))
	return data

def findNodePaths(tunnels):
	nodePaths={}
	for x in tunnels:
		node=nodePaths[x[0]]=nodePaths.get(x[0],set())
		node.add(x[1])

		node=nodePaths[x[1]]=nodePaths.get(x[1],set())
		node.add(x[0])
	return nodePaths

def checkPaths(start, nodePaths,  visited):
	visited=copy.deepcopy(visited)
	if not all(ele.isupper() for ele in start	):
		visited.add(start)
	if start=='end':
		global a
		a+=1
		return
	for n in nodePaths[start]:
		if n in visited:
			continue
		checkPaths(n, nodePaths, visited)

def checkPaths2(start, nodePaths,  visited,sm,path,twice=False):
	#print(start,visited, twice)
	visited=copy.deepcopy(visited)
	path=copy.deepcopy(path)
	path.append(start)
	if not all(ele.isupper() for ele in start	):
		if not twice and start==sm:
			twice=True
	#		print("twice: ",start)
		else:
			visited.add(start)
		
		if start=='end':
			visited.add(start)

	if start=='end':
	#	print("DONE",path)
		global a
		a+=1
		pa.append(path)
		checkPaths2.twice=False
		return
	for n in nodePaths[start]:
		if n in visited:
			continue
		checkPaths2(n, nodePaths, visited,sm,path,twice)


tunnels=readData('in.txt')
nodePaths=findNodePaths(tunnels)

for n in nodePaths['start']:
	checkPaths(n, nodePaths, set(['start']))

print(a)
a=0

small =[]
for x in nodePaths:
	if not all(ele.isupper() for ele in x) and x!='start' and x!='end':
		small.append(x)

for n in nodePaths['start']:
	for s in small:
		checkPaths2(n, nodePaths, set(['start']),s,[])

#to remove double-counted paths
s=['-'.join(p) for p in pa]
print(len(set(s)))