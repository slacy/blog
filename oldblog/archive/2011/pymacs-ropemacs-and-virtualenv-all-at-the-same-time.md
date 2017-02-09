Title: pymacs, ropemacs, and virtualenv, all at the same time.
Date: 2011-03-04 17:15
Author: slacy
Category: General
Tags: emacs, pip, pymacs, python, refactoring, rope, ropemacs
Status: published

So, you're developing for Python, and you want to use rope and ropemacs
and pymacs, but it's totally busted when you use your virtualenv.

In addition, the packaged versions of pymacs+ropemacs for ubuntu 10.10
(and 11.04) are also kind of busted, because they complains with really
odd errors.

Here's the solution:

Install the latest, greatest versions of everything into your
virtualenv:

    . ./env/bin/activate
    pip install -e hg+https://bitbucket.org/agr/rope#egg=rope
    pip install -e hg+https://bitbucket.org/agr/ropemacs#egg=ropemacs
    pip install -e hg+https://bitbucket.org/agr/ropemode#egg=ropemode
    pip install -e git+https://github.com/pinard/Pymacs.git#egg=pymacs

Unfortunately, pymacs doesn't cleanly install, so then need to:

    cd env/src/pymacs
    make

Once that's done, you should have env/src/pymacs/pymacs.el. Great. Now
you just need to import that from your .emacs file. So, add something
that looks like this to your .emacs:

    (setq virtual-env (getenv "VIRTUAL_ENV"))

    (if (not (equal virtual-env 'nil))
          (setq load-path (append
                     (list (concat virtual-env "/src/pymacs" ))
                     load-path))
          (let ((foo 'bar))
          (require 'pymacs)
          (pymacs-load "ropemacs" "rope-")
          (setq ropemacs-enable-autoimport 't)
          ))

Activate your virtualenv, and run emacs from inside there, and you
should be good to go.
