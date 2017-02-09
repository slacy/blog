Title: Django development setup on Windows
Date: 2010-09-21 16:19
Author: slacy
Category: General
Tags: django, postgresql, python, setuptools, visual studio express, windows, zc.buildout
Status: published

Django development on Windows sounds easy, but there are a bunch of
steps to get it all working right.

-   Python.  Use **Python 2.7** from python.org
    ﻿<http://python.org/download/>.  I recommend avoiding the 3rd party
    Python distributions (ActiveState, Enthought, etc.) and sticking
    with the official build.  As a note, this python is (currently)
    built with Video Studio 2008.
-   **Visual Studio Express 2008**.  Note the 2008 part.  The version
    Python is built with **much** match the version used to
    build extensions.  This is currently still available from the
    Microsoft download site, but is a bit buried under a couple links.
     When installing, don't bother installing SQL Server 2008.  You
    won't need it.
-   **PostgreSQL 8.4**.  I chose this version because it most closely
    matched my Linux deployment.  Download and run the installer from
    <http://www.enterprisedb.com/products/pgdownload.do#windows> and
    make sure to choose version 8.4.
-   **setuptools** from
    <http://pypi.python.org/pypi/setuptools#windows>.  This will allow
    you to easily download and install other package add-ons.

Next, you'll need to manually modify your PATH to include Python &
PostgreSQL.    Go to Control Panel-&gt;System-&gt;Advanced system
settings-&gt;Environment Variables, and make sure that your Path
contains:

﻿C:\\Python27\\;C:\\Python27\\Scripts;C:\\Program
Files\\PostgreSQL\\8.4\\bin

<span style="font-size: 15.6px;">Then, you'll need to install some extra
Python libraries:</span>

C:\\&gt; easy\_install pil  
C:\\&gt; easy\_install psycopg2

Then, you can run your zc.buildout script to bring in everything else.
