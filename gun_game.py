import utime
import myutil
import led_communication
from microbit import *

def calibrate_compass():
	microbit.compass.calibrate()


def main(mytime):
	# manage compass calibration
	iscal = microbit.compass.is_calibrated()
	if !iscal:
		# message to calibrate
		calibrate_compass()

	# led countdown to start
	mystart = utime.time()
	ctr = 0
	initialarray = []
	while mystop < (mystart + mytime):
	# Read data to list
		xyz = accelerometer.get_values()
		x = xyz(0)
		y = xyz(1)
		z = xyz(2)

		myheading = microbit.compass.heading()

		gesture = accelerometer.current_gesture()

		initialarray.extend((x,y,z,myheading,gesture))

		utime.sleep(0.2)
		mystop = utime.time()
		ctr = ctr + 1

	# Convert list to two dimensions
	numrows = ctr - 1
	masterarray = util.one_to_twod_array(initialarray,numrows,5)
	return masterarray
