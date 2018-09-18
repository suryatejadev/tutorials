### Dual booting Windows with a Linux distribution

1. Install Minitool partition wizard.
2. Split the required partition to get the free partition.
3. Change the free partition to unallocated space.
4. Download Universal USB installer.
5. Download the iso file of the desired linux distribution.
6. Install the iso file in a pendrive using Universal USB installer. This will make the pendrive a bootable pendrive.
7. Reboot the system with the pendrive connected.
8. After the company logo appears in the bootloader, press the required key to open boot options.
9. Select to boot from the pen drive. Linux OS is loaded.
10. In the installer, while selecting partition for OS, split the unallocated volume into the following partitions.
	- Select Ext4 journaling filesystem + / = OS (85-90 Gb)
	- Select Ext4 journaling filesystem + /boot = boot (200 Mb)
	- Select swap area = swap (5-6 Gb)
11. Continue with the installation steps. 
12. The dual boot installation is complete!
