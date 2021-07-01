#%%
# python.exe xxxx.py

 # Raspberry PI: single board computer with cheap price.

import RPi.GPIO as GPIO 		# Python module RPi.GPIO to work with the Raspberry PI
								# $ sudo apt-get install python-dev python-rpi.gpio

# write output on the Raspberry Pi’s GPIO bus:
GPIO.setmode(GPIO.BOARD)
GPIO.setup(1, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(1, GPIO.HIGH)


# Reading from the Raspberry Pi’s GPIO
GPIO.setup(1, GPIO.IN)
if GPIO.input(1):
    print('Input was HIGH')
else:
    print('Input was LOW')
