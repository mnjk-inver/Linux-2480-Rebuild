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
STUVMIP = "172.17.50."+IP

blog_url = f"http://{STUVMIP}/blog"

# Define aptcheck for checking installed programs
def aptcheck(installed, command, name):
    if installed in command.stdout:
        print(Success + f"{name} is installed")
    else:
        print(Warning + f"{name} is NOT installed!")


# Define simple command for repeated command usage
def simplecommand(command):
    output = subprocess.run(f"{command}", capture_output=True, text=True, shell=True)
    print(output.stdout)


# Define 'ls -al' command for repeated command usage
def lsalcommand(command):
    output = subprocess.run(f"ls -al {command}", capture_output=True, text=True, shell=True)
    output2 = subprocess.run(f"ls -al {command} | cat -n | head", capture_output=True, text=True, shell=True)
    output3 = subprocess.run(f"ls -al {command} | cat -n | tail", capture_output=True, text=True, shell=True)
    print(output.stdout, output2.stdout, output3.stdout)


# Define 'locate' command for both head and tails content
def locate(command):
    Files = subprocess.run(f"locate {command}", capture_output=True, text=True, shell=True)
    for i in Files.stdout.splitlines():
        print(i + " Contents:")
        content = subprocess.run(f"cat -n {i} | head", capture_output=True, text=True, shell=True, errors='ignore')
        content2 = subprocess.run(f"cat -n {i} | tail", capture_output=True, text=True, shell=True, errors='ignore')
        print(content.stdout, content2.stdout)
        

# Define 'locate' command for tail content
def locatetail(command):
    Files = subprocess.run(f"locate {command}", capture_output=True, text=True, shell=True)
    for i in Files.stdout.splitlines():
        print(i + " Contents:")
        content = subprocess.run(f"cat -n {i} | tail", capture_output=True, text=True, shell=True, errors='ignore')
        print(content.stdout)


# Define 'locate' command for both head and tails tar content
def locatetar(command):
    Files = subprocess.run(f"locate {command}", capture_output=True, text=True, shell=True)
    for i in Files.stdout.splitlines():
        print(i + " Contents:")
        content = subprocess.run(f"tar -ztvf {i} | cat -n | head", capture_output=True, text=True, shell=True, errors='ignore')
        content2 = subprocess.run(f"tar -ztvf {i} | cat -n | tail", capture_output=True, text=True, shell=True, errors='ignore')
        print(content.stdout, content2.stdout)


# Checking installed programs (Going to add 'subprocess.run' to the definition later!)
aptcheck("installed", subprocess.run("apt list locate", capture_output=True, text=True, shell=True), "locate")
aptcheck("installed", subprocess.run("apt list curl", capture_output=True, text=True, shell=True), "curl")
aptcheck("installed", subprocess.run("apt list dnsutils", capture_output=True, text=True, shell=True), "dnsutils")
aptcheck("installed", subprocess.run("apt list python3", capture_output=True, text=True, shell=True), "python3")
aptcheck("installed", subprocess.run("apt list python3-requests", capture_output=True, text=True, shell=True), "python3-requests")

# Checking hostname, sudoers, students, and user id's
simplecommand("cat /etc/passwd | grep linuxgeek")
simplecommand("cat /etc/hostname")
simplecommand("cat /etc/group | grep sudo")
simplecommand("cat /etc/group | grep students")

# Checking if host user has sudo permissions (Can be improved. Just a working example!)
is_sudo = subprocess.run("groups " + STUUSER, capture_output=True, text=True, shell=True)
if "sudo" in is_sudo.stdout:
    print("User is sudo")
else:
    print("not sudo")


# Print out files and there content from the 'locate tail' command output
locatetail("lrecent-log")

# Checking and outputing the directorys shown
simplecommand("ls -l /home/linuxgeek/")
simplecommand(f"ls -l /home/{STUUSER}/")
simplecommand(f"ls -l /home/{STUUSER}/itcfinal/")

# Gather the output using the locate command and get the head/tails content
locate("kernmsg.txt")

