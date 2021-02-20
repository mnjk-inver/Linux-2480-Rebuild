# this is a start
import subprocess
import os
import os.path
import requests
os.system('clear')
print()
print()
print("ITC 2480 Lab5 Self Check ... starting...")
# This script will check ITC2480 Lab 5 for successful completion
# This command will import the OS library allowing linux CLI commands
print("-------------------------------------------------")
# Used for telling the user what is installed and not installed at the end of script
Ip_set = False
Index_file_exists = False
Apache_port_open = False
Logtail_file_exists  = False
Php_installed = False

#counts completion of tasks scored
def completion_counter():
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
print("--------------------------------------------------")

#Check if ip address responds to icmp requests "ping"
hostname = StudentIP
response = subprocess.run("ping -c 1 " + "172.17.50.28", capture_output=True, text=True, shell=True)
if "1 received" in response.stdout:
   pingstatus = "Congratulations! your Server is responding to ping requests at your assigned IP"
   done = done + 1
   Ip_set = True
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
    Index_file_exists = True
else:
    print("Your index.file appears to be missing, are you able to visit your server page in a browser?")

#Check for open Port 80 (Apache)
scan = subprocess.run("/usr/bin/nmap localhost", capture_output=True, text=True, shell=True)
if "80/tcp" in scan.stdout:
    print()
    print("Port 80 has been opened to allow access to your web page and Apache Server.")
    done = done + 1
    Apache_port_open = True
else:
    print("Apache is not functional")

#database checking ideas
#check for tail redirection file
Logtail_file = os.path.isfile('/home/'+UserName+'/logtail.txt')
if Logtail_file == True:
    print('You have created a logtail.txt file in your home directory.')
    done = done + 1
    Logtail_file_exists = True

else:
    print('Try Again. There is no logfile.txt file in your home directory.')

#check to see if PHP, MySQL, MariaDB packages are installed and latest version
#check if installed package versions is latest version as of 2/19/2021
php_version = subprocess.run("apt list php", capture_output=True, text=True, shell=True)
if "php" and "[installed]" in php_version.stdout:
    print("You have installed PHP.")
    done = done + 1
    Php_installed = True
else:
    print("You have not installed the latest version of PHP.")

#Testing requests used <p></p> as this would likely be the first custom line
#checking for custom links page
Clinks_page = requests.get("http://"+StudentIP+"/")
CL2 = Clinks_page.text
print()
print()
print('Informational section')
print(CL2[CL2.find("<p>") + 3: CL2.find("</p>")])

#checking for phptest page
Phptest_page = requests.get("http://"+StudentIP+"/phptest.php")
PhpT2 = Phptest_page.text
print(PhpT2[PhpT2.find("<title>") + 7: PhpT2.find("</title>")])
print()
print()
print("-------------------------------------------------")
#Completeion count
completion_counter()

#give complete not complete results
def completion():
    if Ip_set and Index_file_exists and Apache_port_open and Logtail_file_exists and Php_installed is True:
        print("-------------------------------------------------")
        print("Everything is installed correctly. Great Work!")
        print("-------------------------------------------------")
    if Ip_set is False:
        print("Your Ip address is not set.")
    if Index_file_exists is False:
        print("Your index.html file does not exist.")
    if Apache_port_open is False:
        print("The port necessary port to access your webpage is not open, or Apache is not installed.")
    if Php_installed is False:
        print("PHP is not installed correctly.")

completion()