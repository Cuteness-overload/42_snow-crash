# Flag

In the user directory, we can notice two files:
- level06 with the SUID bit set
- level06.php, a php regex script 

the php script uses the deprecated (and removed) "/e" regex modifier which enables us to execute code after regex evaluation.
By crafting a special input file, we can trigger an error that prints out our flag. 

```php
[x {${system(getflag)}}]
```
Basically, the script tries to interpret the inside of the curly braces as a double quoted string with variable interpolation like Python or Rust fstrings.
getflag is treated as a constant, but as it doesn't exist, it is replaced by "getflag", so it executes : system("getflag") and tries to use the result as a variable name and errors out since it doesn't exist.
