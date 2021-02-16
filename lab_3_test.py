#!/usr/bin/env python3
# Import the subprocess module to run commands in shell
import subprocess

# Used for telling the user what is installed and not installed at the end
directories_present = False
redteam_ours = False
redteam_redteam = False

# grab directory listing of redteam
redteam_directory = subprocess.run("ls -al /home/jsmith/redteam", capture_output=True, text=True, shell=True)

# grab appropriate values for redteam and ours
list = subprocess.run("/home/jsmith/redteam/ls -l ours", capture_output=True, text=True, shell=True)
splitlist = list.stdout.split()


# grab directory listing of jsmith
jsmith_directory = subprocess.run("/home/jsmith/ls -l redteam", capture_output=True, text=True, shell=True)
splitlist2 = jsmith_directory.stdout.split()


if "theplan" and "yours" and "mine" and "ours" in redteam_directory.stdout:
    directories_present = True
    pass
if splitlist[4] == "redteam" and splitlist[9] == "ours":
    redteam_ours = True
    pass
if splitlist[4] == 'redteam' and splitlist2[9] == "redteam":
    redteam_redteam = True
    pass


def completion():
    if directories_present and redteam_ours and redteam_redteam is True:
        print("Everything is installed correctly. Great Work!")
    if directories_present is False:
        print("Some required directories are missing")
    if redteam_ours is False:
        print("Redteam is not the owner of /home/jsmith/redteam/ours")
    if redteam_redteam is False:
        print("Redteam is not the owner of home/jsmith/redteam")

completion()
