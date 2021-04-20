import subprocess

#check to see how many lab tasks have been completed
def completion():
    print("-" * 45, "\n" "You have completed", str(done), "out of 8 tasks for this lab!")
    if done == 8:
        print("Congratulations you have completed all tasks for this lab.", "\n", "-" * 45)
    else:
        print("-" * 45)

done = 0

#module to check if a specific port is open
def port_checker(scan, port, protocol,done):
    if str(port)+"/tcp" in scan.stdout:
        print(str(protocol)+" port has been opened")
        done = done + 1
        return done
    else:
        print(str(protocol)+" is not functional or port has NOT been opened")
        return done

print("-" * 45)

#Nmap scan, look for open ports 22, 25, 53, 80, 143, 445, 2222, 10000
# scan for open port
scan = subprocess.run("/usr/bin/nmap localhost", capture_output=True, text=True, shell=True)
firewall_status = subprocess.run("sudo service firewalld status", capture_output=True, text=True, shell=True)
if "service: not found" in firewall_status.stderr:
    print("Try running this script with sudo")
    print("-" * 45)
    exit()
#Check if firewalld is running
if "Active: active (running)" not in firewall_status.stdout:
    print ("Firewalld is NOT running")
    print("-" * 45)
#    exit()
else:
    print("Firewalld service is running")
    done = done + 1
#check if telnet is open
if "23/tcp" in scan.stdout:
    print ("Telnet is not blocked by your firewall")
    print("-" * 45)
    exit()
    
#dictionary of ports to be checked
ports = {"SSH":22, "SMTP":25, "DNS":53, "HTTP":80, "IMAP":143, "SMB":445, "WEBMIN":10000}
#for loop iterating through all those services and ports
for key in ports:
    done = port_checker(scan, ports[key], key, done)


completion()
