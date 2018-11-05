import random
import subprocess
import time
import RPi.GPIO as GPIO
from os import listdir

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

path = "/home/pi/Music/"

# Making an array for the titles
numbers = listdir(path)

# Checking lenght of array, so the it doesn't pick a non excisting number.
length = len(numbers)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
        kill_process = ["/usr/bin/killall", "vlc"]
        subprocess.Popen(kill_process)

        time.sleep(.1)

        # Picking a song
        selected = random.randint(0, length)

        # Combining the strings for the program
        final_path = path + numbers[selected]

        program = ["/usr/bin/vlc", final_path]
        subprocess.Popen(program)

        print len(numbers)
        print final_path
        time.sleep(0.2)
