Title: Buffering problem with xmms & http & .m3u & ubuntu
Date: 2006-07-07 17:17
Author: slacy
Category: Linux Stuff, Music
Status: published

I upgraded one of the machines I use to the "Breezy Badger" ubuntu
release, and playback of mp3 files over http in xmms stopped working.

Well, it was still working, but the audio sounded horrible -- lots of
glitching and weird high pitched noises about 2 or 3 times a second.

The weird part was that I could fetch an .mp3 file directly and play it,
but if I used a PHP script that looked like this:

> &lt;?php  
> passthru("cat file.mp3");  
> ?&gt;

Then it wouldn't sound right. I fixed the problem my including the a
Content-Length header set to zero bytes, like this:

> &lt;?php  
> header("Content-Length: 0");  
> passthru("cat file.mp3");  
> ?&gt;

And now, once xmms starts playing the song, there is no glitching, but
it reports the duration of the song as being some totally bogus value,
like 17895:41 or 3579:08, which come up frequently. Clearly, this is a
bug in xmms since Content-Length: 0 isn't technically valid, and should
have the same behavior as no content length header at all, which is what
I had before.

None of my other systems have ever had this problem.
