#===========================================================================
# class FancyWord
# Description: a colored word - each letter has a color attribute
#
# Methods
#    updateStats(won, tries) - 'won' - True if guessed word correctly
#                            - 'tries' - number of tries it took to guess word
#                            - This is called at the end of each game to update
#                              the game stats for this player
#    winPercentage() - returns % of how many games were won over all time
#    gamesPlayed() - returns the number of games played over all time 
#    currentStreak() - returns the current win streak; it will return 0 if
#                      the last game was lost
#    maxStreak() - returns the longest winning streak
#    displayStats() - prints out nice display of all the Wordle player stats
#    
#    Games Played: 3
#    Win %: 100.00
#    Current Streak: 3
#    Max Streak: 3
#    Guess Distribution
#      1: ########### 1
#      2: # 0                        <-- min bar length is 1
#      3: # 0
#      4: ##################### 2    <-- max bar length is 21
#      5: # 0
#      6: # 0
#=============
from player import Player

class WordlePlayer(Player):

    def __init__(self, name, maxTry):
        super().__init__(name)
        self.maxTry = maxTry    #in use
        self.gamesPlayed = 0   #in use
        self.gamesWon = 0      #in use
        self.currentWinStreak = 0  #in use
        self.maxWinStreak = 0      #in use
        self.gameHistory = []      #in use
        self.guess = []            #in use
    


    def win_rate(self):
        return round((self.gamesWon * 100 / self.gamesPlayed), 2)
    
    def games_played(self):
        return self.gamesPlayed
    
    def current_streak(self):
        return self.currentWinStreak

    def max_streak(self):
        if self.gamesPlayed == self.gamesWon:
            return self.gamesPlayed
        streak = 0
        big_streak_so_far = 0
        for i in self.gameHistory:
            if i == True:
                streak = streak + 1
            elif i == False:
                streak = 0
            if streak > big_streak_so_far:
                big_streak_so_far = streak
        return big_streak_so_far

    def display_stats(self):
        print("Games Played:", self.gamesPlayed)
        print("Win %: {}%".format(self.win_rate()))
        print("Current Streak:", self.currentWinStreak)
        print("Max Streak:", self.maxWinStreak)
        print("Guess Distrubution")

        #make list of tries/number of guesses
        guessList = []
        for number in range(self.maxTry+1):
            if number > 0:
                for i in self.guess:
                    if i == number:
                        guessList.append(number)

        #find the largest number of guesses
        most_guess = -1
        for dum in range(1, self.maxTry + 1):
            if guessList.count(dum) > most_guess:
                most_guess = guessList.count(dum)
        #make histogram
        if self.guess == []:
            print("You have not won any games.")
            return 0
        for guess_display in range(1, 1 + self.maxTry):
            hash_mult = guessList.count(guess_display) * 20//most_guess
            print(str(guess_display) + ": #" + "#" * (hash_mult), guessList.count(guess_display))
        
    def updateStats(self, won, tries):
        self.gameHistory.append(won)
        self.gamesPlayed = self.gamesPlayed + 1
        self.maxWinStreak = self.max_streak()

        if won == True:
            self.gamesWon = self.gamesWon + 1
            self.currentWinStreak = self.currentWinStreak + 1
            self.guess.append(tries)
        elif won == False:
            self.currentWinStreak = 0

    def updateMaxTry(self, newMax):
        if newMax > self.maxTry:
            self.maxTry = newMax
