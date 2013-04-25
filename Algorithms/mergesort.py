from math import ceil
def sort(array) :
	length = len(array)
	if length > 1 :
		subarray1 = array[0:int(ceil(length/2))]
		subarray2 = array[int(ceil(length/2)):]
		sorted_subarray1 = sort(subarray1)
		sorted_subarray2 = sort(subarray2)
		return merge(sorted_subarray1, sorted_subarray2)
	elif length == 1 :
		return(array)

def merge(array1, array2) :
	array1_counter = 0
	array2_counter = 0
	merged_array = []
	while array1_counter < len(array1) and array2_counter < len(array2) :
		if array1[array1_counter] > array2[array2_counter] :
			merged_array.append(array2[array2_counter])
			array2_counter+=1
		else :
			merged_array.append(array1[array1_counter])
			array1_counter+=1
	if array1_counter < len(array1) :
		i = array1_counter
		while i < len(array1) :
			merged_array.append(array1[i])
			i+=1
	elif array2_counter < len(array2) :
		i = array2_counter
		while i < len(array2) :
			merged_array.append(array2[i])
			i+=1
	return merged_array

print sort([3,2,1,4,7,2,9,16,3,24])
