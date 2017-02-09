Title: Magic emacs bindings for dabbrev-expand and TAB indentation.
Date: 2011-11-10 10:41
Author: slacy
Category: General
Status: published

I use emacs for all my text editing.  When editing code, I also like to
use dabbrev-expand, but I find the default binding of C-M-/ really hard
to press and remember.  I'm used to TAB expanding everything.

But, I also want TAB to indent the current line according to the current
mode.  So, here's a best of both worlds solution:

    (defun virtual-beginning-of-line ()
      "Returns 't if there is nothing more than whitespace between
       point and the beginning of the line"
      (interactive)
      (let ((startpos (point))
            (matchpos 0)
            )
        (save-excursion
          (beginning-of-line)
          (setq matchpos (search-forward-regexp "[ \t]*" startpos 't))
          (if (<= startpos matchpos)
              't
            nil))))

    (defun virtual-end-of-line ()
      "Returns 't if there is nothing more than whitespace between
       point and the end of the line"
      (interactive)
      (let ((matchpos 0)
            (lep (line-end-position)))
        (save-excursion
          (setq matchpos (search-forward-regexp "[ \t]+" lep 't))
          (if matchpos
              (if (= matchpos lep)
                  't
                nil)
            't))))

    (defun smart-tab ()
      (interactive)
      (if (virtual-end-of-line)
          (delete-horizontal-space))
      (if (virtual-beginning-of-line)
          (c-indent-command)
        (if (virtual-end-of-line) (dabbrev-expand 'nil))))

Then, in any mode you'd like, just do something like this:

    (local-set-key [tab] 'smart-tab)
