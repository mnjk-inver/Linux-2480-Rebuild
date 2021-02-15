# This script will check ITC2480 Lab 1 for successful completion
# This command will import the OS library allowing linux CLI commands
import subprocess
from colorama import Fore
from colorama import Style

def completion():
    print("You have completed "+str(done)+" of "+str(total)+" tasks for this lab.")
    if done == total:
        print(f"{Fore.GREEN}Congratulations you have completed all tasks for this lab!{Style.RESET_ALL}")

        
done = 0
total = 4
# get the OS version
hostnamectl = subprocess.run("hostnamectl", capture_output=True, text=True)

# check if string exists in output
if "Operating System: Debian GNU/Linux 10 (buster)" in hostnamectl.stdout:
    print("OS is Debian Buster")
    done = done + 1
else:
    print(f"{Fore.RED}You have installed the wrong distribution!{Style.RESET_ALL}")

# scan for open port
scan = subprocess.run("/usr/bin/nmap localhost", capture_output=True, text=True, shell=True)

# check if string exists in output
if "22/tcp    open  ssh" in scan.stdout:
    print("SSH port has been opened")
    done = done + 1
else:
    print(f"{Fore.RED}SSH is not functional!{Style.RESET_ALL}")

# check sudo membership
username = input("enter your username: ")
sudoer = subprocess.run("getent group sudo", capture_output=True, text=True, shell=True)

# check if username is in sudoers
if username in sudoer.stdout:
    print(username+" can execute commands with sudo.")
    done = done + 1
else:
    print(f"{Fore.RED}{username} is not a member of sudo group!{Style.RESET_ALL}")

#check installed version of open-vm-tools
openvmtools_version = subprocess.run("apt list open-vm-tools", capture_output=True, text=True, shell=True)

#check if installed version is latest version as of 2/14/2021
if "open-vm-tools" and "[installed]" in openvmtools_version.stdout:
    print("You have installed the latest version of VM-Tools")
    done = done + 1
else:
    print("You have not installed the latest version of VM-Tools.")

completion()
