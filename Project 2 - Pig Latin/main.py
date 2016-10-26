import os
import sys
import time
sys.path.append(os.path.abspath(".."))
import projectmodule
projectmodule.printheader("Pig Latin", 2, "10/25/2016", "10/26/2016", "This program translates whatever you type in into pig latin.")
base = input("> ")
for x in base.split(" "):
	first = x[0:1]
	if len(x) > 1:
		sys.stdout.write(x[1::] + "-" + first + "ay ")
	else:
		sys.stdout.write(first + "ay ")
	
print("")
end = input("Press enter to continue...")