# Flag

Inspecting the user directory for "level11", we can see a SUID bit set "level11.lua" lua script.
Catting the file, we understand that the program listens on port 5151 of the localhost (127.0.0.1) for a user provided password. If the password matches a hash, it prints out `Gz you dumb*\n`, otherwise it prints out `Erf nope..\n`.

However we can also notice that the "hash" function which is responsible for converting the user provided input into a sha1 hash, does so via a bash command:
```bash
echo "..pass.." | sha1sum"
```

This means we can submit input so as to execute our own command via user input like this: 
```bash
nc 127.0.0.1 5151
Password: ; getflag > /tmp/flag
```

This will stop the echo command via the ";" symbol, then executes the getflag command and sends it to "/tmp/flag".
As the SUID bit is set, this gets us the flag ^^.
