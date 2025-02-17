# Flag

If we remember from our enumeration in level00, we found that /etc/passwd had some strange value in the password field for flag01 instead of the usual "x".

On very old linux systems, password were stored in the /etc/passwd file. They are nowadays stored in a separate file, /etc/shadow. 
Let's copy it to our system and try to crack it!'
```bash
scp -P 4242 level01@127.0.0.1:/etc/passwd passwd
john passwd
john --show passwd
```

This gives us the password "abcdefg" which gets us to flag01!
getflag then gets us the flag and to level02 ^^
