Title: Why is bit.ly compelled to display short links in Flash?
Date: 2010-07-02 14:59
Author: slacy
Category: General
Status: published

I noticed a change to bit.ly a few weeks (months?) ago where instead of
letting you select & copy the shortened link yourself, they have this
cute little "click to copy" button.

Well, today I tried to use it, and I clicked, and it said it was on my
clipboard, but when I pasted, I got some previous junk from my
clipboard. So I tried again. And again. And again.

It didn't work. So, I tried to mouse-select the link. It didn't work. I
tried again, and it still didn't work.

I ran Chrome, and I right clicked on the short link, expecting to see
"Inspect Element" and view the source of that element. I got nothing.

I turned on developer tools, reloaded the page, clicked on "Elements"
and found the element that contained the short link, hoping to be able
to pull it out of the HTML. Here's what I saw:

    <embed id="ZeroClipboardMovie_1" src="/s/flash/zeroclipboard/ZeroClipboard.swf"
    loop="false" menu="false" quality="best" bgcolor="#ffffff" width="260" height="30"
    name="ZeroClipboardMovie_1" align="middle" allowscriptaccess="always"
    allowfullscreen="false" type="application/x-shockwave-flash"
    pluginspage="http://www.macromedia.com/go/getflashplayer"
    flashvars="id=1&width=260&height=30" wmode="transparent">

This is **NOT OK**. What reasonable reason do they have for displaying
shortened links *in flash!*

Dear bit.ly,

I am never going to use your service to shorten links again.  If there
were a way for me to not click on bit.ly links, I would.

Sincerely,

A reasonably-minded web developer.
