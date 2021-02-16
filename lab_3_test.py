#!/usr/bin/env python3
# Import the subprocess module to run commands in shell
import subprocess

# Used for telling the user what is installed and not installed at the end
directories_present = False
redteam_ours = False
redteam_redteam = False
webmin = False

# grab directory listing of redteam
redteam_directory = subprocess.run("ls -al /home/jsmith/redteam", capture_output=True, text=True, shell=True)

# grab appropriate values for redteam and ours
ours = subprocess.run("stat -c %G /home/jsmith/redteam/ours", capture_output=True, text=True, shell=True)

# grab directory listing of jsmith
redteam = subprocess.run("stat -c %G /home/jsmith/redteam", capture_output=True, text=True, shell=True)

# check webmin installation and format the data
# webmin_search = subprocess.run("apt-cache policy webmin", capture_output=True, text=True, shell=True)
webmin_version = subprocess.run("apt-cache policy webmin", capture_output=True, text=True, shell=True)
webmin_installed = webmin_version.stdout.splitlines()[1]
webmin_latest = webmin_version.stdout.splitlines()[2]
webmin_installed = webmin_installed.split()[1]
webmin_latest = webmin_latest.split()[1]

#check completion of tasks
if "theplan" and "yours" and "mine" and "ours" in redteam_directory.stdout:
    print("All directories successfully created!")
    directories_present = True
    pass
if ours.stdout.strip() == "redteam":
    print("redteam owns /home/jsmith/redteam/ours")
    redteam_ours = True
    pass
if redteam.stdout.strip() == 'redteam':
    print("redteam owns /home/jsmith/redteam")
    redteam_redteam = True
    pass
if webmin_latest == webmin_installed:
    print("You have installed the latest version of Webmin")
    webmin = True
    pass

#give complete not complete results
def completion():
    if directories_present and redteam_ours and redteam_redteam and webmin is True:
        print("Everything is installed correctly. Great Work!")
    if directories_present is False:
        print("Some required directories are missing.")
    if redteam_ours is False:
        print("redteam is not the owner of /home/jsmith/redteam/ours.")
    if redteam_redteam is False:
        print("redteam is not the owner of /home/jsmith/redteam.")
    if webmin is False:
        print("The latest version of Webmin is not installed correctly.")

completion()
