print "                      * XYON *"
print "             Pushkar Godbole (09D01005)"
print "Travelling Politician Problem using Simulated Annealing"
from string import strip, split
from math import sqrt, exp
from random import random, randint
from pylab import figure, bar, show
def delta_cost(city1,city2) :
	cost = 0
	h_cross = 1500.0
	v_cross = 2000.0
	dist_cost = sqrt((city1[0]-city2[0])**2+(city1[1]-city2[1])**2)*100.0
	cost = cost + dist_cost
	if city1[2] in [1,2] and city2[2] in [3,4] or city1[2] in [3,4] and city2[2] in [1,2] :
		cost = cost + v_cross
	if city1[2] in [2,3] and city2[2] in [1,4] or city1[2] in [1,4] and city2[2] in [2,3] :
		cost = cost + h_cross
	return(cost)

def total_cost(mydict,permutation) :
	cost = 0
	length = len(permutation)
	for i in range(0,length-1) :
		cost = cost + delta_cost(mydict[permutation[i]],mydict[permutation[i+1]])
	return(cost)

def rand_swap(mylist) :
	newlist = []
	newlist.extend(mylist)
	length = len(newlist)
	x = randint(1,length-1)
	y = randint(1,length-1)
	temp = newlist[x]
	newlist[x] = newlist[y]
	newlist[y] = temp
	return(newlist)

cities = {}
for line in open('cities.txt','r') :
	fields = line .split()
	cities[fields[0]] = [float(fields[1]),float(fields[2])]
Q = [[],[],[],[]]
Q[0] = ['Lucknow','Patna','Gangtok','Agartala','Shillong','Itanagar','Dispur','Kohima','Imphal','Aizawl']
Q[1] = ['Jaipur','Delhi','Chandigarh','Shrinagar','Shimla','Dehradun']
Q[2] = ['Gandhinagar','Mumbai','Panaji','Bangalore','Pondicherry','Thiruvanantapuram','Chennai','Hyderabad','Bhopal']
Q[3] = ['Kolkata','Ranchi','Raipur','Bhubaneshwar']
for i in range(0,4) :
	for city in Q[i] : cities[city].append(i+1)

perm = ['Chandigarh','Patna','Gangtok','Agartala','Shimla','Shillong','Kohima','Imphal','Delhi','Lucknow','Shrinagar','Dehradun',
'Gandhinagar','Mumbai','Itanagar','Dispur','Panaji','Bangalore','Pondicherry','Thiruvanantapuram','Chennai','Hyderabad','Bhopal',
'Kolkata','Aizawl','Jaipur','Ranchi','Raipur','Bhubaneshwar']

cost = total_cost(cities,perm)
min_cost = cost
min_perm = []
min_perm.extend(perm)
T = 10000.0
a = 0.96
c = []
print "T =",T
print "a =",a
print '->',min_cost
for i in range (0,200) :
	count = 0
	for j in range(0,10000) :
		perm1 = rand_swap(perm)
		cost1 = total_cost(cities,perm1)
		prob = random()
		if cost1 < cost or prob < exp(-abs(cost-cost1)/T) :
			if prob < exp(-abs(cost-cost1)/T) :
				count = count+1
			perm = []
			perm.extend(perm1)
			cost = cost1
        if cost1 < min_cost :
			min_perm = []
			min_perm.extend(perm1)
			min_cost = cost1
			print '->',min_cost
	T = T*a
	c.append(count)
path = ''
for city in min_perm : path = path + ' -> ' + city
print path
print 'cost =',min_cost
x = range(1,len(c)+1)
fig = figure()
ax = fig.add_subplot(1,1,1)
ax.bar(x,c)
ax.set_xlabel('Temperature-cycle no.')
ax.set_ylabel('No. of up-hill moves')
show()
