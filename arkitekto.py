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


def partitionDisk(disk):
	os.system("cfdisk " + disk)

def formatDisk(root, boot, swap):
	os.system("mkfs.ext4 " + root)
	os.system("mkfs.fat -F 32 " + boot)
	os.system("mkswap " + swap)

def mountDisk(root, boot, swap):
	os.system("mount " + root + " /mnt")
	os.system("mount --mkdir " + boot + " /mnt/boot")
	os.system("swapon " + root)

def pacmanKeyInit():
	os.system("pacman-key --init")
	os.system("pacman-key --populate archlinux")

def installSystem():
	os.system("pacstrap -K /mnt base base-devel linux linux-headers linux-firmware vim grub efibootmgr networkmanager nvim")
	os.system("genfstab -U /mnt >> /mnt/etc/fstab")
    os.system("cp -r arkitekto/ /mnt/arkitekto/")

def archChroot():
    os.system("arch-chroot /mnt bash -c 'cd /arkitekto;python post-base-installation.py'")

def configureTZandLocales():
    os.system("ln -sf /usr/local/share/zoneinfo/Asia/Manila")
    os.system("echo 'LANG=en_US.UTF-8' >> /etc/locale.conf")
    os.system("echo 'en_US.UTF-8 UTF-8' >> /etc/locale-gen;locale-gen")
    os.system("hwclock --systohc")

def configureHostname():
    os.system("echo 'arch' >> /etc/hostname")

def addUser():
    os.system("useradd -mG wheel xarwin")
    print("Set user password")
    os.system("passwd xarwin")
    print("Set root password")
    os.system("passwd")

def giveUserSudo():
    os.system("echo '%wheel ALL=(ALL:ALL) ALL' | sudo EDITOR='tee -a' visudo")

def installExtraPkgs():
    os.system("pacman -S $(cat packages.txt |xargs) --needed --noconfirm")

def enableServices():
    os.system("systemctl enable bluetooth cups NetworkManager gdm")

def installBootloader():
    os.system("grub-install --target=x86_64-efi --target-directory=/boot --bootloader-id=GRUB")
    os.system("grub-mkconfig -o /boot/grub/grub.cfg")

