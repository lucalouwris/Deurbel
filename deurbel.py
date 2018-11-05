import random
import subprocess
import time
from os import listdir

path = "/home/pi/Music/"

# Making an array for the titles
numbers = listdir(path)

# Checking lenght of array, so the it doesn't pick a non excisting number.
length = len(numbers)

# Picking a song
selected = random.randint(0, length)

# Combining the strings for the program
final_path = path + numbers[selected]

kill_process = ["/usr/bin/killall", "vlc"]
subprocess.Popen(kill_process)

time.sleep(.1)

program = ["/usr/bin/vlc", final_path]
subprocess.Popen(program)

print len(numbers)
print final_path
