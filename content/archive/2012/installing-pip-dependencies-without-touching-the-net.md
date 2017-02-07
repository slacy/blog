Title: Installing pip dependencies without touching the 'net. 
Date: 2012-04-30 21:50
Author: slacy
Category: General
Status: published

@[jacobian just
tweeted](https://twitter.com/#!/jacobian/status/197194403985620993):

> A little shitty-wifi-inspired hack to make pip install not have to
> touch the 'net at
> all: [http://bit.ly/IRrRcn](http://t.co/IcQNA9ow "http://bit.ly/IRrRcn")

Yeah, been there, done that (using PIP\_DOWNLOAD\_CACHE).  It's a good
idea, but pip itself has better support for doing this.  I learned this
technique from the pip development team, specifically @carljm over IRC
and some bugs.

"pip install --no-install" first
--------------------------------

Use an "sdist cache" and not PIP\_DOWNLOAD\_CACHE.  An "sdist cache"
caches the actual distributed files, not the "pip-ified" files from
pypi.   Pick a directory to store these sdist files in.  From now on
out, I'm going to assume you're putting them in \$SDIST\_DIR, wherever
you decide that should be.

If you're adding a new dependency, and you want that dependency to be
able to be installed later without touching the 'net, you need to
download it first, and then install it from that download.  For example,
if I wanted to include Django, I'd do this:

    pip install --no-install --no-input --use-mirrors -I --download=$SDIST_DIR django

Which will put a file named something like Django-1.4.tar.gz (note the
nice filename!) into \$SDIST\_DIR.  You can then put \$SDIST\_DIR under
version control.

"pip install --find-links" second
---------------------------------

Then, you can install django (or any other dependency that you've
previously downloaded) without touching the 'net by executing:

    pip install -I --find-links=file://$SDIST_DIR --no-index --index-url=file:///dev/null django

Use requirements.txt, but not like they taught you
--------------------------------------------------

Unfortunately, this technique breaks "pip install -r requirements.txt".
 (I don't remember the exact details but I do remember it's broken)
 But, the format of requirements.txt is simple enough that you can
basically say:

    for dependency in $(cat requirements.txt); do
        pip install -I --find-links=file://$SDIST_DIR --no-index --index-url=file:///dev/null $dependency

Just put this into a shell script to make your life easier, which leads
us to...

Wrap it all up into a collection of shell scripts
-------------------------------------------------

Now that you know the general technique, you'll need to wrap these two
up into a couple different shell scripts.  Here's what I do (without
source -- but I'll share soon).

./add\_dependency.sh: Download a new single dependency, per the pip line
above, and then immediately install it.  This leaves a file in
\$SDIST\_DIR, but that's good, because it reminds me (via source
control) that I'm out of sync with what everyone else thinks the
dependencies are.

./download\_all\_dependencies.sh: Run "pip freeze" and download every
package currently installed into the current virtualenv.  This is good
because often times "pip install foo" will download several
dependencies, and the ./add\_dependency.sh script above doesn't properly
handle those cases.  I think this is a bug in pip.

./install.sh: Take "requirements.txt" and process it line-by-line
running the "install but don't download" commandline from above.

 
