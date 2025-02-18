# Flag

When looking at the current directory for user level07, we have an executable called level07 owned by flag0 with SUID bit set (like in previous levels).
When disassembling with gdb, we see that the flow of the program is pretty simple:
- get the value environment variable LOGNAME
- place it inside an "/bin/echo %s" format string using asprintf
- just call system() on said string, thus printing whatever we set as LOGNAME

Naturally, we set `export LOGNAME='$(getflag)'`, and we get the flag as user flag07 will be executing this call.

