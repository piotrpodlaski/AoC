import matplotlib.pyplot as plt

def readData(fname):
	with open(fname) as f:
		ages= [int(x) for x in f.readlines()[0].split(',')]
		agesD={}
		for a in ages:
			agesD[a]=agesD.get(a,0)+1
	return agesD

def processOneDay(ages):
	agesNew={}
	for age in ages:
		num=ages[age]
		if age==0:
			agesNew[8]=agesNew.get(8,0)+num
			agesNew[6]=agesNew.get(6,0)+num
		else:
			agesNew[age-1]=agesNew.get(age-1,0)+num
	return agesNew

ages=readData('in.txt')

numFish=sum(ages.values())
population=[numFish]

for i in range(256):
	ages=processOneDay(ages)
	numFish=sum(ages.values())
	population.append(numFish)
	if i==79:
		print(numFish)
print(numFish)
plt.plot(population)
plt.yscale('log')
plt.xlabel('day')
plt.ylabel('population')
plt.show()