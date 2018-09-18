### Configure custom keys for history searching in linux terminal

There are two methods to define key bindings for the Bash commands history-search-backward, etc.

**Method 1: Using ~/.bashrc**  
1. Edit ~/.bashrc with this command:
```
gedit ~/.bashrc
```
2. Add the following lines:
```
bind '"\e[A": history-search-backward'bind '"\e[B": history-search-forward'
```
3. Save then close the file.
4. Execute this command in a terminal : 
```
source ~/.bashrc
```

**Method 2: Using ~/.inputrc**  
1. Execute this command in a terminal: 
```
cp /etc/inputrc ~/.inputrc
```
2. Edit the new ~/.inputrc file with this command: 
```
gedit ~/.inputrc
```
3. Append these lines to the file :
```
"\e[A": history-search-backward
"\e[B": history-search-forward
```
Note: 
```
“\e[5~” – Page up“
\e[6~” – Page down 
```

terminals often use ANSI control-codes to represent non-alphanumeric character sequences. For example, when editing .inputrc for Bash in Linux, it’s easy to find code sequences that look as follows:"\e[A": history-search-backward"\e[B": history-search-forward"\e[C": forward-char"\e[D": backward-char"\e[1~": beginning-of-line"\e[4~": end-of-line"\e[3~": delete-char"\e[2~": quoted-insert"\e[5C": forward-word"\e[5D": backward-word  

Both methods below are almost equivalent, it just depends on which file you want to edit. I’d recommend .bashrc myself, as it doesn’t involve editing a local copy of a system file.  
