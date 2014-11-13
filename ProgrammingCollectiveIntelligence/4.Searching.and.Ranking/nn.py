# -*- encoding:utf-8 -*-

# artificial neural network
# Design of a Click-Tracking Network
# neurons,nultilayer perceptron,hidden layer,query layer

# Setting Up the Database

from math import tanh
from pysqlite2 import dbapi2 as sqlite


def dtanh(y):
    """
    Derivative of y = tanh(x)
    """
    return 1.0 - y * y


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

    def getallhiddenids(self, wordids, urlids):
        """
        Before running the feedforward algorithm,the class will have to
        query the nodes and connections in the database,and build,in
        memory,the portion of the network that is relevant to a specific
        query.
        """
        li = {}
        for wordid in wordids:
            cur = self.con.execute(
                'select toid from wordhidden where fromid=%d' % wordid)
            for row in cur:
                li[row[0]] = 1
        for urlid in urlids:
            cur = self.con.execute(
                'select fromid from hiddenurl where toid=%d' % urlid)
            for row in cur:
                li[row[0]] = 1
        return li.keys()

    def setupnetwork(self, wordids, urlids):
        """
        Construct the relevant neural network with all the current weights
        from the database.
        """
        # value lists
        self.wordids = wordids
        self.hiddenids = self.getallhiddenids(wordids, urlids)
        self.urlids = urlids

        # node outputs
        self.ai = [1.0] * len(self.wordids)
        self.ah = [1.0] * len(self.hiddenids)
        self.ao = [1.0] * len(self.urlids)

        # create weights matrix
        self.wi = [[self.getstrength(wordid, hiddenid, 0)
                    for hiddenid in self.hiddenids]
                   for wordid in self.wordids]
        self.wo = [[self.getstrength(hiddenid, urlid, 1)
                    for urlid in self.urlids]
                   for hiddenid in self.hiddenids]

    def feedforward(self):
        """
        Take a list of inputs,pushes them through the network,and
        returns the output of all the nodes in the output layer.
        Use tanh here as a sigmoid function.
        """
        # the only inputs are the query words
        # for i in range(len(self.wordids)):
            # self.ai[i] = 1.0

        # hidden activations
        for j in range(len(self.hiddenids)):
            sum = 0.0
            for i in range(len(self.wordids)):
                sum = sum + self.ai[i] * self.wi[i][j]
            self.ah[j] = tanh(sum)

        # output activations
        for k in range(len(self.urlids)):
            sum = 0.0
            for j in range(len(self.hiddenids)):
                sum = sum + self.ah[j] * self.wo[j][k]
            self.ao[k] = tanh(sum)

        return self.ao[:]

    def getresult(self, wordids, urlids):
        self.setupnetwork(wordids, urlids)
        return self.feedforward()

    def backProgapate(self, targets, N=0.5):
        """
        Run feedforward.
        Calculate ERROR vector using back propagation(multiply by
            weights matrix).
        Compute the GRADIENT vector of each layer using BP.
        Update the strength(weight matrix) in proportion to the links'
        current strength and the learning rate.
        """
        output_deltas = [0.0] * len(self.urlids)
        for k in range(len(self.urlids)):
            error = targets[k] - self.ao[k]
            # no need to multiply it by dtanh(self.ao[k])?
            output_deltas[k] = dtanh(self.ao[k]) * error

        # calculate errors for hidden layer
        hidden_deltas = [0.0] * len(self.hiddenids)
        for j in range(len(self.hiddenids)):
            error = 0.0
            for k in range(len(self.urlids)):
                # delta[k] = theta[k]' * delta[k+1] .* g'(octave vector)
                error = error + output_deltas[k] * self.wo[j][k]
            hidden_deltas[j] = dtanh(self.ah[j]) * error

        # update output weights
        for j in range(len(self.hiddenids)):
            for k in range(len(self.urlids)):
                # compute gradient.Gradient Descent algorithm
                change = output_deltas[k] * self.ah[j]
                self.wo[j][k] = self.wo[j][k] + N * change

        # update input weights
        for i in range(len(self.wordids)):
            for j in range(len(self.hiddenids)):
                change = hidden_deltas[j] * self.ai[i]
                self.wi[i][j] = self.wi[i][j] + N * change

    def trainquery(self, wordids, urlids, selectedurl):
        # generate a hidden node if necessary
        self.generatehiddennode(wordids, urlids)

        self.setupnetwork(wordids, urlids)
        self.feedforward()
        targets = [0.0] * len(urlids)
        targets[urlids.index(selectedurl)] = 1.0
        error = self.backProgapate(targets)
        self.updatedatabase()

    def updatedatabase(self):
        """
        save the results to the database
        """
        # set them to database values
        for i in range(len(self.wordids)):
            for j in range(len(self.hiddenids)):
                self.setstrength(self.wordids[i], self.hiddenids[j], 0,
                                 self.wi[i][j])
        for j in range(len(self.hiddenids)):
            for k in range(len(self.urlids)):
                self.setstrength(self.hiddenids[j], self.urlids[k], 1,
                                 self.wo[j][k])


if __name__ == "__main__":
    mynet = searchnet('nn.db')
    # mynet.maketables()

    wWorld, wRiver, wBank = 101, 102, 103
    uWorldBank, uRiver, uEarth = 201, 202, 203
    mynet.generatehiddennode([wWorld, wBank], [uWorldBank, uRiver, uEarth])
    # for c in mynet.con.execute('select * from wordhidden'):
        # print c
    # for c in mynet.con.execute('select * from hiddenurl'):
        # print c

    print mynet.getresult([wWorld, wBank], [uWorldBank, uRiver, uEarth])

    mynet.trainquery([wWorld, wBank], [uWorldBank, uRiver, uEarth], uWorldBank)
    print mynet.getresult([wWorld, wBank], [uWorldBank, uRiver, uEarth])
