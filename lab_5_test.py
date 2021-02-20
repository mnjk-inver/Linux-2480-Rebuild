# this is a start
print("hello world!")
# This script will check ITC2480 Lab 5 for successful completion
# This command will import the OS library allowing linux CLI commands
import subprocess
import os

def completion():
    print()
    print("You have completed "+str(done)+" of "+str(total)+" tasks for this lab.")
    if done == total:
        print("Congratulations you have completed all tasks for this lab")
    print()

done = 0
total = 4
#get assigned ip address
StudentIP = input("Please enter your assigned IP address: ")
print(StudentIP)
#Check if ip address responds to icmp requests ping"

import os
hostname = "172.17.50.6"
response = os.system("ping -c 1 " + hostname)
if response == 0
    pingstatus = "Network Active"
else:
    pingstatus = "Network Error"

#check to see if PHP, MySQL, MariaDB packages are installed and latest version
#Request information from index.html file to verify custom link page
#database checking ideas
#check for tail redirection file


#check if installed package versions is latest version as of 2/19/2021

#if "php" and "[installed]" in php.stdout:
#    print("You have installed the latest version of PHP")
#    done = done + 1
#else:
#    print("You have not installed the latest version of PHP.")
#
#completion()
