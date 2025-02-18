# Flag

This time around, we seem to have a program that takes a file and sends it to a server on port 6969 (nice).
However, it checks if we have access to the file. The "token" file we want to read however is only readable by "flag10".

This probably means we'll have to try and create a race condition such that it checks for access, validates access, then reads the file and sends the contents to our server.
We will have to switch the file (or where that file is pointing to) in between the access check and the read. To do that, we can utilize a infinite loop that creates a file in tmp, then makes it a symlink, deletes the symlink, and repeats.
We will also create an infite loop that constantly tries to run level10 with the file we are constantly modifying.

Please check the bash scripts in this directory for the idea

```
bash /tmp/fileloop.sh &
bash /tmp/programloop.sh
*** in another terminal ***
nc -lk 6969
```

This gives us the token to flag10, and we can then get the flag!
`woupa2yuojeeaaed06riuj63c`
