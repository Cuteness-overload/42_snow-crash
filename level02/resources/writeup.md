# Flag

Inspecting the user directory, we see an interesting file: level02.pcap
A pcap file is a "packet capture" file, which can be read using tools such as wireshark. let's download it and see what we find!
```
scp -P 4242 level02@127.0.0.1:/home/user/level02/level02.pcap level02.pcap
wireshark level02.pcap
```

At first glance we see a random TCP exchange between two IPs: 59.233.235.223 59.233.235.218
But we notice that some have Data in them.
If we click on "Analyse", the "Follow", then "TCP Stream", we can view the entire exchange, with an interesting section about "login and password". 
password: ft\_wandr...NDRel.L0L
Looking at it in hexadecimal, we can see the dots correspond to "7f", which in ascii translates to the DEL symbol. so in reality the password is "ft\_waNDReL0L"

This gets us to flag02!
