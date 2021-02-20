# this is a start
print()
print("ITC 2480 Lab5 Self Check ... starting...")
# This script will check ITC2480 Lab 5 for successful completion
# This command will import the OS library allowing linux CLI commands
import subprocess
import os
import os.path
import requests


print()

def completion():
    print()
    print("You have completed "+str(done)+" of "+str(total)+" tasks for this lab.")
    if done == total:
        print("Congratulations you have completed all tasks for this lab")
    print()

done = 0
total = 5

#get assigned ip address and user name
StudentIP = input("Please enter your assigned IP address: ")
UserName = input("please provide the user name for your account: ")
print()
#Check if ip address responds to icmp requests "ping"
hostname = StudentIP
response = os.system("ping -c 1 " + hostname)
if response == 0:
   pingstatus = "Congratulations! your Server is responding to ping requests at your assigned IP"
   done = done + 1
else:
    pingstatus = "Try Again! Network Error - Your Server is not responding to ping requests"
print()
print(pingstatus)

#Request information from index.html file to verify custom link page
Index_file = os.path.exists('/var/www/html/index.html')
if Index_file == True:
    print()
    print("Your index.html file has been created, Great Start!")
    done = done + 1
else:
    print("Your index.file appears to be missing, are you able to visit your server page in a browser?")


#Check for open Port 80 (Apache)
scan = subprocess.run("/usr/bin/nmap localhost", capture_output=True, text=True, shell=True)
if "80/tcp" in scan.stdout:
    print()
    print("Port 80 has been opened to allow access to your web page and Apache Server.")
    done = done + 1
else:
    print("Apache is not functional")


#Testing requests used <p></p> as this would likely be the first custom line
#checking for custom links page
Clinks_page = requests.get("http://"+StudentIP+"/")
CL2 = Clinks_page.text
print('testing section')
print(CL2[CL2.find("<p>") + 7: CL2.find("</p>")])

#checking for phptest page
Phptest_page = requests.get("http://"+StudentIP+"/phptest.php")
PhpT2 = Phptest_page.text
print(PhpT2[PhpT2.find("<title>") + 7: PhpT2.find("</title>")])


#database checking ideas
#check for tail redirection file
Logtail_file = os.path.isfile('/home/'+UserName+'/logtail.txt')
if Logtail_file == True:
    print()
    print('You have created a logtail.txt file in your home directory.')
    done = done + 1
else:
    print('Try Again. There is no logfile.txt file in your home directory.')

#check to see if PHP, MySQL, MariaDB packages are installed and latest version
#check if installed package versions is latest version as of 2/19/2021
php_version = subprocess.run("apt list php7.3", capture_output=True, text=True, shell=True)
if "php7.3" and "[installed,automatic]" in php_version.stdout:
    print("You have installed the latest version of PHP.")
    done = done + 1
else:
    print("You have not installed the latest version of PHP.")

completion()
