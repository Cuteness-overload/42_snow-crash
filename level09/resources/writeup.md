# Flag

As usual, we have an executable owned by flag09. We also have a "token" file that we can read this time.
However it seems to contain gibberish. taking a look at what level09 does, it seems to increment each char by its index in the string. 
So "aaa" becomes "abc". We guess this is what happened to the contents of "token".

We therefore made a simple python script to reverse this transposition: "script.py" that you can find in our ressources.

Running this on the token file gives us a token which we can use to login as "flag09"
`f3iji1ju5yuevaus41q1afiuq`

getflag then gives us the flag ^^
