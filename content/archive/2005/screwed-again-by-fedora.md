Title: Screwed again by Fedora
Date: 2005-04-26 02:45
Author: slacy
Category: Linux Stuff
Status: published

I'm beginning to think that the people on the Fedora Project are trying
to get server users (that is, non-desktop) of their distributions to
switch away.

They keep monkeying around with whats supported and whats not. In this
case, its imapd. In FC1 there was a vanilla imapd, it was replaced with
cyrus-imapd in FC2, persisted in FC3, and now they're replacing
cyrus-imapd with something called "dovecot" And, both times, they did
this with little warning or fanfare. No "Your mail server will no longer
work" messages. Nothing. Just an un-upgraded package that won't start up
anymore.

The problem here is that I have \*gigabytes\* of mail that need to be
converted over every time they decide to switch imap servers on a whim.

The other totally wacky part is that because FC4 is using gcc-4.0, I
can't even compile cyrus-imapd.

Nice job, Fedora Team.

Anyone have any good suggestions on what distro I should be running?
Debian? Mandrake? I'm sick of being jerked around by the Fedora team.

Oh, and by the way, they switched to PHP5, which pretty much screwed all
of my web apps as well. Thankfully, WordPress seems okay, otherwise you
wouldn't be reading this.
