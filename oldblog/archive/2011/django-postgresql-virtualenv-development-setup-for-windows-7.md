Title: Django + PostgreSQL + virtualenv Development setup for Windows 7
Date: 2011-06-02 11:09
Author: slacy
Category: General
Tags: django, installer, pip, postgresql, psycopg2, virtualenv, windows
Status: published

Here's what you need to do Django development on Windows 7. As I go
through the install, I'm writing down all the steps to make sure that I
don't miss any. I'm going to focus on:

-   **Python 2.7.1** from python.org
-   **virtualenv** (manages python packages and dependencies)
-   **Visual Studio 2008** (for compiling Python addons)
-   **PostgreSQL 8.4** (database engine)
-   **Django 1.3** (our web framework)
-   Windows **psycopg2** installer

It will be possible to install any other requirements (PIL, etc.) using
pip after the virtualenv is set up.

Note on 32-bit versus 64-bit
----------------------------

Most modern computers these days are 64-bit capable, and will (usually)
be running a 64-bit operating system.  In addition, they can also run
older 32-bit binaries.  When you install all the components below, you
must choose either

Install Visual C++ 2008 Express Edition with SP1
------------------------------------------------

This is the compiler tool needed to build other python extensions we'll
be adding later. Download it
from ﻿[Microsoft](http://microsoft.com/visualstudio/en-us/products/2008-editions/express).
  Select "Visual C++ 2008 Express Edition with SP1", choose your
Language and click the "Free Download" button.

You **must** use the 2008 edition, since that's the compiler that was
used to build Python 2.7.1, and the compiler versions **must** match for
the additions to be compatible.  If you already have a newer version of
Visual Studio installed, please also install the 2008 edition I've
linked to.

You do not need to install the Silverlight runtime or Microsoft SQL
Server, unless you think you want these for other purposes.

This compiler is only 32-bit capable, so we'll be sticking to 32-bit
Python below.  This shouldn't cause any issues for most development
installs.  If you have an official purchased version of Visual C++ 2008
that's 64-bit, then you're on your own.

Install 32-bit Python 2.7.1 from python.org
-------------------------------------------

Start on [python.org](http://python.org/getit) and select "Python 2.7.1
Windows Installer".  Please **do not** choose the x86-64 Installer, as
it isn't compatible with the compiler from above.

Download and install python-2.7.1.msi

-   Select "Install for all users"
-   Use the default location of "C:\\Python27" (note: no period)
-   Use the default options on "Customize Python".

Install setuptools from python.org
----------------------------------

setuptools is a Python package that facilitates installing other
packages (and thus, bootstrapping your install system).  We'll use
setuptools to install other packages, but first we need to install it.
 Get it from
[python.org](http://pypi.python.org/pypi/setuptools#downloads).  I'm
using "setuptools-0.6c11.win32-py2.7.exe"  Download and run that binary,
and use the default options in the installer.

Install PostgreSQL 8.4
----------------------

This will be your database server.  We use this version because it
mirrors what we use in the production environment.  Select the [8.4.8-1
installer for
Windows](http://enterprisedb.com/products-services-training/pgdownload#windows).

Run the installer and use the default install options. You'll need to
choose a password for the postgres user.  Choose something you won't
forget.

You do not need to run the "Stack Builder" tool.  Un-check that option
and finish your install.

Install psycopg2 for windows
----------------------------

**psycopg2** is the interface API from PostgreSQL to Python.
 Unfortunately, it's not packaged in a way that's easy to install
automatically, so you have to download and install it.  Choose the
proper version for your Python (likely 2.7, 32-bit as we've discussed
 before).  [Here's a link to all the available
packages.](http://www.stickpeople.com/projects/python/win-psycopg/)

Install virtualenv
------------------

virtualenv is a Python tools that helps us manage and install Python
packages in a neat and clean way.  It also helps the installation of
these packages to other systems (like to our deployment environment,
which is likely Linux). Run:

    C:\>cd \Python27\Scripts
    C:\Python27\Scripts>easy_install virtualenv

From this point forward, we won't use easy\_install anymore.

Create a development environment using virtualenv
-------------------------------------------------

The virtualenv tool will create an "environment" where you can install
any needed Python packages, like Django.  This environment contains
specially modified versions of Python and other tools that make
dependency management much, much easier.  Choose a directory for your
environment.  I like to put things in
/Home/&lt;username&gt;/Desktop/src/&lt;environment\_name&gt;  for easy
access.

    C:\Users\Steve Lacy\Desktop>mkdir src
    C:\Users\Steve Lacy\Desktop>cd src
    C:\Users\Steve Lacy\Desktop\src>mkdir test
    C:\Users\Steve Lacy\Desktop\src>cd test
    C:\Users\Steve Lacy\Desktop\src\test>\Python27\Scripts\virtualenv --no-site-packages --distribute env

This will create an environment in src\\test\\env and populate it with
modified versions of Python, pip, etc.

You'll need to "activate" this environment to start using it.
 virtualenv puts in a simple activate script to help you do this, like
this:

    C:\Users\Steve Lacy\Desktop\src\test>env\Scripts\activate.bat
    (env) C:\Users\Steve Lacy\Desktop\src\test>

Note how your prompt changed to say that you're using development
enviroment "env" which we named above.

Now that our environment is "active" we have easy access to the special
versions of python and pip that have been placed in env/Scripts.
 They're now on your PATH, so you can use them directly.

Install Django using pip
------------------------

This is fairly easy now that we're in our environment and it's active:

    (env) C:\Users\Steve Lacy\Desktop\src\test>pip install django

Inspect the terminal output carefully to make sure that it successfully
installs each of these. Once that's complete, you should be good to go.

You can create a new Django project by running:

    (env) C:\Users\Steve Lacy\Desktop\src\test>python env\Scripts\django-admin.py

From here, your best bet is to continue to the [Django tutorial and
introductions](https://docs.djangoproject.com/en/1.3/intro/tutorial01/#creating-a-project)...
