""" Main program to run the binary clock """
__author__ = "David Ordemann / Paige Meyer"
__date__ = "January 2015"



from clockFunctions import *
from clockLightSetup import *



'''
Sets base values for comparison in the while loop if statements
'''

tmpSec1 = datetime.datetime.now().second
tmpMin1 = datetime.datetime.now().minute
tmpHr1 = datetime.datetime.now().hour

'''
Used to keep track of loop iterations for minutes and hours
'''

ctMinutes = 0
ctHours = 0


while True:

    '''
    Sets a second value to compare to the previously set base values
    '''
    
    tmpSec2 = datetime.datetime.now().second
    tmpMin2 = datetime.datetime.now().minute
    tmpHr2 = datetime.datetime.now().hour

    '''
    Selection statement that uses functions to light the proper
    LED lights given the seconds ones and tens place.
    The code block in the selection statement only executes when the
    seconds value changes.
    '''
    
    if tmpSec1 != tmpSec2:
        print("seconds:", tmpSec1) # prints seconds to terminal for testing
        lightSecondsOnes(str(getSecondsOnesPlace()))
        lightSecondsTens(str(getSecondsTensPlace()))
        tmpSec1 = tmpSec2

    '''
    Selection statements to show minutes immediately and when the minutes change
    '''

    if ctMinutes == 0:
	lightMinutesOnes(str(getMinutesOnesPlace()))
	lightMinutesTens(str(getMinutesTensPlace()))
	ctMinutes += 1

    if tmpMin1 != tmpMin2:
        print("minutes:", tmpMin1) # prints minutes to terminal for testing
	lightMinutesOnes(str(getMinutesOnesPlace()))
	lightMinutesTens(str(getMinutesTensPlace()))
	tmpMin1 = tmpMin2

    '''
    Selection statements to show hours immediately and when the hours change
    '''

    if ctHours == 0:
	lightHoursOnes(str(getHoursOnesPlace()))
	lightHoursTens(str(getHoursTensPlace()))
	ctHours += 1

    if tmpHr1 != tmpHr2:
        print("hours:", tmpHr1) # prints hours to terminal for testing
	lightHoursOnes(str(getHoursOnesPlace()))
	lightHoursTens(str(getHoursTensPlace()))
	lightAMorPM(getAMorPM())
	tmpHr1 = tmpHr2

