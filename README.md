# snow-crash

This cybersecurity group project is an introduction to privilege escalation in linux systems,
featuring various challenges, wherein exploits allows you to log in/impersonate a user
and find the 'flag' required to access each consecutive level.

## Overview

The project is centered around *getting the flag*, i.e. the credentials to access the next level,
using for the most part the aptly named `getflag` executable to... well... get the flag printed out
(or into a file).
Thus, for each level, we had to look around the file structures, play around with buggy, unsafe,
or otherwise ill-sanitized programs/services/logs which allowed us to run the aforementioned executable.
That is, until the [last level](level14/resources/writeup.md)...

## Repository Structure

The repository is organized as follows:

```
├── README.md
├── level00
│   ├── flag
│   └── resources
│       └── writeup.md
├── level01
│   ├── flag
│   └── resources
│       └── writeup.md
...
```

## Afterword

All in all, due to the introductory nature of this project, and the relative ease
with which one of us saw through most of the challenges, we were able to complete
it pretty fast.
It was nonetheless a fun endeavour and we are looking forward to the [next challenge](https://github.com/ethanolmethanol/rainfall42)!
