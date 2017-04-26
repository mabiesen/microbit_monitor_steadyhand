import math

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
