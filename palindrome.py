def palindrome(str):
	newList=str.split()
	word=newList[0][::-1]
	if word == newList[0]:
		return True
	else:
		return False

print(palindrome("Hello"))