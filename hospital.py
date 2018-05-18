class Hospital(object):
	def __init__(self, name):
		self.name = name
		self.total_beds = 4
		self.patients = []

	def admit(self, patient):
		self.patients.append(patient)
		# Create empty bed lists and maximum number of beds - complete
		total_beds = 6
		beds = [[] for _ in range(total_beds)]

		# Add bed nubers to beds (sub-lists) and initially declare them all as empty - complete
		bed_count = 1
		for bed in range(0, total_beds):
			beds[bed_count - 1].append(bed_count)
			beds[bed_count - 1].append(None)

			bed_count += 1
		
		# Reset bed_counter to iterate though list again
		bed_count = 1
		# If bed is not occuped, add patient to bed
		# NOT COMPLETE
		for patient in self.patients:
			for bed in range(0, total_beds):
				if beds[bed_count - 1][1] == None:
					beds[bed_count - 1][1] = patient.name
				"""else: 
					no_beds = True
			if no_beds == True:
				print "There are not enought beds to admit additional patients at this time :("
				break"""
			bed_count += 1

		print beds
		return self


class Patient(object):
	def __init__(self, patient_id, name, allergies):
		self.id = patient_id
		self.name = name
		self.allergies = allergies
		self.bed_number = None
		

pat1 = Patient(1, "Steve", "Smoke, Pollin, Bug Bites")
pat2 = Patient(2, "Jason", "Smoke, Pollin, Bug Bites")
pat3 = Patient(3, "Chris", "Smoke, Pollin, Bug Bites")
pat4 = Patient(4, "Nicole", "Smoke, Pollin, Bug Bites")
pat5 = Patient(5, "Bob", "Smoke, Pollin, Bug Bites")
pat6 = Patient(6, "Test", "Smoke, Pollin, Bug Bites")
hos1 = Hospital("St Jude").admit(pat1).admit(pat2).admit(pat3).admit(pat4).admit(pat5).admit(pat6)


