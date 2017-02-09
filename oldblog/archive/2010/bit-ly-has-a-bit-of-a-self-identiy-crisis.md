Title: bit.ly has a bit of a self-identiy crisis.
Date: 2010-04-18 12:10
Author: slacy
Category: General
Status: published

    $ curl -v http://bit.ly/a
    * About to connect() to bit.ly port 80 (#0)
    *   Trying 168.143.174.29... connected
    * Connected to bit.ly (168.143.174.29) port 80 (#0)
    > GET /a HTTP/1.1
    > User-Agent: curl/7.19.5 (x86_64-pc-linux-gnu) libcurl/7.19.5 OpenSSL/0.9.8g zlib/1.2.3.3 libidn/1.15
    > Host: bit.ly
    > Accept: */*
    <
    < HTTP/1.1 301 Moved
    < Server: nginx/0.7.42
    < Date: Sun, 18 Apr 2010 20:05:21 GMT
    < Content-Type: text/html; charset=utf-8
    < Connection: keep-alive
    < Set-Cookie: _bit=4bcb6601-0037b-0165b-b8a08fa8;domain=.bit.ly;expires=Fri Oct 15 16:05:21 2010;path=/; HttpOnly
    < Location: http://apple.com
    < MIME-Version: 1.0
    < Content-Length: 278
    <
    <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
    <HTML>
    <HEAD>
    <TITLE>Moved</TITLE>
    </HEAD>
    <BODY>
    <H2>Moved</H2>
    <A HREF="http://apple.com">The requested URL has moved here.</A>
    <P ALIGN=RIGHT><SMALL><I>AOLserver/4.5.1 on http://127.0.0.1:7200</I></SMALL></P>
    </BODY>
    * Connection #0 to host bit.ly left intact
    * Closing connection #0

Are they really running AOLServer? Is bit.ly written in TCL? Looks like
they're fronting their traffic via nginx, which is good. :)
