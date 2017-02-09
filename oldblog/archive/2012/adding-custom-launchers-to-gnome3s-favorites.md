Title: Adding custom launchers to Gnome3's Favorites. 
Date: 2012-06-04 13:31
Author: slacy
Category: General
Status: published

This is totally non-obvious, so here goes.

At a shell prompt, run:

\$ gnome-desktop-item-edit
\~/.local/share/applications/mylauncher.desktop --create-new

Go through the dialog to create the launcher and make sure you give it
an easy to remember name.  When you're done, that application should
show up under "Applications" in that search thing.
