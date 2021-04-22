#!/usr/bin/env python3
import os.path, subprocess

# Check for files and get boolean
list_file = os.path.isfile("listfiles.txt")
log_file = os.path.isfile("gzlogfiles.txt")
done = 0

# Completion of lab check and output
def completion():
    print("You have completed", str(done), "out of 5 tasks for this lab!")
    if done == 5:
        print("Congratulations you have completed all tasks for this lab.")

# Check for directories and assign them a variable
dir1 = os.path.expanduser("~/documentation")
dir2 = os.path.expanduser("~/experiments")
read_html = os.path.expanduser("/var/www/html/index.html")
locate_installed = subprocess.run("dpkg -s locate", capture_output=True, text=True, shell=True)
print("-" * 45)

# Check if the directories where found and print output
if os.path.exists(dir1):
    print("Good work the directory ~/documentation was created.")
    done = done + 1
else:
    print("Make sure to create the ~/documentation directory!")

if os.path.exists(dir2):
    print("Good work the ~/experiments directory exists.")
    done = done + 1
else:
    print("Make sure to create the ~/experiments directory!")

if os.path.exists(read_html):
    print("Good work the /var/www/html/index.html file exists.")
    done = done + 1
else:
    print("Make sure to have the index.html made and readable!")

if "Status: install ok installed" in locate_installed.stdout:
    done = done + 1
    print("Good work locate app was installed.")
else:
    print("Make sure to install locate!")

# Check if both the files exist then print output
if list_file and log_file is True:
    print("Good work both the listfiles.txt and gzlogfiles.txt exists")
    done = done + 1
else:
    print("Make sure to use the right commands to make both listfiles.txt and gzlogfiles.txt!")

print("-" * 45)
completion()
print("-" * 45)
