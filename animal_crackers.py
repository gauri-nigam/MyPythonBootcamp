def animal_crackers(text):
	myList=text.split()
	if myList[0][0] == myList[1][0]:
		return True
	else :
		return False

print(animal_crackers("level lame"))
