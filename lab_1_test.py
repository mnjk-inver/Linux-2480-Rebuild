# This script will check ITC2480 Lab 1 for successful completion
# This command will import the OS library allowing linux CLI commands
import subprocess


def completion():
    print("You have completed "+str(done)+" of "+str(total)+" tasks for this lab.")
    if done == total:
        print("Congratulations you have completed all tasks for this lab")


done = 0
total = 4
# get the OS version
hostnamectl = subprocess.run("hostnamectl", capture_output=True, text=True)

# check if string exists in output
if "Operating System: Debian GNU/Linux 10 (buster)" in hostnamectl.stdout:
    print("OS is Debian Buster")
    done = done + 1
else:
    print("You have installed the wrong distribution")

# scan for open port
scan = subprocess.run("/usr/bin/nmap localhost", capture_output=True, text=True, shell=True)

# check if string exists in output
if "22/tcp    open  ssh" in scan.stdout:
    print("SSH port has been opened")
    done = done + 1
else:
    print("SSH is not functional")

# check sudo membership
username = input("enter your username: ")
sudoer = subprocess.run("getent group sudo", capture_output=True, text=True, shell=True)

# check if username is in sudoers
if username in sudoer.stdout:
    print(username+" can execute commands with sudo.")
    done = done + 1
else:
    print(username+" is not a member of sudo group.")

openvmtools_version = subprocess.run("apt list open-vm-tools", capture_output=True, text=True, shell=True)

if "open-vm-tools/stable,now 2:10.3.10-1+deb10u2 amd64 [installed]" in openvmtools_version.stdout:
    print("You have installed the latest version of VM-Tools")
    done = done + 1
else:
    print("You have not installed the latest version of VM-Tools.")

completion()
