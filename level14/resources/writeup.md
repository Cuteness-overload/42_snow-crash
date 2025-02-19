# Flag

For this last level, we are greeted by... *NOTHING*!

Thus we start to wonder what it is we need look at.
No user files for users level14 nor flag14.
Hence we look at the last thing we can check: getflag.

As it turns out, the function we decompiled for last level is actually used within getflag, and it is called for each user, checking its user id and giving the corresponding flag.

By decompiling getflag, using the `ft_des` function we already had fixed up, and the last string constant corresponding to the last level (all levels are present), we're able to get the **final flag for this cybersecurity challenge**. Hell yeah!
