#!/usr/bin/env python3
# This script will check ITC2480 Lab 7 for successful completion
# Import OS Library
import os

print()

def completion():
    print()
    print("You have completed "+str(done)+" of "+str(total)+" tasks for this lab.")
    if done == total:
        print("Congratulations you have completed all tasks for this lab.")
    print()

done = 0
total = 3

fstab = 0

fst1 = "/dev/sdb1       /mnt/part1      ext4    defaults        0       0"
fst2 = "/dev/sdb2       /mnt/btrfs      btrfs   defaults        0       0"
mnt1 = "/dev/sdb1 /mnt/part1 ext4"
mnt2 = "/dev/sdb2 /mnt/btrfs btrfs"

with open("/etc/fstab") as a:
	if fst1 in a.read():
		fstab = fstab + 1

with open("/etc/fstab") as a:
	if fst2 in a.read():
		fstab = fstab + 1

if fstab == 2:
	print("1. fstab is configured correctly.")
	done = done + 1
else:
	print("1. fstab is configured incorrectly.")

with open("/proc/mounts") as b:
	if mnt1 in b.read():
		print("2. sdb1 is mounted.")
		done = done + 1
	else:
		print("2. sdb1 is not mounted.")

with open("/proc/mounts") as b:
	if mnt2 in b.read():
		print("3. sdb2 is mounted.")
		done = done + 1
	else:
		print("3. sdb2 is not mounted.")

completion()
