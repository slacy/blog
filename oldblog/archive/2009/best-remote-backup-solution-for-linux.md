Title: Best remote backup solution for Linux?
Date: 2009-12-18 10:08
Author: slacy
Category: General
Tags: backup, linux, remote, rsync, scp, ssh
Status: published

I'm running my own hand-crafted remote backup (rsync++) script to back
up data from one machine to another.  But, it has some serious
drawbacks, and I'm still looking for something better.  Here are my
requirements:

-   Runs on Ubuntu
-   Is either:
    -   Available in the standard distro (i.e. via apt-get)
    -   A simple self-contained script (Python, Perl, Bash, etc.)
-   Uses ssh/scp/rsync to transport files
-   Is incremental (i.e. does "what's changed from last time", and only
    backs up that much)
-   **Handles file renames & moves without re-transmitting the
    underlying data**.
-   Puts files in a simple "directory by date" format.  No fancy
    databases, no fancy metadata required for restoring.
-   Preserves file permissions & modification dates.
-   Correctly handles both hard & soft symbolic links.
-   Is client-side only.  In other words, I don't want to have to
    maintain 2 copies of this script, one for the server, and one for
    the client.

Is there anything out there that meets these requirements?
