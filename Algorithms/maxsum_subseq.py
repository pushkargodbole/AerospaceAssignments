
import sys
def maxsum(array) :
	maxsum = 0
	maxstart = 0
	maxend = 0
	thissum = 0
	thisstart = 0
	thisend = 0
	for i in range (0,len(array)) :
		thissum = thissum + array[i]
		thisend = i
		if(thissum > maxsum) :
			maxsum = thissum
			maxstart = thisstart
			maxend = thisend
		if(thissum <= 0) :
			thissum = 0
			thisstart = i+1
	if (maxstart == maxend) : print [array[maxstart]]
	else : print array[maxstart:maxend+1]
	print "Max Sum =", maxsum
