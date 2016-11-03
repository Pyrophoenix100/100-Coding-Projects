import os
import sys
import time
sys.path.append(os.path.abspath(".."))
import projectmodule
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
projectmodule.printheader("Counting Vowels", 3, "11/1/2016", "11/2/2016", "This program counts the vowels in whatever you type in.")
base = input("> ")
numvowels = 0
consonantarray = []
numconsanants = 0 
consonants = ""
for x in base:
	if x in vowels:
		numvowels += 1
	elif x not in "=_+\][';/@#$%^&*()`~<>:{}|":	
		numconsanants += 1
		consonantarray.append(x)
	elif x not in """1234568790 .,!?$()@#%^&*'""'""":
		print("Please stop trying to break the program.")
for y in consonantarray:
	consonants += y
print("Vowels > %d" % numvowels)
print("Consonants > %d" % numconsanants)
print("User input without consonants > %s" % consonants)
EOF = input("Press enter to continue...")