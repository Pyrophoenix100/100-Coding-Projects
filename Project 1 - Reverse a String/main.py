import time
import sys
import os
sys.path.append(os.path.abspath(".."))
import projectmodule
projectmodule.printheader("Reverse a string", 1, "10/25/2016", "10/25/2016", "This program reverses whatever you type in.")
sys.stdout.write("> ")
inputs = input()
print(inputs[::-1])
empty = input("Press enter to continue...")