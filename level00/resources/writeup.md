# Startup Info

We can initially connect to the machine using the identifiers level00:level00
It is also recommended we use ssh and scp as this avoids working directly on the VM and simplifies file transfers to and from the machine.

- ssh level00@127.0.0.1 -p 4242  (if we have configured port forwarding to 4242)

- scp -P 4242 filefrompc user@127.0.0.1:/home/user/ 
- scp -P 4242 user@127.0.0.1:/home/user/file filetopc 

# Flag

looking at the files in the user directory, we see nothing of note.
sudo - l doesn't give us any useful info either

"cat /etc/passwd" shows us a hash for the flag01, but not flag00, so let's keep it in the back of our head and keep looking.

"find / -user level00" gives nothing
"find / -user flag00" shows two files: /usr/sbin/john and /rofs/usr/sbin/john
catting both files gives us a cryptic string: cdiiddwpgswtgt
inserting this as the password doesn't work, so it's probably encrypted.

Let's try some basic ciphers, like the Cesar Cipher.
That gives us: nottoohardhere

Yay! that logs us into flag00 (su flag00)
and with "getflag", we have the flag!
