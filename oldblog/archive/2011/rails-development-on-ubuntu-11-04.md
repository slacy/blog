Title: Rails development on Ubuntu 11.04
Date: 2011-09-27 14:46
Author: slacy
Category: General
Status: published

This post is just for collective notes on Rails development under Ubuntu
11.04:

-   **Use rvm**.  Really.  <http://beginrescueend.com/>
-   "**sudo apt-get install libreadline-dev ncurses-dev**" before you
    rvm install 1.9.2, otherwise you'll see weird issues when rails code
    says "require readline"  (rails console, for example)  If you had
    previously installed ruby via rvm, you'll need to "rvm remove ..."
    your currently installed version.  **rvm uninstall** is not enough!
-   **You'll need a JavaScript runtime**.  After generating your rails
    app, edit its Gemfile and add "gem '**therubyracer**'" to the end of
    it, and then run "bundle install" to install it.

