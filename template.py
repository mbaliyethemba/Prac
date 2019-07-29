#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Mbaliyethemba Shangase
Student Number: SHNMBA004
Prac: Prac1
Date: 04/08/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO

#set mode
GPIO.setmode(GPIO.BCM)

#set the buttons on pin 17 and 27
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #incremental button
GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #decremental button

#set the LED
GPIO.setup(24,GPIO.OUT)  #LED3
GPIO.setup(23,GPIO.OUT)  #LED2
GPIO.setup(22,GPIO.OUT)  #LED1

#set the LED to low
GPIO.setup(24,GPIO.LOW)  #LED3
GPIO.setup(23,GPIO.LOW)  #LED2
GPIO.setup(22,GPIO.LOW)  #LED1

counter = 0;

def button():
	global counter
	if (GPIO.input(17) == 1 and counter != 7): #counts up
		counter += 1
		print bin(counter)[2:].zfill(3)
		time.sleep(.2)
	if (GPIO.input(17) == 1 and counter == 7): #wraps around to zero
		counter = 0
		print bin(counter)[2:].zfill(3)
		time.sleep(.2)
	if (GPIO.input(27) == 1 and counter != 0): #counts down
		counter -= 1
		print bin(counter)[2:].zfill(3)
		time.sleep(.2)
	if (GPIO.input(27) == 1 and counter == 0): #wraps around back to 7
		counter = 7
		print bin(counter)[2:].zfill(3)
		time.sleep(.2)
	return

# Logic that you write
def main():
    print("write your logic here")


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
