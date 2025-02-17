# Flag

Enumerating again, we find that "flag05" owns two interesting files, one we can't read and one called /usr/sbin/openarenaserver
It's a shell script that seems to execute all the files in /opt/openarenaserver

from the looks of it, this is most likely a cronjob, ie. a script that runs automatically on a regular basis. with a bit of luck we could get it to give us the flag!

Let's create a script as follows:
```
echo "getflag > /tmp/flag" > /opt/openarenaserver/flag.sh
```

After waiting for a bit, we get a flag file in "/tmp" containing the output of getflag!
