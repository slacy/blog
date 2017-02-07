Title: Making pep8, pyflakes, etc work with virtualenv.
Date: 2011-03-02 15:41
Author: slacy
Category: General
Status: published

Unfortunately, the pre-built binaries for the Python pep8 checker and
pyflakes both point directly at \#!/usr/bin/python. (FYI I have at least
one git pull request out to fix this).

This means that if you're using virtualenv, they'll complain about a ton
of missing packages when you actually just have them in your virtualenv
environment.

Since these "binaries" are just simple wrappers, it's fairly easy to
replace them with local copies. I've always put \~/bin early in my PATH
so that I can override things like this. So, I just created \~/bin/pep8
and \~/bin/pyflakes that each look like this:

pep8:

    #!/usr/bin/env python
    # EASY-INSTALL-ENTRY-SCRIPT: 'pep8==0.5.0','console_scripts','pep8'
    __requires__ = 'pep8==0.5.0'
    import sys
    from pkg_resources import load_entry_point

    if __name__ == '__main__':
        sys.exit(
            load_entry_point('pep8==0.5.0', 'console_scripts', 'pep8')()
        )

pyflakes:

    #!/usr/bin/env python

    import sys
    from pyflakes.scripts.pyflakes import main
    sys.exit(main(sys.argv[1:]))

And this is why you wan to always say \#!/usr/bin/env python instead of
\#!/usr/bin/python.
