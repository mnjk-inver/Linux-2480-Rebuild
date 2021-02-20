# this is a start
print()
print("ITC 2480 Self Check ... starting...")
# This script will check ITC2480 Lab 5 for successful completion
# This command will import the OS library allowing linux CLI commands
import subprocess
import os
import os.path

print()

def completion():
    print()
    print("You have completed "+str(done)+" of "+str(total)+" tasks for this lab.")
    if done == total:
        print("Congratulations you have completed all tasks for this lab")
    print()

done = 0
total = 4

#get assigned ip address and user name
StudentIP = input("Please enter your assigned IP address: ")
UserName = input("please provide the user name for your account:")

#Check if ip address responds to icmp requests "ping"
hostname = StudentIP
response = os.system("ping -c 1 " + hostname)
if response == 0:
   pingstatus = "Congratulations! your Server is responding to ping requests at your assigned IP"
   done = done + 1
else:
    pingstatus = "Try Again! Network Error - Your Server is not responding to ping requests"

print(pingstatus)

#Request information from index.html file to verify custom link page
Index_file = os.path.exists('/var/www/html/index.html')
if Index_file == True:
    print("Your index.html file has been created, Great Start")
    done = done + 1
else:
    print("Your index.file appears to be missing, are you able to visit your server page in a browser?")

#Check for open Port 80 (Apache)
scan = subprocess.run("/usr/bin/nmap localhost", capture_output=True, text=True, shell=True)
if "80/tcp" in scan.stdout:
    print("Port 80 has been opened to allow access to your web page and Apache Server")
    done = done + 1
else:
    print("Apache is not functional")

#database checking ideas
#check for tail redirection file
logtail_file = os.path.isfile('/home/+UserName+/logtail.txt')

print(logtail_file)
print(UserName)


#check to see if PHP, MySQL, MariaDB packages are installed and latest version
#check if installed package versions is latest version as of 2/19/2021
php_version = subprocess.run("apt list php7.3", capture_output=True, text=True, shell=True)
if "php7.3" and "[installed,automatic]" in php_version.stdout:
    print("You have installed the latest version of PHP")
    done = done + 1
else:
    print("You have not installed the latest version of PHP.")

completion()
