import os


def isRoot():
	return os.geteuid() == 0

def hasInternetConnection():
	return os.system("ping google.com -c 3 >> /dev/null") == 0


def isDonePartitioning(response):
	if response == "Yes" || response == "yes":
		return True
	else:
		return False


def partitionDisk(partitionTool, disk):
	os.system("cfdisk " + disk)

def formatDisk(root, boot, swap):
	os.system("mkfs.ext4 " + root)
	os.system("mkfs.fat -F 32 " + boot)
	os.system("mkswap " + swap)

def mountDisk(root, boot, swap):
	os.system("mount " + root + " /mnt")
	os.system("mount --mkdir " + boot + " /mnt/boot")
	os.system("swapon " + root)
    os.system("lsblk")

def pacmanKeyInit():
	os.system("pacman-key --init")
	os.system("pacman-key --populate archlinux")

def installSystem():
	os.system("pacstrap -K /mnt base base-devel linux linux-headers
	linux-firmware vim grub efibootmgr networkmanager")
	os.system("genfstab -U /mnt >> /mnt/etc/fstab")

def archChroot():
	os.system("arch-chroot /mnt ")
