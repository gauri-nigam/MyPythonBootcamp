def find_33(nums):
	for i in range(0,len(nums)):
		if nums[i] == 3:
			i+=1
			if nums[i] == 3:
				return True
			else:
				return False
print(find_33([1,3,3]))
