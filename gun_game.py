import speech
import utime
import math
from microbit import *

##############################################################################
#This section will contain utility related functions
def write_file(myfile, contents):
	with open(myfile, 'w') as my_file:
        my_file.write(contents)

def read_file(myfile):
	with open(myfile) as my_file:
	    content = my_file.read()
	return content

def append_file(targetfile, myinput):
	file_contents = read_file(targetfile)
	file_contents = file_contents + myinput
	write_file(targetfile, file_contents)

# Convert 1d array to 2d array
def one_to_twod_array(initialarray, numcols, numrows):
	colctr = 0
	rowctr = 0
	actr = 0
	masterctr = 0

	# Create a list.
	masterarray = []

	# Append empty lists for the number of rows
	while actr < numrows:
		masterarray.append([])
		actr = actr + 1

	# Iterate number of rows and columns provided in args
	while rowctr < numrows:
		while colctr < numcols:
			item = initialarray[masterctr]
			# Now on each iteration, we append to each row
			masterarray[rowctr].append(item)
			colctr = colctr + 1
			masterctr = masterctr + 1
		colctr = 0
		rowctr = rowctr + 1
	return masterarray

def avg_vals_twod_array(myarray,colnum):
	mysum = 0
	ctr = 0
	while ctr < len(myarray):
		mysum = mysum + myarray[ctr][colnum]
		ctr = ctr + 1
	myavg = mysum/ctr
	return myavg

def max_val_twod_array(myarray,colnum):
	mymax = 0
	ctr = 0
	while ctr < len(myarray):
		if myarray[ctr][colnum] > mymax:
			mymax = myarra[ctr][colnum]
		ctr = ctr + 1
	return mymax

def max_dev_twod_array(myarray,colnum,avg):
	maxnum = 0
	maxdev = 0
	ctr = 0
	while ctr < len(myarray):
		if (math.fabs(myarray[ctr][colnum]-avg) > maxdev:
			maxnum = myarray[ctr][colnum]
			maxdev = math.fabs(myarray[ctr][colnum]-avg)
		ctr = ctr + 1
return maxdev, maxnum
############################################################################
#This section contains button actions

def wait_for_a_btn():
    while True:
        if button_a.is_pressed():
            break

##################################################

############################################################################
#This section contains speech related functions

def stat_drift_speech(direction):
    if direction != "perfect":
        speech.say("You drifted a little to the")
        speech.say(direction)
    else:
        speech.say("No drift! that was perfect")

def game_welcome_speech():
    speech.say("Welcome to the gun training game.  Please press A to continue")

def game_countdown_speech():
    speech.say("The game will begin in")
    x=0
    countdown = ["three","two","one","starting now"]
    while x < len(countdown):
        speech.say(countdown[x])
        sleep(1000)
        x = x + 1
        
def success_or_fail_speech(mybool):
    if mybool:
        speech.say("Great success")
    else:
        speech.say("Please try again")
################################################

##############################################################################
#This section contains display related functions

################################################

##############################################################################
#This section contains accelerometer related functions
def acc_get_accelerometer_data():
    myreturn = accelerometer.get_values()
    return myreturn
###############################################

##############################################################################
#This section contains compass related functions

#Calibrate the compass
def calibrate_compass():
    compass.calibrate()
    myreturn = microbit.compass.is_calibrated()
    return myreturn
        

# retrieve compass data as 0-360
def get_compass_data():
    

################################################

##############################################################################
#This section will have meaningful containers for low level functions i.e. anything above this line

#Container to translate data to twod array
def translate_data(mydata):
    #interestlist("xavgdev","yavgdev","zavgdev","compassavgdev")
    numreturns = 4
    myreturnlist = []
    numcols = 4
    #convert to twod array
    numrows = mydata/numcols
    mapped = one_to_twod_array(mydata,numcols,numrows)
    ctr = 0
    while ctr < numreturns:
        tempavg = avg_vals_twod_array(mapped,ctr)
        myreturnlist[ctr] = tempavg
        ctr = ctr + 1
    return myreturnlist
    

#Container to house information gathering that occurs during gameplay
def gameplay_container():
    roundarray = []
    starttime = utime.time()
    currenttime = starttime
    timespent = 0
    while timespent < 30:
        accdata = get_accelerometer_data()
        compdata = get_compass_data()
        roundarray.append(accdata)
        roundarray.append(compdata)
        currenttime = utime.time()
        sleep(500)
        timespent = currenttime - starttime
    return roundarray
################################################

##################################################################################
#This section contains our main container
def main():
    game_welcome_speech()
    wait_for_a_btn()
    game_countdown_speech()
    roundarray = gameplay_container()
    mytranslation = translate_data(roundarray)
    myanalysis = analysis_for_summary(mytranslation)
    gamesummary_container(myanalysis)
####################################################################################
#Kick off the microbit!
main()
        
