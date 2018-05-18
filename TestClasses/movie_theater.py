### Create a Theater Class ###
	## Attributes ##

	# Theater Name
	# Number of Screens
	# Ticket Price
	# City

	##Methods##
	# add - adds a movie that is being shown at the theater
	# remove - removes the first movie (index 0)
	# list_movies - show all movies being shown at a given time



### Create a Movie Class ###
	## Attributes ##
	# Movie Name
	# Genre
	# Show Time
	# Matinee
	# Rating

class Theater(object):
	def __init__(self, theater_name, number_screens, ticket_price, city):
		self.theater_name = theater_name
		self.number_screens = number_screens
		self.ticket_price = ticket_price
		self.city = city
		self.movies = []

	def add(self, movie):
		self.movies.append(movie)
		return self

	def subtract(self, movie):
		self.movies.pop(0)
		return self

	def list_movies(self):
		for each in self.movies:
			print self.movie.movie_name
			print self.movie.number_screens
			print self.movie.ticket_price
			print self.movie.city
		return self

class Movie(object):
	def __init__(self, movie_name, genre, show_time, rating):
		self.movie_name = movie_name
		self.genre = genre
		self.show_time = show_time
		self.rating = rating
	def details(self):
		print self.movie_name
		print self.genre
		print self.show_time
		print self.matinee
		print self.rating
		return self



movie1 = Movie("The Road", "Drama", "12:00pm", "R")
the_landing = Theater("Regal at The Landing", 12, "$12.00", "Renton").add(movie1).list_movies()










