# This will handle microbit upon turn on
import gun_game

# Two Activities: loop for button press, loop for data
# Note: MicroPython does not allow threading, shouldnt be an issue


def main():
	# Welcome the user

	# Provide option trigger or no trigger, or multi-target acquisition

	# User Press A button to start

	# Start gun tilt recording Session
	masterarray = gun_game.main(15)

	# Provide feedback



	# Can gauge:
	# smoothness of motion
	# amount of motion
	# average/max direction of motion
	# polar deviation

	# score()
	# tilt_stats()
	# old_stats()
