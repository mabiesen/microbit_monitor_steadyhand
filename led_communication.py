import utime
from microbit import *

# Countdown until game Begins
def game_start_countdown():
	mylist = ["3","2","1","GO"]
	for item in mylist:
		microbit.display.show(item, delay=400, *, wait=True, loop=False, clear=True)
		utime.sleep(0.5)

# Display visual tilt


# Display Rank as 1-5 in order of shakiness
