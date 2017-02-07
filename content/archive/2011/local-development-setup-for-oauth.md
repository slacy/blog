Title: Local development setup for OAuth. 
Date: 2011-02-18 14:51
Author: slacy
Category: General
Status: published

Developing OAuth applications can be a little bit tricky.  Particularly
when you want to test out the interaction between your local development
server and the 3rd party authentication.  Here's a quick rundown of how
I'm developing my site.  For this example, assume my domain name is
**example.com**.  (These examples are for Ubuntu Linux, and may work on
Macintosh systems.  The general principal below should work on Windows,
but the exact configurations will be different.) This setup should work
for Django, Pyramid, Pylons, RoR, and pretty much any other web
framework.

-   Get API keys for **example.com** on your favorite OAuth provider.
     Register an "Example" application name, and set the callback domain
    name to "**local.example.com**"
-   Modify /etc/hosts and add a line that looks like this:

        # For OAuth development:
        127.0.0.1 local.example.com
        ::1 local.example.com

-   Modify /etc/host.conf and make sure it looks like this:

        order hosts,bind
        multi on

-   Run a port forwarder to forward incoming connections on port 80 to
    your local development server (running on 8000, 8080, 6543, etc.)

        sudo ssh -N -L 80:localhost:6543 localhost

    or if you're on a Mac, try this:

        sudo ssh -N -L 80:localhost:6543 username@localhost

    <p>
    , replacing "username" with the user name that you use to log in.  
   (Modify the port number 6543 as necessary for your
    development server.)

That should just about do it.  Good luck!
