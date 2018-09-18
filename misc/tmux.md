### TMUX guide

[Source](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-tmux-on-ubuntu-12-10–2)  

Tmux is a “terminal multiplexer”, it enables a number of terminals (or windows) to be accessed and controlled from a single terminal. It is a must when working on remote servers without root previliges and without qsub system. IT CAN BE USED TO CONTINUE RUNNING TASKS IN A REMOTE SERVER EVEN AFTER LOGGING OUT OF THE SSH SESSION !  

Tmux is intended to be a simple, modern, BSD-licensed alternative to programs such as GNU screen. This release runs on OpenBSD, FreeBSD, NetBSD, Linux, OS X and Solaris. tmux depends on libevent 2.x. Download it from: http://www.monkey.org/~provos/libevent/  

**WITH ROOT PREVILIGES:** 
1. Install libevent using 
```
./configure && make && make install 
```
2. To build tmux from a release tarball, do:
```
$ ./configure && make
$ sudo make install
```

**WITHOUT ROOT PREVILIGES:** 
1. Get libevent source from libevent.org and build. This will install the header files and libraries under folder $HOME/local
```
$./configure --prefix=$HOME/local $ make; make install
```
2. Get tmux source from tmux.sourceforge.net and build. This will statically link to libevent and put the binary under folder $HOME/local
```
$touch configure.ac aclocal.m4 configure Makefile.am Makefile.in  
( OR )
$autoreconf -ivf. $LIBEVENT_LIBS="-L$HOME/local/lib -levent" LIBEVENT_CFLAGS="-I$HOME/local/include" ./configure --prefix=$HOME/local 
$ make; make install
```
3. Add $HOME/local/bin to your PATH and tmux is ready to rock. Add the following line to ~/.bashrc file.
```
$export PATH="$HOME/local/bin:$PATH"
```
