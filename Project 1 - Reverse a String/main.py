import time
import sys
time.sleep(1)
print(sys.path)
time.sleep(1)
sys.path.append('\..')
print(sys.path)
time.sleep(1)

sys.stdout.write("> ")
inputs = input()
print(inputs[::-1])
time.sleep(2)