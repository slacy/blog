Title: emacs, tramp, ido, dbus and avahi
Date: 2012-04-07 12:59
Author: slacy
Category: General
Status: published

Yeah, that's quite a cast of characters isn't it?

If you're using emacs, and inside emacs you use ido-mode, then it is, by
default, attempting to use "tramp completion" which, by default, is
using dbus, which, by default, uses avahi (i.e. zeroconf) to browse your
network for shares.

What this means is that if you use ido, and you're on a "big network"
(With lots of avahi/zeroconf/rendezvous hosts) then you'll see a
noticable slowdown in opening files. The solution is:

    M-x customize-group ido

and turn off ido-enable-tramp-completion

My .emacs.d/init.el has this line in the custom-set-variables section:

    '(ido-enable-tramp-completion nil)

Then, it won't use tramp, and it won't use dbus and it won't use avahi
and you'll be able to swiftly open files again. Whew!
