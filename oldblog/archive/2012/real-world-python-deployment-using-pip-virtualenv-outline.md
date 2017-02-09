Title: Real-world Python deployment using pip  virtualenv. (Outline)
Date: 2012-08-27 10:14
Author: slacy
Category: General
Status: published

Real-world Python deployment. (Outline/notes)
---------------------------------------------

### Introduction

You've got a great development setup and now you want to "do the right
thing" in production.

You're using virtualenv (good!)

You're using "pip install..." for all your dependencies (good!)

You're probably not keeping a requirements.txt up to date (that's OK!)

You're using "django-admin.py runserver" or similar (not gonna cut it!)

You've got all your source code in a git repo (self hosted or github or
other, good!)

You're ready to write your first fabric script! (good!)

Now let's get that code out to production!

### Goals

1.  Deploy a git repository to production.
2.  Let's not use eggs for our own source.
    1.  This is a debatable point, but for specific use cases like
        deploying a Django application, building and maintaining eggs is
        harder than it should be (mainly because of static resources)
    2.  Deploying from a source directory is actually
        more straightforward.
    3.  We'll still use "python ./setup.py install" for our own code.

3.  Use virtualenv for environment management.
4.  Use pip to install dependencies.
5.  Reproducible deployment.
6.  No external network dependencies.
7.  Fast-ish deployment & dependency installation.
8.  Match development & production environments as closely as possible.

### Pitfalls

1.  Think about security for just a couple seconds.
    1.  ssh keys in production?
    2.  Could an attacker gain access to your git repository?

2.  "pip install" is a heavyweight process.
    1.  Goes out to pypi.python.org and fetches metadata.
    2.  Fetches each package from it's own home hosting provider.
    3.  These hosts go down.  Do you want YOUR deployment to depend on
        their servers being up?

3.  Cut your external network access and see what happens.
    1.  Imagine if outbound network access from production
        was disallowed.  Could you still deploy?

4.  How do I rollback?
5.  How do I manage my system configuration
    1.  apache configs
    2.  nginx configs
    3.  gunicorn
    4.  crontabs
    5.  init scripts (start/stop, etc)
    6.  supervisord configs

### Solutions

1.  Security & key management
    1.  Never ssh from production to anywhere.  Only ssh
        into production.
    2.  Production machines should never have private keypairs.
         (authorized\_keys is OK)

2.   git access in production
    1.  Use the "push-pull" strategy.
    2.  Your development machine does "git push" into a bare git repo in
        production
    3.  Production machine then turns around and does "git pull" from
        it's own local repository.
    4.  Or, build some eggs. (This has its own issues that I won't
        cover here)
    5.  You can modify code in production, and commit it, but it won't
        make it back to your repository unless you "git pull" from
        that repo.  This is a good thing.  Manage
        production customization in a reproducible way.

3.  users
    1.  don't deploy as root

4.  virtualanv & pip
    1.  virtualenv is great!
    2.  don't rely on system packages!
    3.  Make a new virtualenv every time you deploy!
    4.  never run "sudo virtualenv..."
    5.  never run "sudo pip..."
    6.  PIP\_DOWNLOAD\_CACHE is NOT your friend.
        1.  why with examples

    7.  Solution: Separate "install this package" from "download this
        package"
        1.  Step 1: pip install --no-install --use-mirrors -I
            --download=\$CACHE\_DIR ...
        2.  Step 2: pip install --no-index
            --index-url=file:///dev/null ...

    8.  Use some helper scripts to make this easier. (github link TBD)
    9.  You're still screwed sometimes.
        1.  outline when TBD

    10. Automatic dependency downloads can still bite you
    11. Periodically re-download everything
        1.  This makes sure that if dependencies change

    12. Managing package upgrades.
        1.  When you want to upgrade, re-download the package and you'll
            pick up the latest version.
        2.  modify requirements.txt

5.  Managing your system configurations
    1.  In principle: Make a "mock /etc" in your repo
    2.  Copy "mock /etc" on top of the "system /etc" to install.
        (using fabric)
    3.  A couple other commands to enable system services (a2ensite, and
        friends, etc.)
    4.  supervisord, but it's outside the scope of this talk
        1.  system supervisord or a self-installed supervisord?
        2.  How to start up supervisord?
        3.  web interface to production or not?


