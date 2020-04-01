#in this there is security system named travis which use list data structure to check if the person is present in the list and authorized to enter otherwise it'll request you to be added

known_users = ["Alice", "Bob", "Dan", "Emma"]

#print(len(known_users))

while True:
	print("Hi! My name is Travis")
	name = input("What is your name?: ").strip().capitalize() #.strip and .captialize is used to avoid if user enter small letter and machine donot understant it

	if name in known_users:#in is used to check if name of user is present in the system
	   print("Hello {}!".format(name))
	   remove = input("Would you like to be removed from the system (y/n)?: ") 

	   if remove == "y" or remove == "Y":
	   	known_users.remove(name)
	   elif remove == "n" or remove == "N":
	   	print("I have no problem!")


	else:
		print("Hmmmm I don't think I have met you yet {}".format(name))
		add_me = input("Would you like to be added to system (y/n)?: ").strip().capitalize()
		if add_me == 'y' or add_me == 'Y':
			known_users.append(name)
		elif add_me == "n" or add_me == "N":
			print("No worries, see you around")


