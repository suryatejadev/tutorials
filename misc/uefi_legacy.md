### UEFI Vs Legacy

Firmware is the piece of software that acts as an interface between the hardware(motherboard) and the Operating System. Legacy Mode refers to BIOS firmware. Basic Input/Output System(BIOS) was the first popular firmware for desktop PC introduced in 1975 by IBM for its CP/M OS. Even though it is still widely present, computers have evolved tremendously and BIOS is unable to provide advanced features of modern hardware.  

Unified Extensible Firmware Interface(UEFI) is the successor to BIOS. UEFI uses the GUID Partition Table (GPT) whereas BIOS uses the Master Boot Record(MBR) partitioning scheme. GPT and MBR are both formats specifying physical partitioning information on the hard disk. Below I have listed the difference:  
1. Max partition size in MBR is ~2TB whereas in UEFI it is ~9 ZetaBytes
2. MBR can have at max 4 primary partition whereas GPT can have 128.
3. MBR can store only one bootloader whereas GPT has a separate dedicated EFI System Partition(ESP) for storing multiple bootloaders. This is very helpful if you have two or more operating systems which require different bootloaders.
4. UEFI offers secure boot which can prevent boot-time viruses from loading.
5. There are many more differences and UEFI is completely different from Legacy BIOS. http://www.rodsbooks.com/ by Roderick W. Smith  is an excellent online resource to learn about UEFI and BIOS.  

BIOS is pretty much outdated and UEFI offers many useful features. Thus it is recommended to install any operating system in UEFI mode. Note: One can’t install in UEFI mode by booting in legacy mode.  
