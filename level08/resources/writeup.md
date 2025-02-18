# Flag

This time, we are met with another program with the SUID set for user flag08.
Running it, it is asking for a file to read as argument.
There is also a "token" file which is owned by flag08 and can be read by them. We supposed this contains the flag and must use the program to read it.

Giving "token" as parameter returns an error : `You may not access 'token'`
Looking at the disassembled code, we see the program checks for the string "token" within the file name via a "strstr" call.

Using symlinks we hope to bypass this check as the compared filename would be different.
```bash
ln -s /home/user/level08/token /tmp/myflag
./level08 /tmp/myflag
```
It is important to use the absolute file path for the symlink otherwise we would get broken symlink errors.
This worked and gave us the password to flag08!
`quif5eloekouj29ke0vouxean`
We can then run getflag and access level09.
