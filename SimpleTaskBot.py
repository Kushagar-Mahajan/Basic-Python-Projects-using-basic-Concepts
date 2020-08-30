import os
import pyttsx3 as tts #library to make our system speak


tts.speak("Hi, Welcome to our system") #speak function for our system
tts.speak("Please Enter what can I do for you?")
while True:
	p = input("")
	p = p.lower() #lower down all the character entered by the user

	if ("run" in p) or ("open" in p) or ("find" in p) or ("execute" in p):
		if ("firefox" in p):
			tts.speak("Opening firefox for you")
			os.system("firefox")
			tts.speak("Do you want any other help from me?")
		elif ("editor" in p) or ("notepad" in p) or ("gedit" in p):
			tts.speak("Opening editor for you")
			os.system("subl")
			tts.speak("Do you want any other help from me?")
		elif ("excel" in p) or ("sheets" in p):
			tts.speak("Opening sheets for you")
			os.system("libreoffice --calc")
			tts.speak("Do you want any other help from me?")
		elif ("powerpoint" in p) or ("slides" in p):
			tts.speak("Opening slides for you")
			os.system("libreoffice --impress")
			tts.speak("Do you want any other help from me?")
		elif ("draw" in p) or ("paint" in p):
			tts.speak("Opening paint for you")
			os.system("libreoffice --draw")
			tts.speak("Do you want any other help from me?")
		elif ("writer" in p) or ("word" in p):
			tts.speak("Opening word for you")
			os.system("libreoffice --word")
			tts.speak("Do you want any other help from me?")
		else:
			tts.speak("Sorry, I don't understand what you are saying. Do, you want me to search for it?")
			tts.speak("Enter Y if you want to search it on Google, or else enter N as input.")
			ch = input()
			if ch == "y":
				tts.speak("Opening google in firefox you can perform your search in it.")
				os.system("firefox "+p)
			elif ch == "n":
				tts.speak("Do you want any other help from me?")


	elif ("no" in p):
		tts.speak("Would you like me to hold and wait for next instruction or should I exit?")
	if("hold" in p) or ("yes" in p):
		tts.speak("Ok, I am waiting for the next instruction")
	elif("done" in p):
		tts.speak("Thankyou for using me.")
		break