def master_yoda(str):
	my_list=[]
	newstr=""
	my_list=str.split()
	newstr=my_list[::-1]

	return ' '.join(newstr)

print(master_yoda("i am home"))
