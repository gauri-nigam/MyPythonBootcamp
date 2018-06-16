import string
def ispangram(str,alphabet=string.ascii_lowercase):
	count=0
	for i in range(0,26):
		if alphabet[i] in str:
			count+=1

	if count==26:
		return True
	else:
		return False
print(ispangram("The quick brown fox jumps over the lazy dog"))
