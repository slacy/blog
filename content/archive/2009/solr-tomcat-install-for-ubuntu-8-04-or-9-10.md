Title: Solr  Tomcat install for Ubuntu 8.04 or 9.10
Date: 2009-11-18 17:25
Author: slacy
Category: General
Tags: apache tomcat, lucene, solr, tomcat
Status: published

**<span style="color: #ff0000;">NOTE: THE VERSION OF SOLR PROVIDED BY
UBUNTU IS ONLY 1.2.  THIS VERSION IS OVER 2 YEARS OLD.</span>**

You can fairly easily install [tomcat](http://tomcat.apache.org/) &
[Solr](http://lucene.apache.org/solr/) for Ubuntu via apt-get, but there
are some quick caveats before you begin.  The packages are in the base
repositories, but something is messed up with the dependencies, so you
can't just say "sudo apt-get install solr-tomcat5.5" unless tomcat is
already installed.  So, the right sequence is:

    $ sudo apt-get install tomcat5.5
    $ sudo apt-get install solr-tomcat5.5

I'm a bit nervous that solr doesn't seem to work with (or rely on) newer
versions of tomcat, but I'm to to stressed at the moment.  Once you're
done with the above, you can check your Solr install at
<http://localhost:8180/solr/admin>

Solr config files live in /etc/solr/config/...
