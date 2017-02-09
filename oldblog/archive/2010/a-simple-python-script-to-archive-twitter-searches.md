Title: A simple Python script to archive Twitter searches. 
Date: 2010-06-04 08:43
Author: slacy
Category: General
Tags: python, script, twitter, twitter archive, twython
Status: published

Using the [twython](http://github.com/ryanmcgrath/twython) library, I've
written this excruciatingly simple script to archive the results of any
twitter search.  It just pickles the search results and writes them to a
file with the current date & time.  I've put this in my crontab and run
it on a regular interval, and I'll do the post-processing later.   There
are likely much better possible implementations of this (sqlite database
for archive?) but this one is dirt simple and preserves 100% of what I
got from the Twitter API, which will likely have some advantage.  This
is based on the twython "search\_results.py" example. Here ya go:

    import pickle
    import twython.core as twython
    import datetime
    import pprint

    search = "PUT YOUR SEARCH TERM HERE"

    filename = (datetime.datetime.now().strftime("%Y%m%d_%H:%M:%S") + ".pkl")

    twitter = twython.setup()

    all_results = []

    for page in range(1,10):
        search_results = twitter.searchTwitter(search, rpp=15, page=page)
        if not search_results['results']:
            break
        all_results.append(search_results)

    if all_results:
        output = open(filename, "w+")
        pickle.dump(all_results, output)
        # pprint.pprint(all_results)
        output.close()
        print "Saved results to " + filename
    else:
        print "No search results for " + search

I think the twitter API allows 150 requests per HOUR, so don't run this
too frequently. For big searches, this could issue 10 calls (for up to
10 pages of results, 15 tweets per page). So, you probably don't want to
run it any more frequently than 5 minutes, which would result in a
maximum of 120 requests per hour. I've heard that if you put in an HTTP
Referrer into the request, that you get a higher limit, but that's not
really that important to me. I tried setting rpp (responses per page) to
a higher value, but that had no effect, so I stuck with what twitter was
returning, which was 15.
