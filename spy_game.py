def spy_game(my_list):
	fl=0
	k=0
	b=False
	for i in range(0,len(my_list)):
		if my_list[i]==0:
			fl=1
			break
	if fl==1:
		for j in range(i,len(my_list)):
			if my_list[j]==0:
				k=1
				break
	if k==1:
		for l in range(j,len(my_list)):
			if my_list[l]==7:
				b=True
	return b

print(spy_game([1,7,2,0,4,5,0]))
