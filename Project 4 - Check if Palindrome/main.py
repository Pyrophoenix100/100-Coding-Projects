import time
import sys
import os
sys.path.append(os.path.abspath(".."))
import projectmodule
projectmodule.printheader("Check if Palindrome", 4, "11/8/2016", "11/8/2016", "Checks if the input is a palindrome")
base = input("> ")
noSpace = base.replace(" ", "")
allLower = noSpace.lower()
if (allLower == allLower[::-1]) :
	print("'%s' is a palindrome" % base)
else :
	print("'%s' is not a palindrome" % base)
time.sleep(3)
