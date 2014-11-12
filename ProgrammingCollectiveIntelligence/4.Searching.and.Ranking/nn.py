# -*- encoding:utf-8 -*-

# artificial neural network
# Design of a Click-Tracking Network
# neurons,nultilayer perceptron,hidden layer,query layer

# Setting Up the Database

from math import tanh
from pysqlite2 import dbapi2 as sqlite


class searchnet:

    def __init__(self, dbname):
        self.con = sqlite.connect(dbname)

    def __del__(self):
        self.con.close()

    def maketables(self):
        self.con.execute("create table hiddennode(create_key)")
        self.con.execute("create table wordhidden(fromid,toid,strength)")
        self.con.execute('create table hiddenurl(fromid,toid,strength)')
        self.con.commit()

    # determines the current strength of a connection
    def getstrength(self, fromid, toid, layer):
        if layer == 0:
            table = 'wordhidden'
        else:
            table = 'hiddenurl'
        res  = self.con.execute('select strength from %s \
                                where fromid=%d and toid=%d' %
                                (table, fromid, toid)).fetchone()
        if res == None:
            if layer == 0:
                return -0.2
            if layer == 1:
                return 0
        return res[0]

    # determine if a connection already exists and to update or create
    # the connection with the new strength
    def setstrength(self, fromid, toid, layer, strength):
        if layer == 0:
            table = 'wordhidden'
        else:
            table = 'hiddenurl'
        res = self.con.execute('select rowid from %s \
                               where fromid=%d and toid=%d' %
                               (table, fromid, toid)).fetchone()
        if res == None:
            self.con.execute("insert into %s (fromid,toid,strength) \
                             values(%d,%d,%f)" %
                             (table, fromid, toid, strength))
        else:
            rowid = res[0]
            self.con.execute('update %s set strength=%f \
                             where rowid=%d' %
                             (table, strength, rowid))

    # create a new node in the hidden layer every time it is passed a
    # combination of words that it has never seen together before
    def generatehiddennode(self, wordids, urls):
        if len(wordids) > 3:
            return None
        # Check if we already created a node for this set of words
        createkey = '_'.join(sorted([str(wi) for wi in wordids]))
        res = self.con.execute(
            "select rowid from hiddennode where \
            create_key='%s'" % createkey).fetchone()

        # If not,create it
        if res == None:
            cur = self.con.execute(
                "insert into hiddennode (create_key) values ('%s')" %
                createkey)
            hiddenid = cur.lastrowid
            # Put in some default weights
            for wordid in wordids:
                self.setstrength(wordid, hiddenid, 0, 1.0 / len(wordids))
            for urlid in urls:
                self.setstrength(hiddenid, urlid, 1, 0.1)
            self.con.commit()

if __name__ == "__main__":
    mynet = searchnet('nn.db')
    # mynet.maketables()
    wWorld, wRiver, wBank = 101, 102, 103
    uWorldBank, uRiver, uEarth = 201, 202, 203
    mynet.generatehiddennode([wWorld, wBank], [uWorldBank, uRiver, uEarth])
    for c in mynet.con.execute('select * from wordhidden'):
        print c
    for c in mynet.con.execute('select * from hiddenurl'):
        print c
