#===========================================================================
# Description: a bank/list of words
#
# State Attributes
#    words - List - a list of all the words
#    index - Integer - index into the next word of the list
# Methods
#    contains(word) - returns boolean of whether word is in the bank of words
#    getRandom() - returns a random word within the bank of words
#    getNext() - get the next word in the list (wraps around when at end of list)
#===========================================================================
import random

class WordBank:

    # inputs:
    #   filename - the filename that is read with the list of all the words
    def __init__(self, filename):
        with open(filename) as wordfile:
            self.words = wordfile.read().split()
        self.index = 0

    def contains(self, word):
        return word in self.words

    def getRandom(self):
        choice = random.randrange(len(self.words))
        return self.words[choice]

    def getNext(self):
        word = self.words[self.index]

        self.index += 1
        if self.index >= len(self.words):
            self.index = 0

        return word

            

