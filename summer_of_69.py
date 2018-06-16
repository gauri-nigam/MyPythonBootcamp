
def summer_of_69(arr):
	sum=0
	if 6 in arr and 9 in arr:
		first_index=arr.index(6)
		second_index=arr.index(9)
		for i in range(0,first_index):
			sum+=arr[i]
		for i in range(second_index+1,len(arr)):
			sum+=arr[i]
	else:
		for i in range(0,len(arr)):
			sum+=arr[i]


	print(sum)


summer_of_69([2,1,6,9,11])
