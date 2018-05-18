class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100
	def walk(self):
		self.health = self.health - 1
		return self
	def run(self):
		self.health = self.health - 5
		return self
	def display_health(self):
		print self.name + "'s health is", self.health
		return self

class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health = 150
	def pet(self):
		self.health += 5
		return self

class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health = 170
	def fly(self):
		self.health -= 5
		print "I'm a Dragon!"
		return self









animal1 = Animal("Bob").walk().walk().walk().run().run().display_health()
dog1 = Dog("Summer").walk().walk().walk().run().run().pet().display_health()
dragon1 = Dragon("Drogon").fly().display_health()
#animal2 = Animal("fail").pet()
#animal3 = Animal("Steve").fly()
#dog2 = Dog("fail").fly()
#dragon2 = Dragon("lshdg").pet



