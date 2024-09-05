import os
from arkitekto import *
import sys

if not isRoot():
    print("Please run this script as root.")
    sys.exit()

if not hasInternetConnection():
    print("You are not connected to any network.")
    sys.exit()

print("Performing post base installation tasks...")

print("Setting up locale and timezone")
configureTZandLocales()

print("Setting up hostname")
configureHostname()

print("Setting up user and privilleges")
addUser()
giveUserSudo()

print("Installing extra packages")
installExtraPkgs()

print("Enabling startup services")
enableServices()

print("Installing bootloader")
installBootloader()

print("Finished installing. type 'reboot' to reboot the computer")
os.system("exit")
