#!/usr/bin/env python3
'''
This is a work in progress! A lot of the code can be improved and revised.
It will definitly change so its not adviced to used this in your own scripts until it is finalized!
Still need to make it append outputs to a file but will do that at the end.
'''
# Import modules used for this script
import subprocess

# Assign Success and Warning for outputs (color coded)
Success = '\x1b[6;30;42m' + 'Success!' + '\x1b[0m'
Warning = '\x1b[5;30;41m' + 'Warning!' + '\x1b[0m'

# Get the user name and system id (Can be improved. Just a working example!)
STUUSER = "examuser"
STUVMID = input("Enter System ID:")

# Get ip address
IPfull = subprocess.run("ip address show", capture_output=True, text=True, shell=True)
IP = IPfull.stdout[IPfull.stdout.find("inet 172.17.50.") +15: IPfull.stdout.find("/24")]
ipadd = "172.17.50."+IP

blog_url = f"http://{ipadd}/blog"

# Define aptcheck for checking installed programs
def aptcheck(installed, command, name):
    if installed in command.stdout:
        print(Success + f"{name} is installed")
    else:
        print(Warning + f"{name} is NOT installed!")

# Define 'cat' command for repeated command usage 
def catcommand(command):
    output = subprocess.run(f"cat {command}", capture_output=True, text=True, shell=True)
    print(output.stdout)

# Define 'ls -l' command for repeated command usage (May be able to merge with catcommand?)
def lscommand(command):
    output = subprocess.run(f"ls -l {command}", capture_output=True, text=True, shell=True)
    print(output.stdout)

# Define 'ls -al' command for repeated command usage
def lsalcommand(command):
    output = subprocess.run(f"ls -al {command}", capture_output=True, text=True, shell=True)
    output2 = subprocess.run(f"ls -al {command} | cat -n | head", capture_output=True, text=True, shell=True)
    output3 = subprocess.run(f"ls -al {command} | cat -n | tail", capture_output=True, text=True, shell=True)
    print(output.stdout, output2.stdout, output3.stdout)

# Checking installed programs (Going to add 'subprocess.run' to the definition later!)
aptcheck("installed", subprocess.run("apt list locate", capture_output=True, text=True, shell=True), "locate")
aptcheck("installed", subprocess.run("apt list curl", capture_output=True, text=True, shell=True), "curl")
aptcheck("installed", subprocess.run("apt list dnsutils", capture_output=True, text=True, shell=True), "dnsutils")
aptcheck("installed", subprocess.run("apt list python3", capture_output=True, text=True, shell=True), "python3")
aptcheck("installed", subprocess.run("apt list python3-requests", capture_output=True, text=True, shell=True), "python3-requests")

# Checking hostname, sudoers, students, and user id's
catcommand("/etc/passwd | grep linuxgeek")
catcommand("/etc/hostname")
catcommand("/etc/group | grep sudo")
catcommand("/etc/group | grep students")

# Checking if host user has sudo permissions (Can be improved. Just a working example!)
is_sudo = subprocess.run("groups " + STUUSER, capture_output=True, text=True, shell=True)
if "sudo" in is_sudo.stdout:
    print("User is sudo")
else:
    print("not sudo")


# Print out files and there content from the locate command output (Works to fast and breaks. May need to be timed!)
# Could add as a child definition to the "catcommand" definition
Files = subprocess.run("locate recent-log", capture_output=True, text=True, shell=True)
for i in Files.stdout.splitlines():
    print(i + " Contents:")
    content = subprocess.run(f"cat -n {i} | tail", capture_output=True, text=True, shell=True)
    print(content.stdout)

# Checking and outputing the directorys shown
lscommand("/home/linuxgeek/")
lscommand(f"/home/{STUUSER}/")
lscommand(f"/home/{STUUSER}/itcfinal/")

# This is a repeat of the "for loop" above (This WILL be changed! This is bad code design! Dont reuse same code blocks!)
Files2 = subprocess.run("locate kernmsg.txt", capture_output=True, text=True, shell=True)
for i in Files2.stdout.splitlines():
    print(i + " Contents:")
    content = subprocess.run(f"cat -n {i} | head", capture_output=True, text=True, shell=True)
    content2 = subprocess.run(f"cat -n {i} | tail", capture_output=True, text=True, shell=True)
    print(content.stdout, content2.stdout)

lsalcommand(f"/home/{STUUSER}/backups/orig-config/")
lsalcommand(f"/home/{STUUSER}/backups/orig-config/etc/")
