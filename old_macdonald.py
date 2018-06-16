def old_mac(name):
	str=""
	for i in range(0,len(name)):
		if i==0 or i==3:
			str=str+name[i].upper()
		else:
			str=str+name[i]
	return str
print(old_mac("macdonalds"))