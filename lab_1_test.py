# This script will check ITC2480 Lab 1 for successful completion
# This command will import the OS library allowing linux CLI commands
import subprocess

# get the OS version
hostnamectl = subprocess.run("hostnamectl", capture_output=True, text=True)

# check if string exists in output
if "Operating System: Debian GNU/Linux 10 (buster)" in hostnamectl.stdout:
    print("OS is Debian Buster")
else:
    print("You have installed the wrong distribution")

# scan for open port
scan = subprocess.run("/usr/bin/nmap localhost", capture_output=True, text=True, shell=True)

# check if string exists in output
if "22/tcp    open  ssh" in scan.stdout:
    print("SSH port has been opened")
else:
    print("SSH is not functional")

# check sudo membership
username = input("enter your username: ")
sudoer = subprocess.run("getent group sudo", capture_output=True, text=True, shell=True)

# check if username is in sudoers
if username in sudoer.stdout:
    print(username+" can execute commands with sudo.")
else:
    print(username+" is not a member of sudo group.")
