
#test array = [22,9,7,29,1,25]
def inserstionSort(arr):
	"""
	This function is used to take an array and sort the array in the ascending order with the help of insertion sort
	"""
	for i in range(1,len(arr)):
		key = arr[i]
		j=i-1
		while (j>=0) & ( key < arr[j]):
			arr[j+1]=arr[j]
			j=j-1
		arr[j+1]=key		
	
	return(arr)



if __name__ == '__main__':
	test_arr=[22,9,7,29,1,25]
	print(inserstionSort(test_arr))