#!/usr/bin/env python3
# This script will check ITC2480 Lab 2 for successful completion
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

# Define directories and tar file to check
dir1 = os.path.expanduser("~/sample-files/Shakespeare")
dir2 = os.path.expanduser("~/sample-files")
tar = os.path.expanduser("~/sample-files/shakespeare.tar.gz")

# Check to see if Apache is installed correctly
print("Open a browser on your host computer. Type in your server IP address and hit enter.")

def prompt1():
	global done
	answer = input("Did either the Apache default page or your personal webpage appear? [Y / N]: ").lower()
	if answer == "y":
		print("1. Apache was installed correctly.")
		done = done + 1
	elif answer == "n":
		print("1. Try again. You did not install Apache correctly.")
	else:
		print("You did not choose Y or N.")
		prompt1()

prompt1()

# Check to see if Shakespeare directory exists
if os.path.exists(dir1):
	print("2. Try again. The ~/sample-files/Shakespeare directory should have been deleted.")
else:
	print("2. The ~/sample-files/Shakespeare directory was successfully deleted.")
	done = done + 1

# Check to see if sample-files directory exists
if os.path.exists(dir2):
	print("3. The ~/sample-files directory exists.")
	done = done + 1
else:
	print("3. Try again. The ~/sample-files directory does not exist.")

# Check to see if shakespeare.tar.gz exists
if os.path.exists(tar):
	print("4. The ~/sample-files/shakespeare.tar.gz file exists.")
	done = done + 1
else:
	print("4. The ~/sample-files/shakespeare.tar.gz file does not exist.")

completion()