# Us the ls -al command to get the contents of the backups folder
lsalcommand(f"/home/{STUUSER}/backups/orig-config/")
lsalcommand(f"/home/{STUUSER}/backups/orig-config/etc/")

# Getting the tail of the system users of the home and root
locatetail("system-users | grep -E 'home|root'")

# Gather the output using the locate command and get the head/tails content
locatetar("systemlogs.tar.gz")

simplecommand("ls -al /home/linuxgeek/")
simplecommand("ls -al /home/linuxgeek/ | head")
simplecommand("ls -al /home/linuxgeek/itcfinal-backups")
simplecommand("ls -al /home/linuxgeek/itcfinal-backups | head")
simplecommand("dpkg -s apache2 2>&1 | head -2")
simplecommand("dpkg -s php 2>&1 | head -2")
simplecommand("dpkg -s php-mysql 2>&1 | head -2")
simplecommand("dpkg -s libapache2-mod-php 2>&1 | head -2")
simplecommand("dpkg -s mariadb-server 2>&1 | head -2")
simplecommand("dpkg -s wordpress 2>&1 | head -2")
simplecommand("ls -l /var/www")
simplecommand("ls -l /var/www/html")
simplecommand("ls /var/www/html/blog")
WPSITETITLE = simplecommand(f'curl -s {STUVMIP}/blog/ | grep -o "<title>[^<]*" | tail -c+8')
simplecommand(f"echo Site Title: {WPSITETITLE}")
simplecommand("echo Entry Titles: ")
simplecommand(f"curl -s {STUVMIP}/blog/ | grep -o -P '(?<=<h. class=\"entry-title heading-size-1\">).*(?=</h.>)'")
simplecommand("fdisk -l /dev/sdb")
simplecommand("file -sL /dev/sdb*")
simplecommand("mount 2>&1 | grep sd")
simplecommand("cat /etc/fstab")
simplecommand("dpkg -s samba 2>&1 | head -2")
simplecommand("tail -20 /etc/samba/smb.conf")
simplecommand(f"ls -l /home/{STUUSER}/Windows File Test/")
simplecommand("ls -al /winshare/students")
simplecommand("dpkg -s bind9 2>&1 | head -2")
simplecommand("nslookup google.com 127.0.0.1")
simplecommand(f"nslookup sba-{STUVMID}.itc2480.campus.ihitc.net 127.0.0.1")
simplecommand(f"nslookup mymachine.sba-{STUVMID}.itc2480.campus.ihitc.net 127.0.0.1")
simplecommand(f"nslookup mailserver.sba-{STUVMID}.itc2480.campus.ihitc.net 127.0.0.1")
simplecommand(f"nslookup www.sba-{STUVMID}.itc2480.campus.ihitc.net 127.0.0.1")
simplecommand(f"nslookup -q=MX sba-{STUVMID}.itc2480.campus.ihitc.net 127.0.0.1")
simplecommand(f"cat /var/lib/bind/sba-{STUVMID}.itc2480.campus.ihitc.net.hosts")
# simplecommand(f"cat /var/lib/bind/sba-{STUVMID}.itc2480.campus.ihitc.net.hosts")
simplecommand("cat /etc/dhcp/dhcpd.conf 2>&1 | tail")
simplecommand("firewall-cmd --list-all-zones")
simplecommand("iptables-legacy -L")
simplecommand("iptables-legacy -t nat -L -n -v")
simplecommand("sysctl net.ipv4.ip_forward")

myscript = subprocess.run("locate myscript", capture_output=True, text=True, shell=True)
for i in myscript.stdout.splitlines():
    print(i + " Contents:")
    content = subprocess.run(f"ls -l {i}", capture_output=True, text=True, shell=True, errors='ignore')
    content2 = subprocess.run(f"cat {i}", capture_output=True, text=True, shell=True, errors='ignore')
    print(content.stdout, content2.stdout)
print("#"*25, "END OF SCRIPT", "#"*25)
