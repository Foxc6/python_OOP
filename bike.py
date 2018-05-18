class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	
	def display_info(self):
		print self.price
		print self.max_speed
		print self.miles
		return self



	def ride(self):
		print "Riding"
		self.miles += 10
		print self.miles
		return self

	def reverse(self):
		print "Reversing"
		self.miles -= 5
		if self.miles < 0:
			self.miles = 0
		print self.miles
		return self

bike1 = Bike(100, "20mph")
bike2 = Bike(75, "15mph")
bike3 = Bike(110, "22mph")


bike1.display_info().ride().ride().ride().reverse()
bike2.display_info().ride().ride().reverse().reverse()
bike3.display_info().reverse().reverse().reverse()
