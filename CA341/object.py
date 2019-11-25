import time
import datetime
import sys

class Queue:
#The Queue class which holds all of our To-Do Items
	def __init__(self):
		self.holder = []
		# keep track of the size of our Queue
		self.size = 0

	def enqueue(self, item):
	# add to our queue
		self.holder.append(item)
		self.size += 1

	def dequeue(self):
	# remove from our queue
		if self.is_empty():
			print("Nothing left in queue")
		else:
			self.holder.pop(0)
			self.size -= 1

	def peek(self):
		if self.is_empty():
			print("Nothing left in queue")
		else:
		# we just want to peek at the next thing, not remove it
			print(self.holder[0])

	def is_empty(self):
	#utility method to prevent us indexing an empty list, ie is the Queue populated or not
		return self.size == 0

	def show_all(self):
		if self.is_empty():
			print("Nothing left in queue")
		else:
			for to_do_item in self.holder:
				print(to_do_item)
	def size_(self):
		print(self.size)

	def quit(self):
	#stops execution of the whole program
		sys.exit(0)

class ToDoItem:
# each item that can be Qued , is a ToDo item , that is, either a Task or an Event. They share 2 common attributes (Date and Start_time) so we can use
#inheritance to our advantage here 
	def __init__(self, date, start_time):
		self.date = date
		self.start_time = start_time

	def __str__(self):
	# a Parent class __str__ which is modified as per child class
		return "Date -> {} -- Start Time -> {} --".format(self.date, self.start_time)


class Task(ToDoItem):
# A task has 4 attributes , Date, Start_time, Duration and People
# Date and start time is inherited from the Parent class
	def __init__(self, date, duration,start_time,  people):
		self.people = people
		self.duration = duration
		ToDoItem.__init__(self, date, start_time)
	# inheriting parent attributes
	def __str__(self):
	# using the Parent class's __str__ and adding what we need
		return "TASK : " + super().__str__() + '  Duration -> {} hour(s) -- People -> {}'.format(self.duration,  " ".join(self.people))

class Event(ToDoItem):
#An Event has 3 attributes, Date , Start time and a location 
#Date and Start time is inherited from the parent class
	def __init__(self, date, start_time,  location):
		self.location = location
		ToDoItem.__init__(self, date, start_time)
	# Inheriting parent attributes

	def __str__(self):
		return "EVENT : " + super().__str__() + ' Location -> {}'.format(self.location)

class Parser:
#The parser class , is what runs and combines ALL of our other objects into the desired programe 
	def __init__(self):
	# parser has its Data object (Queue), and a dictionary of commands which it can exec
		self.queue = Queue()
		self.commands = {"del" : self.queue.dequeue, "peek" : self.queue.peek, "size" : self.queue.size_, "quit" : self.queue.quit, "show": self.queue.show_all, "help" : self.help}

	def make_task(self, args):
	# utility method to instantiate a task which ensures the correct number of args have been supplied
		try:
			return Task(args[0], args[1], args[2], args[3:])
		except IndexError:
		# if the correct number of arguments HAVENT been supplied, catch the IndexError and tell the user what went wrong
			print("Insufficient arguments supplied to instantiate a TASK requires a minimum of 3 ( String -> Date, String -> Start Time,  Int ->  Duration,  String -> People)")

	def make_event(self, args):
	# utility method to instantiate an Event
		try:
			return Event(args[0], args[1], args[2])
		except IndexError:
			print("Insufficient arguments supplied to instantiate an EVENT, requires 3")

	def choose_item(self,item_type, args):
	# this method chooses what type of ToDoItem needs to be instantiated as per user input
		if item_type == "TASK":
			if self.check_date(args[0]) == 0 and self.check_time(args[2]) == 0:
				# the above checks if the user entered correct date/time formats
				# following C convention, if a function returns 0 it has executed correctly
				return self.make_task(args)
		elif item_type == "EVENT":
			if self.check_date(args[0]) == 0 and self.check_time(args[1]) == 0:
				return self.make_event(args)
		else:
			print("Not a valid ADD command, type help for more informtation")

	def check_date(self, date_arg):
	# function to check whether the user has inputted date in the correct format
		try:
			datetime.datetime.strptime(date_arg, '%Y-%m-%d')
			return 0
		except ValueError:
			print("The date was not supplied in the correct format , 'Year - Month - day'")
	def check_time(self, time_arg):
	# method to check whether the user has inputted time in the correct format
		try:
			time.strptime(time_arg, '%H:%M')
			return 0
		except ValueError:
			print("The time was not supplied in the correct format, 'Hours:Minutes'")

	def parse_input(self):
	# this method takes user input and decides what exactly needs to be done with it
		input_ = input("> ").strip().split()
		command = input_[0]
		arguments = input_[2:]
		# command should be the first thing in the input and the arguments follow on from the 3rd thing in the input
		if command == "add":
		# we need to efficiently parse an ADD command
			if not arguments:
			# make sure add TO-DoOITEM received arguments so it can be instantiated
				print("Not a valid ADD command, no arguments were passed to instantiate your To-Do Item")
				return # quit execution of the function to ensure no errors are thrown
			next_item = self.choose_item(input_[1], arguments)
			if next_item:
				# the condition statement above ensures we dont push an empty string into our queue
				self.queue.enqueue(next_item)
		else:
			# if the command wasnt add, try to run it from our dictionary of commands
			try:
				self.commands[command]()
			except KeyError:
			# if it ISNT in our dictionary, tell the user 
				print("Invalid command, type help for a list of commands")

	def help(self):
	# a self explanatory help method
		print("Type size to see how many ToDo-items are in your To-Do list")
		print()
		print("Type add TASK DATE (In the form Y M D)  DURATION (interpreted as Integer Hours) START_TIME (interpreted as Hours:Minutes)  PEOPLE to add a task to the queue")
		print("EXAMPLE -> add TASK 2019-09-09 1 12:12 CONOR BERNS")
		print()
		print("Type add EVENT DATE (In the form Y M D)  Start Time (Interpreted as Hours:Minutes) LOCATION to add an event to the queue")
		print("EXAMPLE -> add EVENT 2019-09-09 12:12 DUBLIN")
		print()
		print("Type del to delete the next ToDo-item off the queue once completed")
		print("Type peek to look at your next ToDo-item in the queue")
		print("Type show to print the whole queue of ToDo-Items")
		print("Type quit to exit the program")
def main():
	parser = Parser()
	parser.help()
	while True:
		parser.parse_input()

if __name__ == '__main__':
	main()
