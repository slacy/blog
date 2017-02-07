Title: Your flash cannot stop me.
Date: 2005-04-22 07:00
Author: slacy
Category: Music
Status: published

I was driving around this evening, listening to the radio, and heard a
couple really great songs. One was by DJ Shadow, and the other by RJD2.
DJ Shadow's website has a bunch (12) songs on it, but its all fronted by
a flash interface, so I couldn't (on first inspection) just download the
mp3 files. But, never fear, there is a solution to this problem: strace
firefox, and grep through the system calls looking for calls that told
me what the URLs of the mp3 files were, because they had to have been
requested from the flash interface. So, I did so, got a really really
big file, and did a simple grep:

<span style="font-family: courier new,courier,monospace;">\# fgrep mp3
/tmp/firefox.strace | fgrep send</span>  
<span style="font-family: courier new,courier,monospace;">\[pid 18483\]
send(42, "GET /trks/hardcore\_hip\_hop.mp3 HTTP/1.1  
Host: www.djshadow.com  
User-Agent: Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5)
Gecko/20041107 Firefox/1.0  
Accept:
text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,\*/\*;q=0.5  
Accept-Language: en-us,en;q=0.5  
Accept-Encoding: gzip,deflate  
Accept-Charset: ISO-8859-1,utf-8;q=0.7,\*;q=0.7  
Keep-Alive: 300  
Connection: keep-alive  
Range: bytes=2564112-  
If-Range: "604056-68201b-a0607a80"

", 478, 0) = 478</span>  
  
So, there you have it. The URL to one of the songs. Easy squeazy. I
clicked on each one, and got the URL, and then cut and pasted them right
here:

<http://djshadow.com/trks/disavowed.mp3>  
<http://djshadow.com/trks/hardcore_hip_hop.mp3>  
<http://djshadow.com/trks/marchofdeath.mp3>  
<http://djshadow.com/trks/mutual_slump.mp3>  
<http://djshadow.com/trks/red_bus_needs_to_leave.mp3>  
<http://djshadow.com/trks/shadows_legitimate_mix.mp3>  
<http://djshadow.com/trks/sixdays.mp3>  
<http://djshadow.com/trks/swan_lake.mp3>  
<http://djshadow.com/trks/the_number_song.mp3>  
<http://djshadow.com/trks/war_is_hell.mp3>  
<http://djshadow.com/trks/Instrumental3.mp3>  
<http://djshadow.com/trks/mashin_motorway.mp3>

Thanks, DJ Shadow!

RJD2 has a flash interface too, but it doesn't look like he has mp3
files. As far as I can tell, they're in some odd flash/mod file format,
and they're not real songs anyway.
[hiphopsite.com](http://hiphopsite.com/) appears to have some of the
songs in realplayer format, but thats always garbage. Maybe I'll get one
of his albums from amazon.com  
  

