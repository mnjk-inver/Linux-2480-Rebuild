import subprocess
import os
os.system('clear')

pingtest = subprocess.run("ping -c 1 " + "172.17.50.28", capture_output=True, text=True, shell=True)


if "1 received" in pingtest.stdout:
    print("success")

print("hello world!")
