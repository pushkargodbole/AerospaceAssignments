# This code finds the minimum distance between any two nodal points of the IIT-B campus using the Djikstra's 
# algorithm.
print "               * XYON *"
print "      Pushkar Godbole (09D01005)"
print "- DJIKSTRA'S SHORTEST PATH ALGORITHM -"
print " 1) Lakeside Gate\n 2) Main Gate\n 3) YP Gate\n 4) E\n 5) Temple\n 6) F\n 7) White house\n 8) 3P\n 9) A\n10) D\n11) Shops\n12) Guest house\n13) H10\n14) C\n15) B\n16) SOM\n17) AA\n18) Aero Dept.\n19) MB\n20) H11\n21) Arch\n22) VMCC\n23) Cycle Shop\n24) H12\n25) Tansa\n26) Lib\n27) Tree Labs\n28) H2"
start = int(raw_input("Your start point is (Enter the number corresponding to the desired starting point) : "))-1
nodes = (
"Lakeside Gate",          #0
"Main Gate",              #1
"YP Gate",                #2
"E",                      #3
"Temple",                 #4
"F",                      #5
"White house",            #6
"3P",                     #7
"A",                      #8
"D",                      #9
"Shops",                  #10
"Guest house",            #11
"H10",                    #12
"C",                      #13
"B",                      #14
"SOM",                    #15
"AA",                     #16
"Aero Dept.",             #17
"MB",                     #18
"H11",                    #19
"Arch",                   #20
"VMCC",                   #21
"Cycle Shop",             #22
"H12",                    #23
"Tansa",                  #24
"Lib",                    #25
"Tree Labs",              #26
"H2"                      #27
)
map = []
for i in range(0,len(nodes)) :
	map.append({'edge':[],'length':[]})
map[0]['edge'] = [1,5]
map[0]['length'] = [6,3]
map[1]['edge'] = [0,2,3]
map[1]['length'] = [6,6,1]
map[2]['edge'] = [1,8]
map[2]['length'] = [6,2]
map[3]['edge'] = [1,7,9]
map[3]['length'] = [1,1,5]
map[4]['edge'] = [5]
map[4]['length'] = [8]
map[5]['edge'] = [0,4,6]
map[5]['length'] = [3,8,2]
map[6]['edge'] = [5,7,11]
map[6]['length'] = [2,2,5]
map[7]['edge'] = [3,6,12]
map[7]['length'] = [1,2,6]
map[8]['edge'] = [2,9,10]
map[8]['length'] = [2,3,2]
map[9]['edge'] = [3,8,13]
map[9]['length'] = [5,3,5]
map[10]['edge'] = [8,14]
map[10]['length'] = [2,5]
map[11]['edge'] = [6,12,22]
map[11]['length'] = [5,3,5]
map[12]['edge'] = [7,11,13,15]
map[12]['length'] = [6,3,3,3]
map[13]['edge'] = [9,12,14,16]
map[13]['length'] = [5,3,3,6]
map[14]['edge'] = [10,13,17]
map[14]['length'] = [5,3,3]
map[15]['edge'] = [12,18]
map[15]['length'] = [3,1]
map[16]['edge'] = [13,17,20]
map[16]['length'] = [6,5,5]
map[17]['edge'] = [14,16,21]
map[17]['length'] = [3,5,7]
map[18]['edge'] = [15,19,20,25]
map[18]['length'] = [1,2,1,4]
map[19]['edge'] = [18,22]
map[19]['length'] = [2,1]
map[20]['edge'] = [16,18,21,26]
map[20]['length'] = [5,1,3,5]
map[21]['edge'] = [17,20]
map[21]['length'] = [7,3]
map[22]['edge'] = [11,19,23,24]
map[22]['length'] = [5,1,5,2]
map[23]['edge'] = [22]
map[23]['length'] = [5]
map[24]['edge'] = [22,25,27]
map[24]['length'] = [2,2,5]
map[25]['edge'] = [18,24,26,27]
map[25]['length'] = [4,2,3,5]
map[26]['edge'] = [20,25]
map[26]['length'] = [5,3]
map[27]['edge'] = [24,25]
map[27]['length'] = [5,5]
grid = []
for i in range(0,len(nodes)) :
	grid.append([])
	for j in range(0,len(nodes)) : grid[i].append(100)
	k = 0	
	for j in map[i]['edge'] :
		grid[i][j] = map[i]['length'][k]
		k = k+1
out = []
for i in range(0,len(nodes)) :
	out.append({'path':nodes[start],'dist':grid[start][i]})
done = [start]
for i in range(0,len(nodes)-1) :
	minimum = 100
	for j in done :
		temp = grid[j]
		for k in done : temp[k] = 100
		if j == start : newmin = min(temp)
		else : newmin = min(temp)+out[j]['dist']		
		if newmin < minimum :
			minimum = newmin
			min_i = temp.index(min(temp))
	newnode = min_i
	done.append(newnode)
	for j in range(0,len(nodes)) :
		if j not in done :
			if out[j]['dist'] > (out[newnode]['dist']+grid[newnode][j]) :
				out[j]['dist'] = out[newnode]['dist']+grid[newnode][j]
				out[j]['path'] = out[newnode]['path'] + ' -> ' + nodes[newnode]
for i in range(0, len(nodes)) :
	if i != start :
		out[i]['path'] = out[i]['path'] + ' -> ' + nodes[i]
print 
for i in range(0,len(nodes)) :
	if i != start :
		print nodes[start] + ' -> ' + nodes[i]
		print "Path : " + out[i]['path']
		print "Distance = " + str(out[i]['dist']) + "\n"
