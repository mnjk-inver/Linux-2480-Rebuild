import requests, subprocess, os.path

def completion():
    print("------------------------------------------")
    print("You have completed "+str(done)+" of "+str(total)+" tasks for this lab.")
    if done == total:
        print("Congratulations you have completed all tasks for this lab")
    print("------------------------------------------")

done = 0
total = 6

def requesting(ipaddress):
    try:
        r=requests.get(ipaddress)
        r2 = r.text
        r3 = (r2[r2.find("<title>") + 7: r2.find("</title>")])
        return r3
    except(requests.exceptions.ConnectionError):
        pass

def version_check(app):
    version = subprocess.run("apt-cache policy "+app, capture_output=True, text=True, shell=True)
    try:
        installed = version.stdout.splitlines()[1]
        latest = version.stdout.splitlines()[2]
        version = {"installed":installed.split()[1],"latest": latest.split()[1]}
    except IndexError:
        pass
    return version

print("------------------------------------------")

apps = ["postfix","courier-pop","courier-imap", "fam"]
for app in apps:
    appname = version_check(app)
    if appname['installed'] == appname['latest']:
        print(app+' is installed correctly')
        done = done + 1
    else:
        print (app+" is not installed correctly")

#check for alias of sysadmin
#check for telnet port 25
scan = subprocess.run("/usr/bin/nmap localhost", capture_output=True, text=True, shell=True)
if "25/tcp" in scan.stdout:
    print("Telnet port has been opened")
    done = done + 1
else:
    print("Telnet is not functional")

#verify postfix service is running
services = subprocess.run("systemctl --type=service",  capture_output=True, text=True, shell=True)
if "postfix" in services.stdout:
    print("Postfix is running")
    done = done + 1
else:
    print("Postfix is NOT running")

#email to standup server

completion()