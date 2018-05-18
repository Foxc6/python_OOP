class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if price > 10000:
			self.tax = 0.15
		else: 
			self.tax = 0.12
		self.display_all()

	def display_all(self):
		print "Price:", self.price
		print "Speed:", self.speed
		print "Fuel:", self.fuel
		print "Mileage:", self.mileage
		print "Tax:", self.tax
		return self

car1 = Car(100, "15mph", "1mpg", 100000)
car2 = Car(12000, "150mph", "32mpg", 116000)
car3 = Car(2000, "110mph", "30mpg", 16000)
car4 = Car(9999, "160mph", "30mpg", 10670)
car5 = Car(10001, "160mph", "30mpg", 16000)
car6 = Car(10001, "160mph", "30mpg", 16000)
car7 = Car(10001, "160mph", "30mpg", 16000)
car8 = Car(10001, "160mph", "30mpg", 16000)
car8 = Car(10001, "160mph", "30mpg", 16000)
car9 = Car(10001, "160mph", "30mpg", 16000)
car10 = Car(10001, "160mph", "30mpg", 16000)
