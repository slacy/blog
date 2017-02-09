Title: Local port forwarding via ssh
Date: 2011-01-25 16:19
Author: slacy
Category: General
Tags: localhost, port forwarding, ssh
Status: published

This is one of those things that took too long to figure out.

**Problem**: You need to accept incoming connections on a privileged
port (&lt;1024) and forward the connections to an unprivileged port.

**Solution**: Set up a local ssh connection, as root, with port
forwarding.

**Details:**

-   "sudo bash" and as root, generate a keypair for root if you don't
    already have one.
-   As root, "cat id\_rsa.pub &gt;&gt; authorized\_keys" if you haven't
    already done this.
-   Test it out by doing "sudo ssh localhost".  You should not be
    prompted for a password, and you should get a root shell prompt.
-   Add "GatewayPorts yes" to \~root/.ssh/config

Now, when you want to port forward, you can run:

    sudo ssh -N -L 80:localhost:8080 localhost

This will listen on port 80, and forward any connections to 8080,
locally. If you, for some reason, need this globally, then add the -g
parameter to ssh, but that's super dangerous.
