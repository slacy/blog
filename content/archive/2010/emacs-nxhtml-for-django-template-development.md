Title: emacs + nxhtml for Django template development
Date: 2010-10-04 21:12
Author: slacy
Category: General
Status: published

nxhtml mode is really awesome for editing Django template files.  It
includes a mode called mumamo (MUltiple MAjor MOde) that allows
different sections of a file to be run in different modes.  This means
that your inlined JavaScript will be properly highlighted and indented!
 WOOT!

On my Ubuntu 10.04 Lucid system, the install is fairly straightforward.
 There are 2 requirements:

1.  nxhtml.zip from
    ﻿<http://ourcomments.org/cgi-bin/emacsw32-dl-latest.pl>
2.  js2-mode.  Install via "sudo apt-get install js2-mode"

Once you've done that, unzip nxhtml.zip and put it in \~/el, and add the
following to your .emacs:

    (require 'js2-mode)
    (load "~/el/nxhtml/autostart.el")
    (setq mumamo-background-colors nil)
    (add-to-list 'auto-mode-alist '("\\.html$" . django-html-mumamo.-mode))
