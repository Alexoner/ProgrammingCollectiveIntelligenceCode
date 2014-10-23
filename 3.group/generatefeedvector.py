# Counting the words in a Feed

import feedparser
import re
import urllib2

# Returns title and dictionary of word counts for an RSS feed

# proxy = urllib2.ProxyHandler({"http": "http://127.0.0.1:8087/"})


def getwordcounts(url):
    # Parse the feed
    # d = feedparser.parse(url, handlers=[proxy])
    d = feedparser.parse(url)
    wc = {}

    print d.feed.title
    # Loop over all the entries
    for e in d.entries:
        if 'summary' in e:
            summary = e.summary
        else:
            summary = e.description

        # Extract a list of words
        words = getwords(e.title + ' ' + summary)
        for word in words:
            wc.setdefault(word, 0)
            wc[word] += 1

    return d.feed.title, wc

# strips out all of the HTML and splits the words by nonalphabetical
# characters,returning them as a list.


def getwords(html):
    # Remove all the HTML tags
    txt = re.compile(r'<[^>]+>').sub('', html)

    # split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower() for word in words if word != '']

if __name__ == "__main__":
    # generates the word counts for each blog,as well as the number of
    # blogs each word appeared in (apcount).
    apcount = {}
    wordcounts = {}
    feedlist = [line for line in file('feedlist.txt')]
    for feedurl in file('feedlist.txt'):
        try:
            title, wc = getwordcounts(feedurl)
            wordcounts[title] = wc
            for word, count in wc.items():
                apcount.setdefault(word, 0)
                if count > 1:
                    apcount[word] += 1
        except:
            print "Failed to parse feed %s" % (feedurl)

    # generate the list of words that will actually be used in counts for
    # each blog.Start with 10 percents as the lower bound and 50 percents
    # as the upper bound.
    wordlist = []
    for w, bc in apcount.items():
        frac = float(bc) / len(feedlist)
        if frac > 0.1 and frac < 0.5:
            wordlist.append(w)

    # use the list of words and the list of blogs to create a text file
    # containing a big matrix of all the words counts for each of the
    # blogs
    out = file('blogdata.txt', 'w')
    out.write('Blog')
    for word in wordlist:
        out.write('\t%s' % word)
    out.write('\n')
    for blog, wc in wordcounts.items():
        out.write(blog)
        for word in wordlist:
            if word in wc:
                out.write('\t%d' % wc[word])
            else:
                out.write('\t0')
        out.write('\n')
