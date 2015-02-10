""" Contains all of the functions used in the Main program to run the clock """
__author__ = "David Ordemann / Paige Meyer"
__date__ = "January 2015"



from clockLightSetup import *
from time import strftime
import RPi.GPIO as GPIO
import datetime



def getSecondsOnesPlace():

    '''
    Description: Returns the value in the ones place for the currect second
                 on the computers clock
    '''
    
    if len(str(datetime.datetime.now().second)) == 1:
        return dec_to_bin(datetime.datetime.now().second)
            
    else:
        tmpStr = str(datetime.datetime.now().second)[1]
        return dec_to_bin(int(tmpStr))




def getSecondsTensPlace():

    '''
    Description: Returns the value in the tens place for the currect second
                 on the computers clock
    '''
    
    if len(str(datetime.datetime.now().second)) == 1:
        return dec_to_bin(0)
    
    else:
        tmpStr = str(datetime.datetime.now().second)[0]
        return dec_to_bin(int(tmpStr))




def getMinutesOnesPlace():

    '''
    Description: Returns the value in the ones place for the currect minute
                 on the computers clock
    '''
    
    if len(str(datetime.datetime.now().minute)) == 1:
        return dec_to_bin(datetime.datetime.now().minute)
            
    else:
        tmpStr = str(datetime.datetime.now().minute)[1]
        return dec_to_bin(int(tmpStr))




def getMinutesTensPlace():

    '''
    Description: Returns the value in the tens place for the currect minute
                 on the computers clock
    '''
    
    if len(str(datetime.datetime.now().minute)) == 1:
        return dec_to_bin(0)
            
    else:
        tmpStr = str(datetime.datetime.now().minute)[0]
        return dec_to_bin(int(tmpStr))




def getHoursOnesPlace():

    '''
    Description: Returns the value in the ones place for the currect hour
                 on the computers clock, compensates for military time
    '''

    if datetime.datetime.now().hour < 1:
	return dec_to_bin(2)	# Ones place for hour 12

    elif len(str(datetime.datetime.now().hour)) == 1:
        return dec_to_bin(datetime.datetime.now().hour)

    elif datetime.datetime.now().hour > 12 and datetime.datetime.now().hour < 22:
	convert = datetime.datetime.now().hour
	convert = convert - 12
	return dec_to_bin(convert)

    elif datetime.datetime.now().hour > 21:
	doubleDigitOne = str(datetime.datetime.now().hour)[1]
	doubleDigitOne = int(doubleDigitOne) - 2
	return dec_to_bin(doubleDigitOne)
            
    else:
        tmpStr = str(datetime.datetime.now().hour)[1]
        return dec_to_bin(int(tmpStr))




def getHoursTensPlace():

    '''
    Description: Returns the value in the tens place for the currect hour
                 on the computers clock
    '''

    if datetime.datetime.now().hour < 1:
	return dec_to_bin(1)	# Tens place for hour 12

    elif len(str(datetime.datetime.now().hour)) == 1:
        return dec_to_bin(0)

    elif datetime.datetime.now().hour > 12 and datetime.datetime.now().hour < 22:
	return dec_to_bin(0)

    elif datetime.datetime.now().hour > 21:
	return dec_to_bin(1)
            
    else:
        tmpStr = str(datetime.datetime.now().hour)[0]
        return dec_to_bin(int(tmpStr))

    


def getAMorPM():

    '''
    Description: Returns the string AM or PM depending on if it is morning or night
    '''

    morningOrNight = datetime.datetime.now()
    morningOrNight = strftime("%p")
    return morningOrNight




def dec_to_bin(x):

    '''
    Description: Converts the given decimal value to a 4 bit binary number.
    Pre-Conditions: The parameter must be between 0 and 15.
    '''
    
    tmpBin = int(bin(x)[2:])
    
    if len(str(tmpBin)) == 1:
        tmpBin = "000" + str(tmpBin)
        return tmpBin
    
    elif len(str(tmpBin)) == 2:
        tmpBin = "00" + str(tmpBin)
        return tmpBin
    
    elif len(str(tmpBin)) == 3:
        tmpBin = "0" + str(tmpBin)
        return tmpBin
    
    else:
        return tmpBin



'''

lights the four LEDs for the ones in the seconds....

'''

def lightSecondsOnes(binString):

    GPIO.output(gpio22, int(binString[0]))  # turn on/off gpio22

    GPIO.output(gpio27, int(binString[1]))  # turn on/off gpio27

    GPIO.output(gpio17, int(binString[2]))  # turn on/off gipo17

    GPIO.output(gpio4, int(binString[3]))  # turn on/off gipo4





'''

lights the three LEDs for the tens in the seconds....

'''

def lightSecondsTens(binString):

    binString = binString[1:4]

    GPIO.output(gpio24, int(binString[0]))  # turn on/off gpio24

    GPIO.output(gpio23, int(binString[1]))  # turn on/off gpio23

    GPIO.output(gpio18, int(binString[2]))  # turn on/off gpio18





'''

lights the four LEDs for the ones in the minutes....

'''

def lightMinutesOnes(binString):

    GPIO.output(gpio12, int(binString[0]))  # turn on/off gpio12

    GPIO.output(gpio6, int(binString[1]))  # turn on/off gpio6

    GPIO.output(gpio5, int(binString[2]))  # turn on/off gipo5

    GPIO.output(gpio25, int(binString[3]))  # turn on/off gipo25





'''

lights the three LEDs for the tens in the minutes....

'''

def lightMinutesTens(binString):

    binString = binString[1:4]

    GPIO.output(gpio21, int(binString[0]))  # turn on/off gpio21

    GPIO.output(gpio20, int(binString[1]))  # turn on/off gpio20

    GPIO.output(gpio16, int(binString[2]))  # turn on/off gpio16





'''

lights the four LEDs for the ones in the hours....

'''

def lightHoursOnes(binString):

    GPIO.output(gpio26, int(binString[0]))  # turn on/off gpio26

    GPIO.output(gpio19, int(binString[1]))  # turn on/off gpio19

    GPIO.output(gpio13, int(binString[2]))  # turn on/off gipo13

    GPIO.output(gpioMISO, int(binString[3]))  # turn on/off gipoMISO




'''

lights the three LEDs for the tens in the hours....

'''

def lightHoursTens(binString):

    binString = binString[3]

    GPIO.output(gpioCE0, int(binString[0]))  # turn on/off gpio20




'''

lights AM or PM light....

'''

def lightAMorPM(string):
    
    if string == "AM":
	GPIO.output(gpioCE1, 0)  # turn off gpioCE1 when morning

    elif string == "PM":
	GPIO.output(gpioCE1, 1)  # turn on gpioCE1 when afternoon / evening


    
