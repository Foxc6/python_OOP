class Call(object):
	def __init__(self, unique_id, caller_name, caller_phone_number, time_of_call, reason_for_call):
		self.unique_id = unique_id
		self.caller_name = caller_name
		self.caller_phone_number = caller_phone_number
		self.time_of_call = time_of_call
		self.reason_for_call = reason_for_call

	def display(self):
		print"**********************************************************"
		print "ID:", self.unique_id
		print "Name:", self.caller_name
		print "Phone Number:", self.caller_phone_number
		print "Time of Call:", self.time_of_call
		print "Reason for Call:", self.reason_for_call
		print"**********************************************************"

class CallCenter(object):
	def __init__(self):
		self.calls = []
		self.queue_size = len(self.calls)

	def add(self, call):
		# Add call to the calls list
		self.calls.append(call)
		self.queue_size = len(self.calls)
		return self

	def remove(self, call):
		# Remove call from the beginning of the calls list (index 0)
		self.calls.pop(0)
		self.queue_size = len(self.calls)
		return self

	def info(self):
		# print the name and phone number for each call in the queue as well as the length of the queue
		for call in self.calls:
			print"**********************************************************"
			print "Caller:", call.caller_name
			print "Queue Size:", len(self.calls)
			print"**********************************************************"
		return self



call1 = Call(1, "Steve", 1234567, "10pm", "Complaint")
call2 = Call(2, "Joe", 2345678, "11pm", "I be hella sick")
call3 = Call(3, "Jason", 3456789, "12pm", "Lost Dog")


CallCenter().add(call1).add(call2).add(call3).info()

# Ninja and Hacker Levels to be completed soon!


