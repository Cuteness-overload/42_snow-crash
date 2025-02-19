# Flag

This challenge gives us a compiled binary. When trying to run it, we face the issue of needing to be UID 4242.
This of course isn't possible unless we are root. So we decided to look under the hood at the decompiled code.

Using gdb, we first noticed an interesting string constant as follows: `boe]!ai0FB@.:|L6l@A?>qJ}I`
While this is not the flag, we noticed it was passed to another function called "ft_des". DES is a symmetric cipher used for data transmission. We can therefore assume the random string is either encrypted or decrypted into the output we want.

Launching ghidra, we copy the decompiled function "ft_des" and ran it locally on our machine, passing it the string as argument. (after some slight modifications to allow it to be compiled).

This gave us the flag to level14!
