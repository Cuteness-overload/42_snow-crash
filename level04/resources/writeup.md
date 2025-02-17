# Flag

Again, taking a look at the user directory shows us a file called "level04.pl"
This is a perl script. When catting it out, we can see that it is a cgi script that takes a parameter "x" and executes the shell command "echo theparameter 2>&1".

With a bit of luck, a webserver is running on this machine and we will be able to exploit this with the following parameter: "$(getflag)", as this would echo out what getflag returns, ie. the flag.

We forward port 7474 (as specified in a comment in the script) on our VM and access it. A webserver does exist!
```
http://127.0.0.1:4747/?x=$(getflag)
```
Running our command does indeed give us the flag, let's go ^^
