def enqueue(queue, next_item):
	if not queue:
		queue = ""
	# This will prevent indexing an empty queue
	queue =  queue + next_item + "&"
	# add next task to the queue	return queue
	return queue
def dequeue(queue):
	if not queue:
	# again, prevents indexing an empty queue
		print("Queue is empty")
		return
	i = 0
	while queue[i] != "&":
		i += 1
	queue = queue[i+1:]
	return queue

def size(queue):
	# len is a method of the String object in python, this function replaces the in-built length
	if not queue:
		return 0
	length = 0
	for character in queue:
		length += 1
	return length

def items(queue):
	# utility for the user to see how many items are left for them to do (very busy people )
	count = 0
	if not queue:
		print("No items left in the To-Do list")
		return
	for character in queue:
	# the string placeholder allows us very easily to determine # items
		if character == "&":
			count += 1
	print("Number of things left in the To-Do list -> " , (count))

def peek(queue):
	# allows the user to see their next To-Do item
	if not queue:
		print("Queue is empty")
		return
	i = 0
	while queue[i] != "&":
		i += 1
	print(queue[0:i])

def show(queue):
	# prints all the tasks in the Queue
	i = 0
	parsed = ""
	while i < size(queue):
		if queue[i] == "&":
		#  we  obviously dont want to print the placeholder character, this would be silly
			parsed += '\n'
		# place a new line where we see "&" as we know this is the end of a TASK/EVENT
			i += 1
			continue
		# otherwise, add the character to a string we build from the ground up 
		parsed += queue[i]
		i += 1
	if parsed:
		print(parsed[0:-1])
	else:
		print("Queue is empty")

def help():
	print("Any special characters you see in the following commands are not needed, they are merely there to highlight the command syntax eg to add hello to the queue, type add hello NOT *add [hello]*")
	print("Type *size* to see how many items are in your To-Do list")
	print("Type *add [you're desired to-do list item]* to add it to the queue")
	print("Type *del* to delete the next item off the queue once completed")
	print("Type *peek* to look at your next task in the queue")
	print("Type *show* to print the whole queue of tasks")

def run(command):
	global queue
	if command[0:3] == "add":
		queue = enqueue(queue, command[4:])
	elif command == "del":
		queue = dequeue(queue)
	elif command == "show":
		show(queue)
	elif command == "peek":
		peek(queue)
	elif command == "help":
		help()
	elif command == "size":
		items(queue)
	else:
		print("Command entered is not valid, type \"help\" for a list of accepted commands")

queue = ""
while True:
	input_ = input()
	if input_ == "quit":
		break
	run(input_)



