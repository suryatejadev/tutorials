### Getting started with Raspberry Pi

Raspberry pi is a mini computer which can be connected to external output hardware to make it a complete computer.  

1. Take an sd card. Format it using SDFormatter.
2. Download an OS image file from Rpi official website.
3. Install the OS on the SD card using the software Win32DiskImager.
4. Connect the following to the Rpi:
	- USB cable for power supply
	- Keyboard and mouse using USB port
	- Monitor using HDMI/VGA cable.
	- Connect the SD card.
5. Rpi is ready to use !

**Important notes:**  
1. Browser – netsurf
2. Text editor – leafpad
3. Immediately after installing, a configuration window will appear, which can also be opened using ‘raspi-config’ . Change the password and enable the camera from there.

**SSH communication with Rpi:**  
SSH is a protocol that can be used to communicate with Rpi through terminal.
1. Connect Rpi to laptop using an ethernet cable.
2. Enter the command ‘ hostname -I’ in the terminal of the Rpi. The IP address of the Rpi will be displayed. The Rpi will get an IP address only after it is connected to the laptop.
3. In the terminal, enter the command ‘ssh pi@<ip address>’.
4. It will prompt to enter the password. Enter the password of the Rpi.
5. ssh connection is established ! You can now enter Rpi terminal commands from your terminal.
