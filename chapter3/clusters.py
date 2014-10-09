# Hierarchical clustering

# load file


def readfile(filename):
    lines = [line for line in file(filename)]

    # First line is the column titles
    colnames = lines[0].strip().split('\t')[1:]
    rownames = []
    data = []
    for line in lines[1:]:
        p = line.strip().split('\t')
        # First column in each row is the rowname
        rownames.append(p[0])
        # The data for this row is the ramainder of the row
        data.append([float(x) for x in p[1:]])

    return rownames, colnames, data

# define closeness
# Pearson correlation coefficient
from math import sqrt


# The final line is to create a smaller distance between items that are
# more similar
def pearson(v1, v2):
    # Simple sums
    sum1 = sum(v1)
    sum2 = sum(v2)

    # Sums of the squares
    sum1sq = sum([pow(v, 2) for v in v1])
    sum2sq = sum([pow(v, 2) for v in v2])

    # Sum of the products
    pSum = sum([v1[i] * v2[i] for i in xrange(len(v1))])

    # Calculate r (Pearson score)
    num = pSum - (sum1 * sum2) / len(v1)
    den = sqrt((sum1sq - pow(sum1, 2) / len(v1))
               * (sum2sq - pow(sum2, 2) / len(v1)))
    if den == 0:
        return 0

    return 1.0 - num / den

# Each cluster in a hierarchical clustering algorithm is either a point in
# the tree with two branches, or an endpoint associated with an actual row
# from the dataset (in this case, a blog).
# Each cluster also contains data about its location,which is either the
# row data for the endpoints or the merged data from its two branches for
# other node types.


class bicluster:

    def __init__(self, vec, left=None, right=None, distance=0.0, id=None):
        self.left = left
        self.right = right
        self.vec = vec
        self.id = id
        self.distance = distance

# Initialization: for hierarchical clustering, creating a group of
#   clusters that are just the original items.
# Maintenance: search for two best matches by trying every possible pair
# and calculating their correlation.The best pari of clusters are merged
# into a single cluster.The data for this new cluster is the average of
# data for two old clusters.
# Termination:only one cluster remains


def hcluster(rows, distance=pearson):
    distances = {}
    currentclustid = -1

    # Clusters are initially just the rows
    clust = [bicluster(rows[i], id=i) for i in xrange(len(rows))]

    while len(clust) > 1:
        lowestpair = (0, 1)
        closest = distance(clust[0].vec, clust[1].vec)

        # loop through every pair looking for the smallest distance
        for i in xrange(len(clust)):
            for j in xrange(i + 1, len(clust)):
                # distance is the cache of distance calculations
                if (clust[i].id, clust[j].id) not in distances:
                    distances[(clust[i].id, clust[j].id)] = distance(
                        clust[i].vec, clust[j].vec)

                d = distances[(clust[i].id, clust[j].id)]

                if d < closest:
                    closest = d
                    lowestpair = (i, j)

        # calculate the average of the two clusters
        mergevec = [(clust[lowestpair[0]].vec[i] +
                     clust[lowestpair[1]].vec[i]) / 2.0
                    for i in xrange(len(clust[0].vec))]

        # create the new cluster
        newcluster = bicluster(mergevec, left=clust[lowestpair[0]],
                               right=clust[lowestpair[1]],
                               distance=closest,
                               id=currentclustid)

        # cluster ids that weren't in the original set are negative
        currentclustid = -1
        del clust[lowestpair[1]]
        del clust[lowestpair[0]]
        clust.append(newcluster)

    return clust[0]


def printclust(clust, labels=None, n=0):
    # indent to make a hierarchy layout
    for i in xrange(n):
        print ' ',
    if clust.id < 0:
        # negative id means that this is branch
        print '-'
    else:
        # positive id means that this is an endpoint
        if labels == None:
            print clust.id
        else:
            print labels[clust.id]

    # now print the right and left branches
    if clust.left != None:
            printclust(clust.left, labels=labels, n=n + 1)
    if clust.right != None:
            printclust(clust.right, labels=labels, n=n + 1)

# Drawing the dendromgram
# interpret the clusters more clearly by viewing them as a dendrogram.

