### Adding PPA repositories under proxy

The default or normal method to add a PPA via command line is as follows:  
```
sudo add-apt-repository ppa:something
```
However, if you are behind a proxy, you may not be able to add this way and when you try to do something like this:  
```
sudo add-apt-repository ppa:gnome3-team/gnome3
you may get an error like this:

Cannot access PPA (https://launchpad.net/api/1.0/~gnome3-team/+archive/gnome3) to get PPA information, please check your internet connection.
```
 
Type   
```
export http_proxy="http://username:password@your proxy":"port" export https_proxy="https://username:password@your proxy":"port" 
```
Remember to replace “username” by your username and “password” by your password, if applicable.  
Now we have two methods to export these parameter to “sudo” user:  
  
**Method 1:**  
- Type sudo visudo.  
- Add Defaults env_keep="https_proxy" to the end of the file. (Note that Defaults has a capital “d”).  
- Type Ctrl + x and y to save and exit.  

**Method 2:**  
Whenever you use sudo command, export the environment variables of the user you are currently using. To do this, when you use sudo, use sudo -E.  
