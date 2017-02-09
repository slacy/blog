Title: flymake for emacs + Python 
Date: 2009-11-06 09:46
Author: slacy
Category: General
Tags: emacs, pep8, pylint, python, syntax
Status: published

flymake is an emacs mode that lets you "compile" (or syntax check) your
code on the fly. For Python, this means that you can run several syntax
checkers, like pep8 or pylint, or pyflakes (or all of the above) while
you're editing your code in realtime. To get this set up in emacs, do
the following:

Create \~/bin/pychecker, which will be a simple script calling all your
checkers.

    #!/bin/bash
    pylint --output-format=parseable "$1"
    pyflakes "$1"
    pep8 --repeat "$1"
    true

Second, edit your .emacs and set up flymake to call this script for
python files, and add some useful keyboard shortcuts for jumping between
errors & warnings:

    (require 'flymake)
    (defun flymake-pylint-init ()
     (let* ((temp-file (flymake-init-create-temp-buffer-copy
                        'flymake-create-temp-inplace))
            (local-file (file-relative-name
                         temp-file
                         (file-name-directory buffer-file-name))))
       (list "~/bin/pychecker" (list local-file))))

    (add-to-list 'flymake-allowed-file-name-masks
                 '("\\.py\\'" flymake-pylint-init))

    (defun my-python-mode-hook ()
     (interactive)
     (flymake-mode)
     (local-set-key [S-up]
                    (lambda ()
                      (interactive)
                      (flymake-goto-prev-error)
                      (message "%s"
                        (flymake-ler-text (caar (flymake-find-err-info
                        flymake-err-info
                        (flymake-current-line-no)))))))
     (local-set-key [S-down]
                    (lambda ()
                      (interactive)
                      (flymake-goto-next-error)
                      (message "%s"
                        (flymake-ler-text (caar (flymake-find-err-info
                        flymake-err-info
                        (flymake-current-line-no)))))))
    )
    (add-hook 'python-mode-hook 'my-python-mode-hook)
