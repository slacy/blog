Title: Port forwarding using netcat
Date: 2011-01-12 15:14
Author: slacy
Category: General
Tags: linux, nc, netcat, port forwarding, ports, ssh, tcp
Status: published

netcat (nc) is a really useful, if obscure command for managing and
listening on TCP sockets.

I had a need to implement a local port forward on my machine. (more
details coming).  I could use ssh to do this, but decided to write a
simple shell script using nc instead.  Here's the script, which I'm
calling port\_forward.sh

    #!/bin/bash
    # Run as root if your listening port is < 1024!

    FIFO=$(mktemp -u)
    trap "rm -f $FIFO; killall -9 nc; exit 255;" SIGINT SIGTERM SIGKILL
    mkfifo $FIFO

    while true; do
        # echo "Listening..."
        cat $FIFO | nc -k -l localhost $1 | nc localhost 6543 > $2
    done

And then, you run it like this:

    $ ./port_forward.sh 80 8080
