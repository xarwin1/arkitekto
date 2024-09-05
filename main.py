import os
import sys
from arkitekto import *

if not isRoot():
	print("Please run this script as root.")
	sys.exit()

if not hasInternetConnection():
	print("You are not connected to a network.")
	sys.exit()

response = input("Are you done partitioning? (yes/no): ")

while not isDonePartitioning(response):
	os.system("lsblk")
	disk = input("What disk do you want to partition?: ")
	partitionDisk(disk)
	response = input("Are you done partitioning? (yes/no): ")
	isDonePartitioning(response)

os.system("lsblk")
print("Enter partitions for formatting and mounting")

root = input("Enter root partition: ")
boot = input("Enter boot partition: ")
swap = input("Enter swap partition: ")

formatDisk(root, boot, swap)
mountDisk(root, boot, swap)

print("Initializing pacman keys...")
pacmanKeyInit()
print("Installing base system...")
installSystem()
print("Base system install complete. Chrooting to /mnt...")
archChroot()





