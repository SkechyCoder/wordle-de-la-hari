#===========================================================================
# Description: WordleWord(word)
# Inherits from the FancyWord class and adds methods for the Wordle game
#
# Methods
#    isCorrect(pos) - boolean - return True if character at pos is correct
#    isMisplaced(pos) - boolean - return True if character at pos is misplaced
#    isNotUsed(pos) - boolean - return True if character at pos is not in word
#    setCorrect(pos) - integer - set character are pos correct and colors accordingly
#    setMisplaced(pos) - integer - set character are pos misplaced and colors accordingly
#    setNotUsed(pos) - integer - set character are pos misplaced and colors accordingly
#===========================================================================
from turtle import color
from fancyword import FancyWord

# TODO - make WordleWord
class WordleWord(FancyWord):

    def __init__(self, word):
        super().__init__(word)

    def setCorrect(self, pos): # sets a letter green
        self.setColorAt(pos, "green")

    def setMisplaced(self, pos): # sets a letter yellow
        self.setColorAt(pos, "yellow")

    def setUnused(self, pos): # sets a letter red
        self.setColorAt(pos, "red")
    
    def setNormal(self,pos): # sets a letter gray
        self.setColorAt(pos, "gray") 

    def isCorrect(self, pos): # if correct, set green
        if self.colorAt(pos) == "green": 
            return True
        else:
            return False

    def isMisplaced(self, pos): # if misplaced, set yellow
        if  self.colorAt(pos) ==  "yellow":
            return True
        else:
            return False

    def isNotUsed(self, pos): # if unused, set gray
        if self.colorAt(pos) == "gray":
            return True
        else:
            return False