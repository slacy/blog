Title: Getting all the wordpress.com themes on your local wordpress install.
Date: 2008-04-09 16:50
Author: slacy
Category: General
Status: published

So, you've got your own wordpress install, and you've got the 2 default
themes, but you want to stay up-to-date with all the themes that are
available to users of wordpress.com (their hosted solution)? I've got
the commandline for you!

> \# cd /to/the/place/that/you/installed/your/blog/wp-content/themes  
> \# svn co http://svn.automattic.com/wpcom-themes/ .  
> \# chown -R apache .  
> \# chgrp -R apache .

That will pull in all the themes that are available on hosted
wordpress.com blogs into your themes directory, making them available
for use.

If you want to update to the newest versions of these themes at some
later time, then you can issue an "svn update" to pull in any new or
changed files. Excellent!
