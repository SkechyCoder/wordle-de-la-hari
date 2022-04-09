'''
Edited on Feb 4, 2020

@author: mark_kwong
'''

#===========================================================================
# Description: a card player with money and a hand of stack_of_cards
#
# State Attributes
#    name - string - the name of the player
#    score - integer - how many points the player has
# Methods
#    introduce() - prints out message "Hi, my name is ..."
#    __str__() - returns a string ex. 'Joe: 5 points'
#    getName() - returns the name of the player
#===========================================================================
class Player:

    # inputs:
    #    name - string for the player's name
    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        self.score = 0
     
    # prints out name and the hand of stack_of_cards    
    def __str__(self):
        return("{}: {} points".format(self.name, self.score))
    
    def introduce(self):
        print("Hi, my name is {}".format(self.name))
        
    def getName(self):
        return(self.name)
    
    def getScore(self):
        return self.score

    # add (or subtract) from player's score    
    def addScore(self, amount):
        self.score += amount
    