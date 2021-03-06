# A dictionary of movie critics and their ratings of a small
# set of movies
critics = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
                         'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
                         'The Night Listener': 3.0},
           'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
                            'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
                            'You, Me and Dupree': 3.5},
           'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
                                'Superman Returns': 3.5, 'The Night Listener': 4.0},
           'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                            'The Night Listener': 4.5, 'Superman Returns': 4.0,
                            'You, Me and Dupree': 2.5},
           'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                            'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
                            'You, Me and Dupree': 2.0},
           'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                             'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
           'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}}

from math import sqrt

# Returns a distance-based similarity score for person1 and person2


def sim_distance(prefs, person1, person2):
    # Get the list of shared_items
    si = {}
    for item in person1:
        if item in person2:
            si[item] = 1

    # if they have no ratings in common,return 0
    if len(si) == 0:
        return 0

    # Add up the squares of all the differences
    sum_of_squres = sum([pow(prefs[person1][item] - prefs[person2][item], 2)
                         for item in prefs[person1] if item in prefs[person2]])

    return 1 / (1 + sum_of_squres)

# Returns the Pearson correlation coefficient for p1 and p2


def sim_pearson(prefs, p1, p2):
    # Get the list of mutually rated items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    # Find the number of elements
    n = len(si)

    # if they have no ratings in common,return 0
    if n == 0:
        return 0

    # Add up all the preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    # Sum up the squares
    sum1Sq = sum([pow(prefs[p1][it], 2)for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])

    # Sum up the products
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    # Calculate Pearson score
    num = pSum - (sum1 * sum2) / n
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))

    if den == 0:
        return 0

    r = num / den

    return r

# Ranking the Critics
# Returns the best matches for person from preferences dictionary.
# Number of results and similarity function are optional params.


def topMatches(prefs, person, n=5, similarity=sim_pearson):
    scores = [(similarity(prefs, person, other), other)
              for other in prefs if other != person]

    # sort the list so the highest scores appear at the top
    scores.sort()
    scores.reverse()
    return scores[0:n]

# recommending items
# Score the items by producing a weighted score that ranks the critics.
# Take the votes of all the other critics and multiply how similar they
# are to me by the score they gave each movie.

# Gets recommendations for a person by using a weighted average
# of every other user's rankings


def getRecommendations(prefs, person, similarity=sim_pearson):
    totals = {}
    simSums = {}
    for other in prefs:
        # don't compare me to myself
        if other == person:
            continue
        sim = similarity(prefs, person, other)

        # ignore scores of zero or lower
        if sim <= 0:
            continue
        for item in prefs[other]:

            # only score movies I haven't seen yet
            if item not in prefs[person] or prefs[person][item] == 0:
                # Similarity * Score
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim
                # Sum of similarities
                simSums.setdefault(item, 0)
                simSums[item] += sim

    # Create the normalized list
    rankings = [(total / simSums[item], item)
                for item, total in totals.items()]

    # Return the sorted list
    rankings.sort()
    rankings.reverse()
    return rankings

# Matching products
# Determine similarity between items by looking at who liked a particular
# item and seeing the other things they liked.
# This is actually the same method we used to determine similarity between
# people:to swap the people and items.


def transformPrefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})

            # Flip item and person
            result[item][person] = prefs[person][item]

    return result

# Item-based Filtering
# user-based collaborative filtering and item-based collaborative filtering
# Item-based:
#   Precompute the most similar items for each item.


def calculateSimilarItems(prefs, n=10):
    # Create a dictionary of items showing which other items they are most
    # similar to
    result = {}

    # Invert the preference matrix to be item-specific
    itemPrefs = transformPrefs(prefs)
    c = 0
    for item in itemPrefs:
        # Status update for large datasets
        c += 1
        if c % 100 == 0:
            print "%d / %d" % (c, len(Prefs))
        # Find the most similar items to this one
        scores = topMatches(itemPrefs, item, n=n, similarity=sim_distance)
        result[item] = scores
    return result

# Getting Recommendations
# Give recommendations using the item similarity dictionary without going
# through the whole dataset.
# Get all the items that the user has ranked,find the similar items,and
# weight them according to how similar they are.


def getRecommendedItems(prefs, itemMatch, user):
    userRatings = prefs[user]
    scores = {}
    totalSim = {}

    # Loop over rated by this user
    for (item, rating) in userRatings.items():

        # Loop over items similar to this one
        for (similarity, item2) in itemMatch[item]:

            # ignore if this user has already rated this item
            if item2 in userRatings:
                continue

            # Weighted sum of ratings times similarity
            scores.setdefault(item2, 0)
            scores[item2] += similarity * rating

            # Sum of all the similarities
            totalSim.setdefault(item2, 0)
            totalSim[item2] += similarity

    # divide each total score by total weighting to get an average
    rankings = [(scores[item] / totalSim[item], item) for item in scores]
    rankings.sort()
    rankings.reverse()
    return rankings


def loadMovieLens(path='../dataset/ml-10M100K'):

    # Get movie titles
    movies = {}
    for line in open(path + '/movies.dat'):
        (id, title) = line.split('::')[0:2]
        movies[id] = title

    # Load data
    prefs = {}
    for line in open(path + '/ratings.dat'):
        (user, movieid, rating, ts) = line.split('::')
        prefs.setdefault(user, {})
        prefs[user][movies[movieid]] = float(rating)

    return prefs


if __name__ == "__main__":
    print sim_pearson(critics, 'Lisa Rose', 'Gene Seymour')

    print topMatches(critics, 'Toby', n=3)

    print getRecommendations(critics, 'Toby')
    print getRecommendations(critics, 'Toby', similarity=sim_distance)

    movies = transformPrefs(critics)
    print topMatches(movies, 'Superman Returns')

    print "\nSimilar items:"
    itemsim = calculateSimilarItems(critics)

    print getRecommendedItems(critics, itemsim, 'Toby')

    prefs = loadMovieLens()
    # print prefs['87']
    print getRecommendations(prefs, '87')[0:30]
