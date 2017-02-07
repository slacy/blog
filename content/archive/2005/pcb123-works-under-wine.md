Title: PCB123 works under Wine
Date: 2005-04-22 07:00
Author: slacy
Category: Atmel AVR
Status: published

![](http://pcb123.com/images/new_index/logo.jpg)  
Well, I finally had success getting the PCB123 installer to run, and
after that, the program actually seems to work!  I haven't done any real
design using it yet, or ordered any boards, but I will in good time,
just be patient.  The secret is getting the latest Wine, and making sure
you force the installer into fullscreen mode, by doing something like
this in your \~/.wine/config file:  
  
<span style="font-family: courier new,courier,monospace;">; PCB123
installer</span>  
<span
style="font-family: courier new,courier,monospace;">\[AppDefaults\\pcb123.exe\\Version\]</span>  
<span style="font-family: courier new,courier,monospace;">"Windows" =
"win2k"</span>  
<span
style="font-family: courier new,courier,monospace;">\[AppDefaults\\pcb123.exe\\x11drv\]</span>  
<span style="font-family: courier new,courier,monospace;">"Desktop" =
"800x600"</span>

That should just about do it.  There was a special DLL that was missing
(a vbscript runtime thing?) but I google'd for it, found it on MS's
site, downloaded the installer, and it worked just fine after that. 
Good luck!  
  

