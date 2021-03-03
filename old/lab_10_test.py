import subprocess

def completion():
    print("-" * 45, "\n" "You have completed", str(done), "out of 8 tasks for this lab!")
    if done == 8:
        print("Congratulations you have completed all tasks for this lab.", "\n", "-" * 45)
    else:
        print("-" * 45)
done = 0
print("-" * 45)

#Nmap scan, look for open ports 22, 25, 53, 80, 143, 445, 2222, 10000
# scan for open port
scan = subprocess.run("/usr/bin/nmap localhost", capture_output=True, text=True, shell=True)
firewall_status = subprocess.run("service firewalld status", capture_output=True, text=True, shell=True)
#print(firewall_status.stderr)
if "service: not found" in firewall_status.stderr:
    print("Try running this script with sudo")
    print("-" * 45)
    exit()

if "Active: active (running)" not in firewall_status.stdout:
    print ("Firewalld is NOT running")
    print("-" * 45)
    exit()
else:
    print("Firewalld service is running")
    done = done + 1

if "23/tcp" in scan.stdout:
    print ("Telnet is not blocked by your firewall")
    print("-" * 45)
    exit()
#Check SSH port 22
if "22/tcp" in scan.stdout:
    print("SSH port has been opened")
    done = done + 1
else:
    print("SSH is not functional or or port has NOT been opened")

#Check SMTP port 25
if "25/tcp" in scan.stdout:
    print("SMTP port has been opened")
    done = done + 1
else:
    print("SMTP is not functional or port has NOT been opened")

#Check DNS port 53
if "53/tcp" in scan.stdout:
    print("DNS port has been opened")
    done = done + 1
else:
    print("DNS is not functional or port has NOT been opened")

#Check HTTP port 80
if "80/tcp" in scan.stdout:
    print("HTTP port has been opened")
    done = done + 1
else:
    print("HTTP is not functional or port has NOT been opened")

#Check IMAP port 143
if "143/tcp" in scan.stdout:
    print("IMAP port has been opened")
    done = done + 1
else:
    print("IMAP is not functional or port has NOT been opened")

#Check SMB port 445
if "445/tcp" in scan.stdout:
    print("SMB port has been opened")
    done = done + 1
else:
    print("SMB is not functional or port has NOT been opened")

#Check PC2 SSH port 2222
# pc2scan = subprocess.run("nmap - p 2222 192.168.1.100", capture_output=True, text=True, shell=True)
# if "0 hosts up" not in pc2scan.stdout:
#     print("SSH port on second PC has been opened")
#     done = done + 1
# else:
#    print("SSH port on second PC is NOT functional")

#Check Webmin 10000
if "10000/tcp" in scan.stdout:
    print("Webmin port has been opened")
    done = done + 1
else:
    print("Webmin is not functional or port has NOT been opened")

completion()
