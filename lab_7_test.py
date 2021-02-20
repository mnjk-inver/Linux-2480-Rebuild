#!/usr/bin/env python3
# This script will check ITC2480 Lab 7 for successful completion
# Import OS Library
import os.path
from os import path

print()

def completion():
    print()
    print("You have completed "+str(done)+" of "+str(total)+" tasks for this lab.")
    if done == total:
        print("Congratulations you have completed all tasks for this lab.")
    print()

done = 0
total = 4

# Define directories to check
grp = os.path.expanduser("/srv/Group-Share")
gst = os.path.expanduser("/srv/Guest-Files")

# Check to see if Group Share exists
if os.path.exists(grp):
	print("1. The Group Share exists.")
	done = done + 1
	if oct(os.stat(grp).st_mode & 0o777) == "0o777":
		print("2. The Group Share has correct permissions.")
		done = done + 1
	else:
		print("2. The Group Share has inccorrect permissions.")
else:
	print("1. Try again. the Group Share was not created correctly.")
	print("2. Could not check permissions on Group Share.")

# Check to see if Guest Share exists
if os.path.exists(gst):
	print("3. The Guest Share exists.")
	done = done + 1
	if oct(os.stat(gst).st_mode & 0o777) == "0o755":
		print("4. The Guest Share has correct permissions.")
		done = done + 1
	else:
		print("4. The Guest Share has incorrect permissions.")
else:
	print("3. Try again. The Guest Share was not created correctly.")
	print("4. Could not check permissions on Guest Share.")

completion()
