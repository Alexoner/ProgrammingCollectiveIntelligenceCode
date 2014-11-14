# -*-encoding:utf-8 -*-
"""
    Document filtering
    """

import re
import math


def getwords(doc):
    """
        Extract the features from the text
    """
    splitter = re.compile('\\W*')
    # Split the words by non-alpha characters
    words = [s.lower() for s in splitter.split(doc)
             if len(s) > 2 and len(s) < 20]

    # return the unique set of words only
    return dict([(w, 1) for w in words])


class classifier:

    """
    Represent the classifier.This class encapsulate what the classifier
    has learned so far.
    Methods won't use the dictionaries directly because this restricts
    potential options for storing the training data in a file or database.
    """

    def __init__(self, getfeatures, filename=None):
        # Counts of feature/category combinations
        self.fc = {}
        # Counts of documents in each category
        self.cc = {}
        self.getfeatures = getfeatures

    def incf(self, f, cat):
        """
        Increase the count of a feature/category pair
        """
        self.fc.setdefault(f, {})
        self.fc[f].setdefault(cat, 0)
        self.fc[f][cat] += 1

    def incc(self, cat):
        """
        increase the count of a category
        """
        self.cc.setdefault(cat, 0)
        self.cc[cat] += 1

    def fcount(self, f, cat):
        """
        The number of times a feature has appeared in a category
        """
        if f in self.fc and cat in self.fc[f]:
            return float(self.fc[f][cat])
        return 0.0

    def catcount(self, cat):
        """
        The number of items in a category
        """
        if cat in self.cc:
            return float(self.cc[cat])
        return 0.0

    def totalcount(self):
        """
        The total number of items
        """
        return sum(self.cc.values())

    def categories(self):
        """
        The list of all categories
        """
        return self.cc.keys()

    def train(self, item, cat):
        features = getwords(item)
        # Increment the count of every count feature with this category
        for f in features:
            self.incf(f, cat)

        # Increment the count for this category
        self.incc(cat)

if __name__ == "__main__":
    cl = classifier(getwords)
    cl.train('the quick brown for jumps over the lazy dog', 'good')
    cl.train('make quick money in the online casino', 'bad')
    cl.train('Nobody owns the water', 'good')
    cl.train('the quick rabbit jumps fences', 'good')
    cl.train('buy pharmaceuricals now', 'bad')
    print cl.fcount('quick', 'good')
    print cl.fcount('quick', 'bad')
