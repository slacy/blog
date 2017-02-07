Title: Twitterbots unite!
Date: 2011-03-10 00:01
Author: slacy
Category: General
Status: published

So, when you post a link to twitter, what happens?

Within a matter of seconds, you'll see traffic from at least all of the
following:

    50.18.61.103 - - [10/Mar/2011:07:46:15 +0000] "HEAD / HTTP/1.1" 404 221 "-" "UnwindFetchor/1.0 (+http://www.gnip.com/)"
    184.72.240.15 - - [10/Mar/2011:07:46:17 +0000] "HEAD / HTTP/1.1" 404 183 "-" "MetaURI API/2.0 +metauri.com"
    199.59.149.24 - - [10/Mar/2011:07:46:17 +0000] "HEAD / HTTP/1.1" 404 221 "-" "Twitterbot/0.1"
    67.195.115.120 - - [10/Mar/2011:07:46:18 +0000] "GET / HTTP/1.0" 200 4210 "-" "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)"
    38.113.234.181 - - [10/Mar/2011:07:46:18 +0000] "HEAD / HTTP/1.1" 404 164 "-" "Voyager/1.0"
    89.151.99.94 - - [10/Mar/2011:07:46:19 +0000] "GET / HTTP/1.1" 200 4191 "-" "Mozilla/5.0 (compatible; MSIE 6.0b; Windows NT 5.0) Gecko/2009011913 Firefox/3.0.6 TweetmemeBot"
    89.151.116.53 - - [10/Mar/2011:07:46:24 +0000] "GET / HTTP/1.1" 200 4191 "-" "Mozilla/5.0 (compatible; MSIE 6.0b; Windows NT 5.0) Gecko/2009011913 Firefox/3.0.6 TweetmemeBot"
    50.16.20.4 - - [10/Mar/2011:07:46:57 +0000] "HEAD / HTTP/1.1" 404 164 "-" "PycURL/7.18.2"
    204.236.254.109 - - [10/Mar/2011:07:47:10 +0000] "HEAD / HTTP/1.1" 404 164 "-" "PostRank/2.0 (postrank.com)"
    88.73.99.54 - - [10/Mar/2011:07:52:56 +0000] "HEAD / HTTP/1.1" 404 183 "-" "Twitmunin Crawler http://www.twitmunin.com"

And that's just the tip of the iceberg. I've filtered out many repeated
HEAD requests (which, BTW, I now know I need to properly implement for
these bots to be happy). And, over the next 10-30 minutes, I'll continue
to see more hits from other places as well (Baidu, etc.) Wow, amazing
how one simple action like posting a link in a tweet can generate so
much traffic.
