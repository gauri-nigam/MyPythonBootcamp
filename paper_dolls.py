def paper_dolls(str):
	newstr=""
	for item in str:
		newstr=newstr+item*3
	return newstr
print(paper_dolls("Hello"))
