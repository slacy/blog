Title: Adding an Always launch a new terminal shortcut to Gnome Launcher
Date: 2014-10-10 12:43
Author: slacy
Category: General
Status: published

When using gnome3, the default Terminal launcher will just raise and
focus an existing terminal if there already is one.  I find this
behavior counter-intuitive.  I like to always create a new terminal.

To add this behavior, create a file in:

\~/.local/share/applications/newterm.desktop

With contents:

    #!/usr/bin/env xdg-open

    [Desktop Entry]
    Version=1.0
    Type=Application
    Terminal=false
    Icon[en_US]=gnome-terminal
    Name[en_US]=NewTerm
    Exec=gnome-terminal
    Comment[en_US]=Open a new terminal every time.
    Name=NewTerm
    Comment=Open a new terminal every time.
    Icon=gnome-terminal

Then, use Gnome's search feature to find "NewTerm" and add it to your
shortcuts.
