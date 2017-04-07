""" Sets up all the pins for the clock """
__author__ = "David Ordemann"
__date__ = "January 2015"



import RPi.GPIO as GPIO



'''

assigning variables to the gpio pins for lights...

'''

GPIO.setmode(GPIO.BOARD)  # set board mode to BOARD


# SECONDS

gpio4 = 7 #assigning gpio4 to 7

gpio17 = 11 #assigning gpio17 to 11

gpio27 = 13 #assigning gpio27 to 13

gpio22 = 15 #assigning gpio22 to 15


gpio18 = 12 #assigning gpio18 to 12

gpio23 = 16 #assigning gpio23 to 16

gpio24 = 18 #assigning gpio24 to 18




# MINUTES

gpio25 = 22 #assigning gpio25 to 22

gpio5 = 29 #assigning gpio5 to 29

gpio6 = 31 #assigning gpio6 to 31

gpio12 = 32 #assigning gpio12 to 32


gpio16 = 36 #assigning gpio16 to 36

gpio20 = 38 #assigning gpio20 to 38

gpio21 = 40 #assigning gpio21 to 40



# HOURS

gpioMISO = 21 #assigning gpioMISO to 21

gpio13 = 33 # assigning gpio13 to 33

gpio19 = 35 #assigning gpio19 to 35

gpio26 = 37 #assigning gpio26 to 37


gpioCE0 = 24 #assigning gpioCE0 to 24




# AM or PM

gpioCE1 = 26 #assigning gpioCE1 to 26






'''

setting up the GPIO pins for lights...

'''

# SECONDS

GPIO.setup(gpio22, GPIO.OUT)  # set up gpio22

GPIO.setup(gpio27, GPIO.OUT)  # set up gpio27

GPIO.setup(gpio17, GPIO.OUT)  # set up gpio17

GPIO.setup(gpio4, GPIO.OUT)  # set up gpio4


GPIO.setup(gpio24, GPIO.OUT)  # set up gpio24

GPIO.setup(gpio23, GPIO.OUT)  # set up gpio23

GPIO.setup(gpio18, GPIO.OUT)  # set up gpio18




#MINUTES

GPIO.setup(gpio25, GPIO.OUT)  # set up gpio25

GPIO.setup(gpio5, GPIO.OUT)  # set up gpio5

GPIO.setup(gpio6, GPIO.OUT)  # set up gpio6

GPIO.setup(gpio12, GPIO.OUT)  # set up gpio12


GPIO.setup(gpio16, GPIO.OUT)  # set up gpio16

GPIO.setup(gpio20, GPIO.OUT)  # set up gpio20

GPIO.setup(gpio21, GPIO.OUT)  # set up gpio21




# HOURS

GPIO.setup(gpioMISO, GPIO.OUT)  # set up gpioMISO

GPIO.setup(gpio13, GPIO.OUT)  # set up gpio13

GPIO.setup(gpio19, GPIO.OUT)  # set up gpio19

GPIO.setup(gpio26, GPIO.OUT)  # set up gpio26


GPIO.setup(gpioCE0, GPIO.OUT)  # set up gpioCE0




# AM or PM

GPIO.setup(gpioCE1, GPIO.OUT)  #set up gpioCE1


















