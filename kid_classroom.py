# Jeff's Code
"""class Classroom(object):
	def __init__(self, roomName):
		self.roomName = roomName
		self.classSize = []

	def speakAll(self):
		for i in self.classSize:
			i.speak

	def addKid(self, kidName):
		self.classSize.append(kidName)

# My Code
class Kid(object):
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
	def speak(self):
		print self.first_name, self.last_name
		return self

kid1 = Kid("Chris", "Fox").speak()
kid2 = Kid("Steve", "Jobs").speak()
kid3 = Kid("Sue", "Chang").speak()
mathClass = Classroom('Math')
mathClass.speakAll()"""

#_________________________
#Ray's Code

class Classroom(object):
	def __init__(self, name):
		self.name = name
		self.kids = []
	def add(self, kid):
		self.kids.append(kid)
	def allSpeak(self):
		print "Class, say your names!"
		for kid in self.kids:
			kid.speak()

class Kid(object):
	def __init__(self, first, last):
		self.first = first
		self.last = last
	def speak(self):
		print "My name is {} {}".format(self.first, self.last)


mike = Kid('mike', 'arbo')
alan = Kid('alan', 'weber')
mathClass = Classroom('math')
mathClass.add(mike)
mathClass.add(alan)
mathClass.allSpeak()
