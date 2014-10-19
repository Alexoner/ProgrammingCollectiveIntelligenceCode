# -*- encoding:utf-8 -*-
'''
Develop a way to collect documents:crawling

Indexing:database reference

Return a ranked list of documents from a query.

Build a neural network for ranking queries.

'''

import urllib2
from BeautifulSoup import *
from urlparse import urljoin
from pysqlite2 import dbapi2 as sqlite


# Create a list of words to ignore
ignorewords = set(['the', 'of', 'to', 'and', 'a', 'in', 'is', 'it'])


class crawler:
    # Initialize the crawler with the name of database

    def __init__(self, dbname):
        self.con = sqlite.connect(dbname)

    def __del__(self):
        self.con.close()

    def dbcommit(self):
        self.con.commit()

    # Auxilliary function for getting an entry id and adding
    # it if it's not present
    def getentryid(self, table, field, value, createnew=True):
        cur = self.con.execute(
            "select rowid from %s where %s='%s'" % (table, field, value))
        res = cur.fetchone()
        if res == None:
            cur = self.con.execute(
                "insert into %s (%s) values ('%s')" % (table, field, value))
            return cur.lastrowid
        else:
            return res[0]

    # Index an individual page
    def addtoindex(self, url, soup):
        if self.isindexed(url):
            return
        print 'Indexing ' + url

        # Get the individual words
        text = self.gettextonly(soup)
        words = self.separatewords(text)

        # Get the URL id
        urlid = self.getentryid('urllist', 'url', url)

        # Link each word to this url
        for i in range(len(words)):
            word = words[i]
            if word in ignorewords:
                continue
            wordid = self.getentryid('wordlist', 'word', word)
            self.con.execute("insert into wordlocation(urlid,wordid,location) \
                             values (%d,%d,%d)" % (urlid, wordid, i))

    # Extract the text from an HTML page (no tags)
    def gettextonly(self, soup):
        return None

    # Separate the words by any non-whitespace character
    def separatewords(self, text):
        return None

    # Return true this url is already indexed
    def isindexed(self, url):
        u = self.con.execute \
            ("select rowid from urllist where url='%s'" % url).fetchone()
        if u != None:
            # Check if it has actually been crawled
            v = self.con.execute(
                'select * from wordlocation where urlid=%d' % u[0]).fetchone()
            if v != None:
                return True
        return False

    # Add a link between two pages
    def addlinkref(self, urlFrom, urlTo, linkText):
        linkwords = self.separatewords(linkText)
        fromid = self.getentryid('urllist', 'url', urlFrom)
        toid = self.getentryid('urllist', 'url', urlTo)
        if fromid == toid:
            return
        cur = self.con.execute(
            "insert into link(fromid,toid) values(%d,%d)" % (fromid, toid))
        linkid = cur.lastrowid
        for word in linkwords:
            if word in ignorewords:
                continue
            wordid = self.getentryid('wordlist', 'word', word)
            self.con.execute(
                "insert into linkwords(linkid,wordid) values(%d,%d)" %
                (linkid, wordid))

    # Starting with a list of pages,do a breadth first search to the given
    # depth,indexing pages as we go
    def crawl(self, pages, depth=2):
        for i in range(depth):
            newpages = set()
            for page in pages:
                try:
                    c = urllib2.urlopen(page)
                except:
                    print "Could not open %s" % page
                    continue
                soup = BeautifulSoup(c.read())
                self.addtoindex(page, soup)

                links = soup('a')
                for link in links:
                    if ('href' in dict(link.attrs)):
                        url = urljoin(page, link['href'])
                        if url.find("'") != -1:
                            continue
                        url = url.split('#')[0]  # remove location portion
                        if url[0:4] == 'http' and not self.isindexed(url):
                            # print 'New url: %s' % url
                            newpages.add(url)
                        linkText = self.gettextonly(link)
                        self.addlinkref(page, url, linkText)

                self.dbcommit()

            pages = newpages
        pass

    # Create the database tables
    def createindextables(self):
        self.con.execute('create table urllist(url)')
        self.con.execute('create table wordlist(word)')
        self.con.execute('create table wordlocation(urlid,wordid,location)')
        self.con.execute('create table link(fromid integer,toid integer)')
        self.con.execute('create table linkwords(wordid,linkid)')
        self.con.execute('create index wordidx on wordlist(word)')
        self.con.execute('create index urlidx on urllist(url)')
        self.con.execute('create index wordurlidx on wordlocation(wordid)')
        self.con.execute('create index urltoidx on link(toid)')
        self.con.execute('create index urlfromidx on link(fromid)')
        self.dbcommit()

    def gettextonly(self, soup):
        v = soup.string
        if v == None:
            c = soup.contents
            resulttext = ''
            for t in c:
                subtext = self.gettextonly(t)
                resulttext += subtext + '\n'
            return resulttext
        else:
            return v.strip()

    # considers anything nonalphanumberic to be a separator,won't properly handle terms
    # link "C++".You can experience with regular expression to make it work
    # better.
    def separatewords(self, text):
        splitter = re.compile('\\W*')
        return [s.lower() for s in splitter.split(text) if s != '']

    # The PageRank Algorithm
    # The importance of the page is calculated form the importance of
    # all the other pages that link to it and from the number of links
    # each of the other pages has.
    # Implementation:initialization,iterate to get closer
    def calculatepagerank(self, iterations=20):
        # clear out the current PageRank tables
        self.con.execute('drop table if exists pagerank')
        self.con.execute('create table pagerank(urlid primary key,score real)')

        # initialize every url with a PageRank of 1
        self.con.execute('insert into pagerank select rowid,1.0 from urllist')
        self.dbcommit

        for i in range(iterations):
            print 'Iteration %d ' % (i)
            for (urlid,) in self.con.execute('select rowid from urllist'):
                pr = 0.15

                # Loop through all the pages that link to this one
                for (linker,) in self.con.execute(
                        'select distinct fromid from link where toid=%d' % urlid):
                    # Get the PageRank of the linker
                    linkingpr = self.con.execute(
                        'select score from pagerank where urlid=%d' %
                        linker).fetchone()[0]

                    # Get the total number of links from the linker
                    linkingcount = self.con.execute(
                        'select count(*) from link where fromid=%d' %
                        linker).fetchone()[0]
                    pr += 0.85 * (linkingpr / linkingcount)
                    # print(urlid, pr)
                print "update: %d,%f" % (urlid, pr)
                self.con.execute(
                    'update pagerank set score=%f where urlid=%d' %
                    (pr, urlid))
            self.dbcommit()


