Title: WiFi credentials in a QR code
Date: 2011-01-21 16:45
Author: slacy
Category: General
Status: published

It's possible to encode your WiFi credentials into a QR code.  [This
page on ZXIng's encoder lets you choose the right options and generate a
code that works on Android.](http://zxing.appspot.com/generator/) It
ends up linking to the Google Charts API page for the code, so it's
fairly easy to reverse engineer.  The unescaped Google Charts URL looks
like this:

    http://chart.apis.google.com/chart?cht=qr&chs=350x350&chl=WIFI:S:ssid_here;T:WEP;P:wep_password_here;;

Doing a little reverse engineering of the results gives us the following
string format:

    WIFI:S:<ssid>;T:<wep |WPA>;P:<password>;;

So, all you need to do is stuff that into the Google Charts API (per
above) and you get a code, that when scanned, allows you to easily
connect to your local WiFi network. Cool!

Here's an example code:
![](http://chart.apis.google.com/chart?cht=qr&chs=350x350&chl=WIFI:S:ssid_here;T:WEP;P:wep_password_here;;){.aligncenter
width="350" height="350"}