# determine the overall height of the image
try:
    from PIL import Image, ImageDraw

    def getheight(clust):
        # Is this an endpoint? Then the height is just 1
        if clust.left == None and clust.right == None:
            return 1

        # Otherwise the height is the same of the heights of each branch
        return getheight(clust.left) + getheight(clust.right)

    def getdepth(clust):
        # The distance of an endpoint is 0.0
        if clust.left == None and clust.right == None:
            return 0

        # The distance of a branch is the greater of its two sides
        # plus its own distance
        return max(getdepth(clust.left), getdepth(clust.right)) + clust.distance

    # the drawdendrogram function creates a new image allowing 20 pixels
    # in heights and a fixed width for each final cluster.The scaling
    # factor is determined by dividing the fixed width by the total depth.
    # scaling factor
    def drawdendrogram(clust, labels, jpeg='clusters.jpg'):
        # height and width
        h = getheight(clust) * 20
        w = 1200
        depth = getdepth(clust)

        # Width is fixed,so scale distances accordingly
        scaling = float(w - 150) / depth

        # Create a new image with a white background
        img = Image.new('RGB', (w, h), (255, 255, 255))
        draw = ImageDraw.Draw(img)

        draw.line((0, h / 2, 10, h / 2), fill=(255, 0, 0))

        # Draw the first node
        drawnode(draw, clust, 10, (h / 2), scaling, labels)
        img.save(jpeg, 'JPEG')

    def drawnode(draw, clust, x, y, scaling, labels):
        if clust.id < 0:
            h1 = getheight(clust.left) * 20
            h2 = getheight(clust.right) * 20
            top = y - (h1 + h2) / 2
            bottom = y + (h1 + h2) / 2
            # Line length
            ll = clust.distance * scaling
            # Vertical line from this cluster to children
            draw.line((x, top + h1 / 2, x, bottom - h2 / 2),
                      fill=(255, 0, 0))

            # Horizontal line to left item
            draw.line(
                (x, top + h1 / 2, x + ll, top + h1 / 2), fill=(255, 0, 0))

            # Horizontal line to right item
            draw.line((x, bottom - h2 / 2, x + ll, bottom - h2 / 2),
                      fill=(255, 0, 0))

            # Call the function to draw the left and right nodes
            drawnode(draw, clust.left, x + ll, top + h1 / 2, scaling, labels)
            drawnode(draw, clust.right, x + ll,
                     bottom - h2 / 2, scaling, labels)
        else:
            # If this is an endpoint,draw the item label
            draw.text((x + 5, y - 7), labels[clust.id], (0, 0, 0))

except:
    print "Python Imaging Library not found"

# Column clustering
# rotate the entire dataset so that columns become rows,each with a list
# of numbers indicating how many times that particular word appear in each
# of the blogs


def rotatematrix(data):
    newdata = []
    for i in xrange(len(data[0])):
        newrow = [data[j][i] for j in xrange(len(data))]
        newdata.append(newrow)

    return newdata

# K-Means Clustering
# Initialization:randomly place k centroids,and assigns every item to the
# nearest one.
# Maintenance: move the centroids to the average location of all the nodes
# assigned to them,and the assignments are redone.
# Termination:the assignments stop changing.
import random


def kcluster(rows, distance=pearson, k=4):
    # Determine the minimum and maximum values for each input
    ranges = [(min([row[i] for row in rows]),
               max([row[i] for row in rows]))
              for i in xrange(len(rows[0]))]

    # Create k randomly placed centroids
    clusters = [[random.random() * (ranges[i][1] - ranges[i][0]) +
                 ranges[i][0]
                 for i in xrange(len(rows[0]))] for j in xrange(k)]

    lastmatches = None
    for t in xrange(100):
        print 'Iteration %d' % t
        bestmatches = [[] for t in xrange(k)]

        # Find which centroid is the closest for each row
        for j in range(len(rows)):
            row = rows[j]
            bestmatch = 0
            for i in range(k):
                d = distance(clusters[i], row)
                if d < distance(clusters[bestmatch], row):
                    bestmatch = i
            bestmatches[bestmatch].append(j)

        # if the results are the same as last time,this is complete
        if bestmatches == lastmatches:
            break
        lastmatches = bestmatches

        # Move the centroids to the average of their members
        for i in xrange(k):
            avgs = [0.0] * len(rows[0])
            if len(bestmatches[i]) > 0:
                for rowid in bestmatches[i]:
                    for m in xrange(len(rows[rowid])):
                        avgs[m] += rows[rowid][m]
                for j in xrange(len(avgs)):
                    avgs[j] /= len(bestmatches[i])
                clusters[i] = avgs

    return bestmatches

# for dataset having only 1s and 0s for presence or absence,it would be
# more useful to define some measure of overlap between the people who
# want two items.
# For this,there is a measure called the Tanimoto coefficient,which is the
# ration of the intersection set (only the items that are in both sets) to
# the union set (all the items in either set).


def tanamoto(v1, v2):
    c1, c2, shr = 0, 0, 0

    for i in xrange(len(v2)):
        if v1[i] != 0:
            c1 += 1  # in v1
        if v2[i] != 0:
            c2 += 1  # in v2
        if v1[i] != 0 and v2[i] != 0:
            shr += 1  # in both

    return 1.0 - (float(shr) / (c1 + c2 - shr))

if __name__ == "__main__":
    blogname, words, data = readfile("blogdata.txt")
    clust = hcluster(data)
    printclust(clust, labels=blogname)

    # drawdendrogram(clust, blogname, jpeg='blogcluster.jpg')
    # rdata = rotatematrix(data)
    # wordclust = hcluster(rdata)
    # drawdendrogram(wordclust, labels=words, jpeg='wordclust.jpg')

    kclust = kcluster(data, k=10)
    print[blogname[r] for r in kclust[0]]
