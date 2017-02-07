Title: Using cookies.sqlite in wget or curl
Date: 2010-02-03 15:34
Author: slacy
Category: General
Tags: cookies, cookies.sqlite, cookies.txt, curl, sqlite, sqlite3, wget
Status: published

Newer versions of FireFox use a sqlite3 database to store their cookies.

Older versions of FireFox used a .txt file.  wget and curl know how to
parse the older style text file, but not the sqlite3 database.

So, I wrote a quick script to extract the cookies.sqlite database and
generate a file that looks just like the old cookies.txt file, and then
you can pass that to wget or curl. Here's the script:

    #!/bin/bash

    function cleanup {
    rm -f $TMPFILE
    exit 1
    }

    trap cleanup  SIGHUP SIGINT SIGTERM

    # This is the format of the sqlite database:
    # CREATE TABLE moz_cookies (id INTEGER PRIMARY KEY, name TEXT, value TEXT, host TEXT, path TEXT,expiry INTEGER, lastAccessed INTEGER, isSecure INTEGER, isHttpOnly INTEGER);

    # We have to copy cookies.sqlite, because FireFox has a lock on it 
    TMPFILE=`mktemp /tmp/cookies.sqlite.XXXXXXXXXX`
    cat $1 >> $TMPFILE
    sqlite3 -separator '    ' $TMPFILE << EOF
    .mode tabs
    .header off
    select host,
    case substr(host,1,1)='.' when 0 then 'FALSE' else 'TRUE' end,
    path,
    case isSecure when 0 then 'FALSE' else 'TRUE' end,
    expiry,
    name,
    value
    from moz_cookies;
    EOF
    cleanup

Usage should be like this:

    $ extract_cookies.sh $HOME/.mozilla/firefox/*/cookies.sqlite > /tmp/cookies.txt
    $ wget --load-cookies=/tmp/cookies.txt http://mysite.com
    $ # OR 
    $ curl --cookie /tmp/cookies.txt http://mysite.com 

You could use this script to wrap curl or wget itself in a similar
extraction scheme, so that you always get the most current cookie values
when you run wget.