# set up the search part of the search engine
class searcher:

    def __init__(self, dbname):
        self.con = sqlite.connect(dbname)

    def __del__(self):
        self.con.close()

    # The wordlocation table gives us an easy way to link words to tables.
    # A query function that takes a query string,split it into separate
    # words,and construct a SQL query to find only those URLs containing
    # all the different words.
    # This function creates a reference to the wordlocation  table for
    # each word in the list and joining them all on their URL IDs.
    def getmatchrows(self, q):
        # Strings to build the query
        fieldlist = 'w0.urlid'
        tablelist = ''
        clauselist = ''
        wordids = []

        # Split the words by spaces
        words = q.split(' ')
        tablenumber = 0

        for word in words:
            # Get the word ID
            wordrow = self.con.execute(
                "select rowid from wordlist where word='%s'" % word).fetchone()
            if wordrow != None:
                wordid = wordrow[0]
                wordids.append(wordid)
                if tablenumber > 0:
                    tablelist += ','
                    clauselist += ' and '
                    clauselist += 'w%d.urlid=w%d.urlid and ' % (
                        tablenumber - 1, tablenumber)
                fieldlist += ',w%d.location' % tablenumber
                tablelist += 'wordlocation w%d' % tablenumber
                clauselist += 'w%d.wordid=%d' % (tablenumber, wordid)
                tablenumber += 1

        # Create the query from the sepratate parts
        fullquery = 'select %s from %s where %s' % (
            fieldlist, tablelist, clauselist)
        cur = self.con.execute(fullquery)
        rows = [row for row in cur]

        return rows, wordids

    # Content-Based Ranking
    #
    # Take a query,get the query result rows,put them in a dictionary,and
    # display them in a formatted list.
    def getscoredlist(self, rows, wordids):
        totalscores = dict([(row[0], 0) for row in rows])

        # This is scoring function
        weights = []
        # frequency
        # weights = [(1.0, self.frequencescore(rows))]
        # document location
        # weights = [(1.0, self.locationscore(rows))]
        #
        weights = [(1.0, self.frequencescore(rows)),
                   (1.5, self.locationscore(rows)),
                   (1.0, self.distancescore(rows)),
                   (1.0, self.pagerankscore(rows)),
                   (1.0, self.linktextscore(rows, wordids))]

        for (weight, scores) in weights:
            for url in totalscores:
                totalscores[url] += weight * scores[url]

        return totalscores

    def geturlname(self, id):
        return self.con.execute(
            "select url from urllist where rowid=%d" % id).fetchone()[0]

    def query(self, q):
        rows, wordids = self.getmatchrows(q)
        scores = self.getscoredlist(rows, wordids)
        rankedscores = sorted([(score, url)
                               for (url, score) in scores.items()],
                              reverse=1)

        for (score, urlid) in rankedscores[0:20]:
            print '%f\t%s' % (score, self.geturlname(urlid))

    # Normalized function
    # take a dictionary of IDs and scores and return a new dictionary
    # with the same IDs,but with the scores between 0 and 1.
    def normalizedscores(self, scores, smallIsBetter=0):
        vsmall = 0.00001  # Avoid division by zero errors
        if smallIsBetter:
            minscore = min(scores.values())
            return dict([(u, float(minscore) / max(vsmall, l))
                         for (u, l) in scores.items()])
        else:
            maxscore = max(scores.values())
            if maxscore == 0:
                maxscore = vsmall
            return dict([(u, float(c) / maxscore)
                         for (u, c) in scores.items()])

    # Metric:
    # Word Frequency,Documentation Location,Word Distance
    # The word frequency metric scores a page based on how many times
    # the words in the query appear on that page.
    def frequencescore(self, rows):
        counts = dict([(row[0], 0)for row in rows])
        for row in rows:
            counts[row[0]] += 1
        return self.normalizedscores(counts)

    # metric about search term's location in the page
    # Usually,if a page is relevant to the search term,it will appear
    # closer to the top of the page,perhaps even in the title.
    # Remember that the first item in earch row elements is the URL ID,
    # followed by the locations of all the different search terms.Each
    # ID can appear multiple times,once for every combination of
    # locations.
    def locationscore(self, rows):
        locations = dict([(row[0], 1000000) for row in rows])
        for row in rows:
            loc = sum(row[1:])
            if loc < locations[row[0]]:
                locations[row[0]] = loc

        return self.normalizedscores(locations, smallIsBetter=1)

    # Word Distance Metric
    # When a query contains multiple words,it is often useful to seek
    # results in which the words in the query are close to each other in
    # the page
    def distancescore(self, rows):
        # If there's only one word,everyone wins!
        if len(rows[0]) <= 2:
            return dict([(row[0], 1.0)
                         for row in rows])

        # Initialize the dictionary with large values
        mindistance = dict([(row[0], 1000000)
                            for row in rows])

        for row in rows:
            dist = sum([abs(row[i] - row[i - 1])
                        for i in range(2, len(row))])
            if dist < mindistance[row[0]]:
                mindistance[row[0]] = dist

        return self.normalizedscores(mindistance, smallIsBetter=1)

    # Using Inbound Links
    # Scoring Metrics: content-based,inbound links analysis

    # Simple count
    def inboundlinkscore(self, rows):
        uniqueurls = set([row[0] for row in rows])
        inboundcount = dict([(u, self.con.execute(
                              "select count(*) from link where toid=%d" % u).fetchone()[0])
                             for u in uniqueurls])
        return self.normalizedscores(inboundcount)

    # pagerank score
    def pagerankscore(self, rows):
        pageranks = dict([(row[0], self.con.execute(
            'select score from pagerank where urlid=%d' %
            row[0]).fetchone()[0]) for row in rows])
        maxrank = max(pageranks.values())
        normalizedscores = dict([(u, float(l) / maxrank)
                                 for (u, l) in pageranks.items()])
        return normalizedscores

    # Using the Link Text
    # Use the text of the links to a page to decide how relevant the page
    # is.
    # @rows: query result rows
    # @wordids:IDs of query words
    # @return link text scores
    def linktextscore(self, rows, wordids):
        linkscores = dict([(row[0], 0) for row in rows])
        for wordid in wordids:
            cur = self.con.execute('select link.fromid,link.toid from \
                                   linkwords,link where wordid=\
                                %d and linkwords.linkid=link.rowid' %
                                   wordid)
            for (fromid, toid) in cur:
                if toid in linkscores:
                    pr = self.con.execute(
                        'select score from pagerank \
                        where urlid=%d' % fromid).fetchone()[0]
                    linkscores[toid] += pr
        maxscore = max(linkscores.values())
        maxscore = max(maxscore, 0.0000001)
        normalizedscores = dict([(u, float(l) / maxscore)
                                 for (u, l) in linkscores.items()])
        return normalizedscores

if __name__ == "__main__":
    pagelist = ['http://www.geeksforgeeks.org', 'http://leetcode.com']
    # pagelist = ['http://leetcode.com']
    crawler = crawler('searchindex.db')
    # crawler.createindextables()
    # crawler.crawl(pagelist, 3)
    # crawler.calculatepagerank()

    e = searcher('searchindex.db')
    # print e.getmatchrows('dynamic programming')
    e.query('dynamic programming')
    # e.query('graph algorithms')
    # e.query('longest increasing subsequence')
    e.query('optimal substructure')
