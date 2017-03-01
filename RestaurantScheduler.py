class Table:
	def __init__(self, capacity):
		self.maxCapacity = capacity
		# the restaurant is open for 11hrs
		# if serving one set of customer takes 1hr 45 mins (i.e. Wait Time)
		# one table can be used 6 times in a day
		self.availableTimeSlots = 6

	def seatPeople(self,peopleCount):
		self.peopleCount = peopleCount

	def waitTime(self):
		# assuming one person orders two items that takes 30mins to prepare
		# also assuming each person takes 45mins to eat their whole meal
		return (30*2) + 45
	def isTimeConstrained(self):
		# No	 booking time constraints for extra-large table
		if self.maxCapacity>=12:
			return false
		else:
			return true
	def totalAvailableTimeSlots(self):
		return self.availableTimeSlots
	def useTable(self):
		self.availableTimeSlots -= 1
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
		
		self.xLargeTables = [Table(12)]
		self.largeTables = [Table(6),Table(6),Table(6)]
		self.medTables = [Table(4),Table(4),Table(4),Table(4),Table(4),Table(4),Table(4),Table(4)]
		self.smallTables = [Table(2),Table(2),Table(2),Table(2)]
	def bookTable(self,numberOfPeople):
		if numberOfPeople>12:
			print "Can not accomodate so many people"
			return None

		elif numberOfPeople > 6 and numberOfPeople <=12:
			if(self.xLargeTables[0].totalAvailableTimeSlots()>0):
				pass
			else:
				try:
					self.xLargeTables = self.xLargeTables[1:]
				except IndexError:
					print "No more extra-large tables left"
					return None
			self.xLargeTables[0].useTable()

			return self.xLargeTables[0]

		elif numberOfPeople > 4 and numberOfPeople <=6:
			if(self.largeTables[0].totalAvailableTimeSlots()>0):
				pass
			else:
				try:
					self.largeTables = self.largeTables[1:]
					
				except IndexError:
					print "No more large tables left"
					return None
			self.largeTables[0].useTable()
			return self.largeTables[0]

		elif numberOfPeople > 2 and numberOfPeople <=4:
			if(self.medTables[0].totalAvailableTimeSlots()>0):
				pass
			else:
				try:
					self.medTables = self.medTables[1:]
				except IndexError:
					print "No more medium tables left"
					return None

			self.medTables[0].useTable()
			return self.medTables[0]
		elif numberOfPeople > 0 and numberOfPeople <=2:
			if(self.smallTables[0].totalAvailableTimeSlots()>0):
				pass
			else:
				try:
					self.smallTables = self.smallTables[1:]
					
				except IndexError:
					print "No more small tables left"
					return None

			self.smallTables[0].useTable()
			return self.smallTables[0]

		elif numberOfPeople <=0:
			print "Invalide Number of People"
			return None


if __name__ == "__main__":
	R = Restaurant()
	T =  R.bookTable(6)
	
	if T:
		# will successfully book Large table
		print T.Name()
	
	T = R.bookTable(20)
	if T:
		# Table wont get booked, too many people
		print T.Name()