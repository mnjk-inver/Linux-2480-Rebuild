#!/usr/bin/env python3
# This script will check ITC2480 Lab 2 for successful completion

# Import OS Library
import os.path
from os import path

# Define directories and tar file to check
dir1 = os.path.expanduser("~/sample-files/Shakespeare")
dir2 = os.path.expanduser("~/sample-files")
tar = os.path.expanduser("~/sample-files/shakespeare.tar.gz")

# Check to see if Shakespeare directory exists
if os.path.exists(dir1):
	print("Try again. The ~/sample-files/Shakespeare directory should have been deleted.")
else:
	print("Congratulations! The ~/sample-files/Shakespeare directory was deleted.")

# Check to see if sample-files directory exists
if os.path.exists(dir2):
	print("Congratulations! The ~/sample-files directory exists.")
else:
	print("Try again. The ~/sample-files directory does not exist.")

# Check to see if shakespeare.tar.gz exists
if os.path.exists(tar):
	print("Congratulations! The ~/sample-files/shakespeare.tar.gz file exists.")
else:
	print("Try again. The ~/sample-files/shakespeare.tar.gz file does not exist.")

# Check to see if Apache is installed correctly
print("Open a browser on your host computer. Type in your server IP address and hit enter.")

def prompt():
	answer = input("Did either the Apache default page or your personal webpage appear? [Y / N]: ").lower()
	if answer == "y":
		print("Congratulations! You installed Apache correctly.")
	elif answer == "n":
		print("Try again. You did not install Apache correctly.")
	else:
		print("You did not choose Y or N")
		prompt()

prompt()
