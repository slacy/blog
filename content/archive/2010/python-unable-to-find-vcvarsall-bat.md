Title: Python: Unable to find vcvarsall.bat
Date: 2010-09-21 21:35
Author: slacy
Category: General
Tags: 2008, easy_install, pip, python, vcvarsall.bat, virtualenv, visual studio express, zc.buildout
Status: published

If you're running easy\_install, pip, zc.buildout, virtualenv, or a
similar tool on Windows, and it says:

    unable to find vcvarsall.bat

The issue is that you need a compiler installed on your system.  Many
people seem to recommend MinGW, but I've been there, and it's a huge
pain in the butt.

Just download and install **[Microsoft Visual Studio Express
2008](http://www.microsoft.com/express/Downloads/#2008-Visual-CPP)**
which is *free*. Please note the 2008 part.  This must match the
compiler that Python itself was built with, and that's the 2008 (NOT
2010) version.  (See
<http://mail.python.org/pipermail/python-list/2010-April/1242706.html>
for more details why 2008 is important.)
