Title: Thoughts on running Linux from a Flash card.
Date: 2008-07-25 10:52
Author: slacy
Category: General
Status: published

When I was away on vacation last month, I realized that it would be
\*really\* great if I could have carried my computer with me on my
travels, but who wants to lug a whole computer through the Swiss Alps?!

I had previously heard about [Puppy Linux]() and [qemu-puppy]() which
are tailor-made linux distributions that come directly as a bootable ISO
image and can be put on a flash disk. This seemed like a great
compromise: Bring your whole 'computer' sans hardware, wherever you go.
qemu-puppy was of particular interest to me, because it could either be
booted directly from a USB disk, or it could be run in the qemu
emulator.

There are a lot of situations where re-booting just isn't possible.
Think about visiting an internet cafe: You don't want to be seen
rebooting their computer, changing the BIOS to be able to boot from USB,
and then rebooting into your own system. Never mind hotel lobbies, or
your friends desktop at home. Making these kinds of changes are just not
cool.

### Evaluating emulation

So, If rebooting isn't an option, then that leaves emulation. There are
several emulated or virtual environments available, so I took a look at
the 3 main options available. Here's my summary:

-   VMWare (Linux, Windows, Mac)
    -   Con: Requires administrator install. (This will be impossible in
        internet cafes, and rude on friends/family computers)
    -   Con: Uses proprietary image creation tools (Although some
        workarounds exist)
    -   Pro: Fast & fairly standard. May be pre installed in some
        locations?
    -   Con: No 'unaccellerated' (i.e. fully emulated) mode available.
-   Qemu (Linux, Windows, Mac)
    -   Con: Requires administrator install for accelleration
    -   Pro: Can run unaccellerated without administrator install, which
        is slow, but works.
    -   Pro: Player can be used without running an installer.
    -   Pro: Open source tools for image creation.
    -   Con: Because of limitations in qemu disk format and fat32, 4GB
        is the largest single disk that can be made.
    -   Pro: Supports both encrypted and sparse image formats.
    -   Pro: Available on Mac, Linux, Windows for free.
-   kvm (Linux-only)
    -   Pro: Just like qemu, except fully accellerated when available on
        Linux systems.
    -   Con: Would require an administrator install if not
        already present.

So, I began to focus in on building a system inside a qemu image, that
would run either accellerated when available (i.e. at home and work) and
that still had reasonable performance when running un-accellerated. So,
I began to download and install a variety of pre-packaged distributions,
and that also made me come up with my personal requirements, which I'll
include here first:

### System requirements

-   Must run in qemu, both accellerated (kqemu, kvm, etc.)
    and unaccellerated. Worst case boot time must still be 'reasonable'.
-   Must include some way to run X11 applications, including a fully
    fledged browser and windowing tools (Firefox 3.x, window manager,
    toolbar, terminal emulator, etc.)
-   Ideally would be based on a standard distribution, and easily
    upgradeable as new software arises
-   Must also include a reasonable set of commandline tools for doing
    terminal-only work when running unaccellerated (i.e. emacs, screen,
    and all the other 'regular' unix tools)
-   Must not boot directly into X11, and must not use an X11 login
    (gdm, etc.) screen. These are too heavyweight when booting
    unaccellerated
-   Must fit in a 4G image.
-   Must have a clean, uncluttered X11 interface

### The distributions

-   Puppy Linux & qemu-puppy
    -   Too ugly
    -   Has a graphical login screen
    -   Uses a non-standard web browser
    -   Uses a non-standard distribution, so hard to upgrade
-   DSL (Damn Small Linux)
    -   Boots \*really\* fast!
    -   Ugly
    -   Uses a non-standard web browser
    -   Uses a non-standard distribution, so hard to upgrade
    -   Lots of missing tools, and no 'apt-get' to install things (i.e.
        emacs)
-   ubuntulite
    -   Con: Has a weird install process with alternate repos
    -   Con: Still uses graphical login
    -   Pro: Mostly standard ubuntu
    -   Con: Not any better than a trimmed down ubuntu-jeos
-   xubuntu
    -   Con: Way too many services running for a small VM
    -   Con: Uses too much CPU when sitting "idle"
-   ubuntu-jeos
    -   Pro: Kernel built specifically for VMs
    -   Pro: Standard ubuntu otherwise (trimmed down base install)
    -   Con: No X11 or graphical UI at all (but easy to install!)
    -   Pro: Easy to install new packages, easy to upgrade.
    -   Pro: Installs as a 'real' fully fledged distro, not as a live CD
        or specially tailored distro.
    -   Con: Only Xorg server is available (no Xvesa, as far as I
        can tell).

So, I decided to start with ubuntu-jeos as my base, and to customize
from there. My biggest insight wast that I realized that I don't really
need to run a "physical" X11 server, I could just run a VNC server, and
export a graphical display that way. The VNC server is much lighter
weight than Xorg, its easy to start and stop on the commandline (no
complicated configs) and it makes the VNC viewer take the brunt of the
CPU needed to power the display. Some quick experiments showed that this
was all true!

My best case image is now:

-   Base ubuntu-jeos install
-   VNC server
-   emacs-nox
-   sshd

Which gives me all kinds of interesting options. The system boots up in
text mode, and from there, I can either:

-   Work strictly in the text UI, if I'm just doing something simple.
-   Start a VNC server and run programs inside that, if local X11
    isn't available.
-   If local X11 is available, then I can use ssh with X11 forwarding to
    run programs in the VM and have them displayed locally.

This is a really flexible setup! A 4GB flash drive is large enough to
hold the entire VM image, as well as some local tools, like Windows &
Mac SSH clients, VNC viewers, qemu emulator binaries, etc. So, on one
flash drive, I have a complete computer (sans hardware) and enough
support binaries in the emulators to run it pretty much any way I like,
with no install on the host computer necessary! Sweet!
