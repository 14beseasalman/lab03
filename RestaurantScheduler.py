from collections import deque

class Table:
	def __init__(self, capacity, ts):
		self.maxCapacity = capacity
		self.timeslot=ts
		

	def seatPeople(self,peopleCount):
		self.peopleCount = peopleCount

	def waitTime(self):
		# assuming one person orders two items that takes 30mins to prepare
		# also assuming each person takes 45mins to eat their whole meal
		return (30*2) + 45
	def timeSlot(self):
		return self.timeslot	

	def Name(self):
		if self.maxCapacity > 6 and self.maxCapacity <=12:
			return "Extra Large Table"
		elif self.maxCapacity > 4 and self.maxCapacity <=6:
			return "Large Table"
		elif self.maxCapacity > 2 and self.maxCapacity <=4:
			return "Medium Table"
		elif self.maxCapacity > 0 and self.maxCapacity <=2:
			return "Small Table"

class Restaurant:
	def __init__(self):
		# the restaurant is open for 11hrs
		# if serving one set of customer takes 1hr 45 mins (i.e. Wait Time)
		# one table can be used 6 times in a day
		self.xLargeTables =[]
		self.largeTables = []
		self.medTables = []
		self.smallTables = []
		timeSlots = ["1100-1245","1245-1430","1430-1615","1615-1800","1800-1945","1945-2100"]
		# add xtralarge tables of 12 capacity 6 times
		for x in range(0,6):
			self.xLargeTables.extend([Table(12,timeSlots[x])])
		self.xLargeTables = self.xLargeTables[::-1]
		
		# add largeTables tables of 6 capacity  6 times
		for x in range(0,6):
			self.largeTables.extend([Table(6,timeSlots[x])])
			self.largeTables.extend([Table(6,timeSlots[x])])
			self.largeTables.extend([Table(6,timeSlots[x])])
		self.largeTables = self.largeTables[::-1]

		# add medTables tables of 4 capacity  6 times
		for x in range(0,6):
			self.medTables.extend([Table(4,timeSlots[x])])
			self.medTables.extend([Table(4,timeSlots[x])])
			self.medTables.extend([Table(4,timeSlots[x])])
			self.medTables.extend([Table(4,timeSlots[x])])
			self.medTables.extend([Table(4,timeSlots[x])])
			self.medTables.extend([Table(4,timeSlots[x])])
			self.medTables.extend([Table(4,timeSlots[x])])
			self.medTables.extend([Table(4,timeSlots[x])])
		self.medTables = self.medTables[::-1]

		# add medTables tables of 2 capacity  6 times
		for x in range(0,6):
			self.smallTables.extend([Table(2,timeSlots[x])])
			self.smallTables.extend([Table(2,timeSlots[x])])
			self.smallTables.extend([Table(2,timeSlots[x])])
			self.smallTables.extend([Table(2,timeSlots[x])])
		self.smallTables = self.smallTables[::-1]


	def bookTable(self,numberOfPeople):
		try:
			numberOfPeople = int(numberOfPeople)
		except ValueError:
			print "Invalid Number of People"
			return None
		
		if numberOfPeople>12:
			print "Can not accomodate so many people"
			return None

		elif numberOfPeople > 6 and numberOfPeople <=12:
			try:
				return self.xLargeTables.pop()
			except IndexError as e:
				print "No more Extra Large Tables Left"

		elif numberOfPeople > 4 and numberOfPeople <=6:
			try:
				return self.largeTables.pop()
			except IndexError as e:
				print "No more Large Tables Left"
			

		elif numberOfPeople > 2 and numberOfPeople <=4:
			try:
				return self.medTables.pop()
			except IndexError as e:
				print "No more Medium Tables Left"
			

		elif numberOfPeople > 0 and numberOfPeople <=2:
			try:
				return self.smallTables.pop()
			except IndexError as e:
				print "No more Small Tables Left"

		elif numberOfPeople <=0:
			print "Invalid Number of People"
			return None


if __name__ == "__main__":
	R = Restaurant()
	T = R.bookTable(6)
	if T:
		# will successfully book Large table
		print(T.Name() + " (" + T.timeSlot() + ")")
	
	T = R.bookTable(20)
	if T:
		# Table wont get booked, too many people
		print T.Name()