def lesser_of_two_evens(a,b):
	if a%2 == 0 and b%2 == 0:
		if a<b:
			ans=a
		else:
			ans=b
	else:
		if a>b:
			ans=a
		else:
			ans=b
	return ans

result=lesser_of_two_evens(2,4)
print(result)
