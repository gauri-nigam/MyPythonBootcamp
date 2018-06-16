class line():
	def __init__(self,coor1,coor2):
		self.coor1 = coor1
		self.coor2 = coor2

	def distance(self):
		dist = ((self.coor1[0] - self.coor2[0])**2 + (self.coor1[1] - self.coor2[1])**2)**0.5
		print(f"Distance is {dist}")
	
	def slope(self):
		slp = (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])
		print(f"Slope is {slp}")	

coordinate1 = (3,2)
coordinate2 = (8,10)

li = line(coordinate1,coordinate2)	#object instantiation

li.distance()
li.slope()