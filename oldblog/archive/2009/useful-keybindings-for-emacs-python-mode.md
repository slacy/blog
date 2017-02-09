Title: Useful keybindings for emacs python-mode
Date: 2009-11-04 10:16
Author: slacy
Category: General
Tags: emacs, python
Status: published

I wrote up this keybinding the other day at work, and found that I
missed it when I went home, so I wrote it again from scratch.

It allows you easily indent or undent the current region using M-left
and M-right:

``` {.lisp name="code"}
(global-set-key [M-left] '(lambda () (interactive)
  (save-excursion
    (py-shift-region-left (region-beginning) (region-end)))))

(global-set-key [M-right] '(lambda () (interactive)
  (save-excursion
     (py-shift-region-right (region-beginning) (region-end)))))
```
