Title: Changing the Jenkins-CI port on Ubuntu
Date: 2012-02-07 10:43
Author: slacy
Category: General
Status: published

So, you've installed Jenkins on Ubuntu (following the directions on
their Wiki page) but you want it to listen on a different port (the
default is 8080).  I'm really, really surprised that there's not a
config file for this.  You have to edit /etc/init.d/jenkins.

Add the following two lines at the top of the file after DAEMON\_ARGS:

    HTTP_PORT=8888
    JENKINS_ARGS="--httpPort=$HTTP_PORT"
