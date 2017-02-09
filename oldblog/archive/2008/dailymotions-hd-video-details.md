Title: Dailymotion's HD video details.
Date: 2008-02-18 22:59
Author: slacy
Category: General
Tags: dailymotion, hd, on2, video, vp6
Status: published

[You may have seen a post that Dailymotion now supports HD
video.](http://feeds.feedburner.com/~r/Techcrunch/~3/237222571/)

I actually played that first 'racecar' clip, and was impressed at the
fullscreen quality, so I did some more digging and found some more about
the video.

First, here's a [direct
link](http://proxy-70.dailymotion.com/16/1280x720/on2/7366107.on2?542422e9d0fc8676892221122126a3b813215d0)
to the content itself. The URL alone implies a couple of things:

1\. It says that its 1280x720, which it actually is.  
2. It says that its an "on2" encoded file, which it actually is.  
3. It looks like there's some kind of encryption key there, so this URL
may not work for you. Let me know if you try it and it does.

After downloading the file, we can see that its 28MB in size. Here are
the interesting bits from "mplayer -identify":

> ID\_FILENAME=7366107.on2?542422e9d0fc8676892221122126a3b813215d0  
> ID\_DEMUXER=lavfpref  
> ID\_VIDEO\_FORMAT=VP6F  
> ID\_VIDEO\_BITRATE=0  
> ID\_VIDEO\_WIDTH=1280  
> ID\_VIDEO\_HEIGHT=720  
> ID\_VIDEO\_FPS=30.000  
> ID\_VIDEO\_ASPECT=0.0000  
> ID\_AUDIO\_FORMAT=85  
> ID\_AUDIO\_BITRATE=96000  
> ID\_AUDIO\_RATE=44100  
> ID\_AUDIO\_NCH=2  
> ID\_LENGTH=128.78  
> ID\_VIDEO\_CODEC=ffvp6f  
> Opening audio decoder: \[mp3lib\] MPEG layer-2, layer-3  
> AUDIO: 44100 Hz, 2 ch, s16le, 96.0 kbit/6.80% (ratio:
> 12000-&gt;176400)  
> ID\_AUDIO\_BITRATE=96000  
> ID\_AUDIO\_RATE=44100  
> ID\_AUDIO\_NCH=2

So, its 128.78 seconds long, and that gives us a total file bitrate of
1.76Mbps. We can see that its video format is "VP6F" which is On2's VP6
encoder. I'm not sure what the extra "F" is. This codec has roughly
equivalent quality to h.264. We can also see that they're using 96kbps
mp3 stereo encoded audio.
