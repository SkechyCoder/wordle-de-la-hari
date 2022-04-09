#===========================================================================
# class FancyWord
# Description: a colored word - each letter has a color attribute
#
# State Attributes
#   - word - String - the word
#   - color - List - a list of strings which indicate the color or each word
#                  - colors: 'normal', 'green', 'yellow', 'red', 'blue' and 'gray' are supported
#
# Methods
#   - getWord() - returns the word
#   - setColor(color) - sets the color of the entire word to 'color'
#   - charAt(pos) - returns the letter of the word at pos
#   - getChColor(pos) - returns the color of the letter at pos
#   - setChColor(pos, color) - sets the color of the letter at pos to color
#   - __str__() - returns an ANSI colored string of the word
#   - __eq__() - compares the word of two Fancy words
#===========================================================================

class FancyWord:
    def __init__(self, w):
        self.word = w
        self.setColor('normal')

    def getWord(self):
        return self.word

    def setColor(self, color):
        self.color = [color for ch in self.word]

    def charAt(self, pos):
        return self.word[pos]

    def colorAt(self, pos):
        return self.color[pos]

    def setColorAt(self, pos, color):
        self.color[pos] = color

    def __str__(self):
        formattedWord = ""
        for i in range(len(self.word)):
            if self.color[i] == 'green':
                # bold green
                formattedWord += u'\u001b[1m\u001b[38;5;34m{}\u001b[0m'.format(self.word[i])
            elif self.color[i] == 'yellow':
                # bold yellow
                formattedWord += u'\u001b[1m\u001b[38;5;214m{}\u001b[0m'.format(self.word[i])
            elif self.color[i] == 'red':
                # bold red
                formattedWord += u'\u001b[1m\u001b[38;5;196m{}\u001b[0m'.format(self.word[i])
            elif self.color[i] == 'blue':
                # bold blue
                formattedWord += u'\u001b[1m\u001b[38;5;20m{}\u001b[0m'.format(self.word[i])
            elif self.color[i] == 'gray':
                # light gray
                formattedWord += u'\u001b[38;5;250m{}\u001b[0m'.format(self.word[i])
            else:
                formattedWord += self.word[i]
    
        return formattedWord

    def __eq__(self, other):
        return self.word == other.word and self.color == other.color