import os
import sys
import time
sys.path.append(os.path.abspath(".."))
import projectmodule
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
projectmodule.printheader("Counting Vowels", 3, "11/1/2016", "11/2/2016", "This program counts the vowels in whatever you type in.")
base = input()
numvowels = 0
numconsanants = 0 
for x in base:
	if x in vowels:
		numvowels += 1
	elif x not in "1234567890 -=_+\][';/.,!@#$%^&*()`~<>?:{}|":	
		numconsanants += 1
	elif x not in """1234568790 .,!?$()@#%^&*'""'""":
		print("Please stop trying to break the program.")
print("Vowels = %d" % numvowels)
print("Consonants = %d" % numconsanants)
time.sleep(5)