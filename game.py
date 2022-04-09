from re import M
import string
from tkinter import Y
from setting import Setting
from wordbank import WordBank
from wordleword import WordleWord
from wordleplayer import WordlePlayer
from alphabet import alpha_to_num

# Snapshot #1: Finished writing two classes, wordleword and wordleplayer. Finished one method, markGuess()
# Snapshot #2: Game works well, might be some bugs but 99% works
# Snapshot #3: Fixed some bugs, added features: intro 
#                                               ability to change number of max tries
#                                               rage quit mode
#                                               menu
#                                               guess listing
#Snapshot #4: Added more features. Added .txt files containing words with 3, 4, 6 letters in each
#                                           1. ability to change number of tries
#                                           2. ability to change length of word
#                                           3. rage quit mode


#======
# markGuess - will "mark" the guess and the alphabet according to the word
#   word - String of word to be guessed
#   guess - WordleWord that have been guessed
#   alphabet - WordleWord of the letters a-z that have been marked
#======
def markGuess(word, guess, alphabet):

    repeatList = [] # list of letters (repetitions are ignored)
    number_of_repeat = [] # number of occurences for each "REPEAT" letter
    word_list = list(word)
    for letter in word_list:
        if letter not in repeatList:
            repeatList.append(letter)
            number_of_repeat.append(word_list.count(letter))

    for guessPos in range(len(word)):

        alpha_pos = alpha_to_num(guess.charAt(guessPos)) #converts letter to number position
        
        if guess.charAt(guessPos) == word[guessPos]: # checks if the letter is "correct"
            guess.setCorrect(guessPos)
            alphabet.setCorrect(alpha_pos)
            number_of_repeat[repeatList.index(guess.charAt(guessPos))] = number_of_repeat[repeatList.index(guess.charAt(guessPos))] - 1    

        elif word.count(guess.charAt(guessPos)) > 0:  # checks if the letter is "misplaced"
            if number_of_repeat[repeatList.index(guess.charAt(guessPos))] >= 1:
                guess.setMisplaced(guessPos)
                alphabet.setMisplaced(alpha_pos)
                number_of_repeat[repeatList.index(guess.charAt(guessPos))] = number_of_repeat[repeatList.index(guess.charAt(guessPos))] - 1    

        else:                                 # checks if the letter is "not used"
            alphabet.setUnused(alpha_pos)   
        
#=====
# playRound(players, words, all_words, settings)
# Plays one round of Wordle. 
# Returns nothing, but modifies the player statistics at end of round
#
#   players - List of WordlePlayers
#   words - Wordbank of the common words to select from
#   all_words - Wordbank of the legal words to guess
#   settings - Settings of game
#======
def playRound(players, words, all_words, settings):

    #retrieve settings
    set_rq = settings.getValue('rage quit')
    how_many_letter = settings.getValue("how many letter") 
    set_ffm = settings.getValue("ffm")

    #initialize variables
    alphabet = WordleWord("abcdefghijklmnopqrstuvwxyz")   #keyboard
    guess_list = []                                        
    total_guesses = 0
    game_solved = False                                    #bool for is the game solved
    colored_guess = []                                     #list of colored guesses
    rage_quit = False                                      #bool for rage quit mode

    #wordle solution
    if set_ffm and how_many_letter == 5:
        bank = WordBank("common5letterClean.txt")
        wordle_solution = bank.getRandom()
    else:
        wordle_solution = words.getRandom()
    


    while total_guesses < settings.getValue("maxguess") and not game_solved and not rage_quit:   

        #print list of colored guesses
        player_guess = input("Enter a guess: ")
        for i in range(total_guesses):
            print("{}.".format(i+1), colored_guess[i])
        
        #check for rage quit
        if set_rq and (player_guess == "I Rage Quit" or player_guess == "i rage quit"):
            print("You rage quit. The correct answer is", wordle_solution)
            rage_quit = True
        
        #if guess is correct
        elif player_guess == wordle_solution:
            total_guesses = total_guesses + 1
            wordle_word_player_guess = WordleWord(player_guess)
            markGuess(wordle_solution, wordle_word_player_guess, alphabet) 
            print("{}. {}".format(total_guesses, wordle_word_player_guess))
            print(alphabet, "")
            print("Congratulautions! You guessed the word!")
            game_solved = True
            guess_list.append(player_guess)

        #if valid guess
        elif len(player_guess) == how_many_letter and all_words.contains(player_guess):
            total_guesses = total_guesses + 1
            guess_list.append(player_guess)
            wordle_word_player_guess = WordleWord(player_guess)
            markGuess(wordle_solution, wordle_word_player_guess, alphabet) 
            print("Your last guess: ",wordle_word_player_guess)
            print(alphabet, "\n")
            colored_guess.append(wordle_word_player_guess)

        #if invalid guess
        else:
            print("============================")
            print(alphabet)
            print("{} is invalid, try again: ".format(player_guess))
            player_guess = False

    #if round lost        
    if game_solved == False:
        print("You didn't guess the answer")
        print("The solution is:", wordle_solution)

    players[0].updateStats(game_solved, total_guesses)   #update game history

def playWordle():

    print("Welcome to Wordle")

    # have you played before? and intro
    intro_noreply = True
    while intro_noreply:
        description_in = input("""Have you played Wordle Before?
===================================
Y = Yes
N = No
===================================
Choice: """)
        if description_in == "N" or description_in == "n":
            intro_noreply = False
            print("""
        Wondering what Wordle is? Wordle is a very addictive word game like crossword. 
        You will have 6 chances to guess a randomly selected 5 letter word.
        Rules for the base game:
        1) To begin, enter a 5 letter word 
        2) Letters in the correct spot would be marked Green
        3) If a letter is in the word but in the wrong position, the letter will be marked Yellow
        4) If a letter is not in the word, it will be marked red
        """) 
            print("Let's play Wordle!") 
        elif description_in == "Y" or description_in == 'y':
            intro_noreply = False
        else:
            print("Please enter a valid choice (Y or N)")
        
    # get player name
    player_name = input("""What is your name? """)
    player_name = player_name.capitalize()
    print("Welcome {}!".format(player_name))
    print("===================================")

    # initialize settings
    settings = Setting()

    # max try
    maxtry_set_in = input("""
The default number of tries is 6. Do you want to change it?
===================================
Y = Change
N = Don't Change
===================================
Choice: """)
    if maxtry_set_in == "Y" or maxtry_set_in == 'y':
        maxguess_in = int(input("How many tries should each game have: "))
        settings.setSetting('maxguess', maxguess_in)
    else:
        settings.setSetting('maxguess', 6)

    #different length mode
    letter_set_in = input("""
In the base game, the answer will be 5 letter long. In this version of Wordle, you have 
the option to try to solve 3, 4, 5, 6, and 7 letter words. Do you want to try this mode? 
NOTE: length of letters other than 5 might be more difficult!
===================================
3 = Change to 3 letters
4 = Change to 4 letters
6 = Change to 6 letters
7 = Change to 7 letters
8 = Change to 8 letters
N = Don't Change, keep it 5 letters
===================================
Choice: """)
    if letter_set_in == '8':
        all_words = WordBank("common8letter.txt")
        common_words = WordBank("common8letter.txt")
        settings.setSetting("how many letter", 8)
    if letter_set_in == '7':
        all_words = WordBank("common7letter.txt")
        common_words = WordBank("common7letter.txt")
        settings.setSetting("how many letter", 7)
    elif letter_set_in == '6':
        all_words = WordBank("common6letter.txt")
        common_words = WordBank("common6letter.txt")
        settings.setSetting("how many letter", 6)
    elif letter_set_in == '4':
        all_words = WordBank("common4letter.txt")
        common_words = WordBank("common4letter.txt")
        settings.setSetting("how many letter", 4)
    elif letter_set_in == '3':
        all_words = WordBank("common3letter.txt")
        common_words = WordBank("common3letter.txt")
        settings.setSetting("how many letter", 3) 
    elif letter_set_in == "N" or letter_set_in == 'n':
        all_words = WordBank("words_alpha.txt")
        common_words = WordBank("common5letter.txt")
        settings.setSetting("how many letter", 5)

    #rage quit mode
    rq_set_in = input("""
Rage Quit Mode: Type 'I Rage Quit' while playing Wordle to end the game and see the answer
Enabled by default.
===================================
N = Disable Rage Quit Mode
Y = Keep enabled
===================================
Choice: """)
    if rq_set_in == 'N' or rq_set_in == 'n':
        settings.setSetting('rage quit', False)
    else:
        settings.setSetting('rage quit', True)

    #Family Friendly Mode
    ffm_set_in = input('''
In Family Friendly mode, the answer is always a clean word. 
All swears and offensive words will be removed. Do you want to enable this mode?
===================================
Y = Activate Family Friendly Mode
N = Disable Family Friendly Mode
===================================
Choice: ''')
    if ffm_set_in == "N" or ffm_set_in == "n":
        settings.setSetting("ffm", False)
    elif ffm_set_in == "Y" or ffm_set_in == 'y':
        settings.setSetting("ffm", True)


    settings.setSetting('numplayers', 1)
    settings.setSetting('difficulty', 'normal')

    #make player
    player = WordlePlayer(player_name, settings.getValue('maxguess'))

    # start playing rounds of Wordle    
    playRound([player], common_words, all_words, settings)

    #check if player wants to play again
    replay_bool = True
    count = 0
    while replay_bool:
        count = count + 1
        replay_preference = input("""
===================================
Y = play again
Q = quit
D = display stats
M = access menu
===================================
Choice: """)

        if replay_preference == "q" or replay_preference == "Q":        #quit game
            replay_bool = False
            player.display_stats()
        elif replay_preference == "d" or replay_preference == "D":      #display stats
            player.display_stats()
        elif replay_preference == "y" or replay_preference == "Y":      #play again
            playRound([player], common_words, all_words, settings)
            print("Starting a new game...")
            print()
            print()
        elif replay_preference == 'M' or replay_preference == 'm':      #access menu
            change_set_in = input("""
===================================
L = Change the number of letters for the answer
N = Change number of max tries
R = Change Rage Quit preferences
F = Toggle Family friendly mode
===================================
Choice: """)
            #menu change number of guesses
            if change_set_in == 'N' or change_set_in == 'n':
                menu_change_maxtry = int(input("How many tries do you want: "))
                settings.setSetting('maxguess', menu_change_maxtry)
                player.updateMaxTry(menu_change_maxtry)

            #menu change number of letters
            elif change_set_in == "L" or change_set_in == 'l':
                menu_change_letter = int(input("""
How many letter should the answer be? 
NOTE: length of letters other than 5 might be more difficult!
===================================
3 = Change to 3 letters
4 = Change to 4 letters
5 = Change to 5 letters
6 = Change to 6 letters
7 = Change to 7 letters
8 = Change to 8 letters
===================================
Choice: """))
                #check if input is valid and change settings accordingly
                checking_lst_letter = [3,4,5,6,7]
                if menu_change_letter not in checking_lst_letter:
                    print("""
You entered an invalid response. This game only supports 3,4,5,6,7 letter words. 
Please try again by entering menu and then type L to change the length of words""")
                elif menu_change_letter == "8":
                    all_words = WordBank("common8letter.txt")
                    common_words = WordBank("common8letter.txt")
                    settings.setSetting("how many letter", 8)
                elif menu_change_letter == "7":
                    all_words = WordBank("common7letter.txt")
                    common_words = WordBank("common7letter.txt")
                    settings.setSetting("how many letter", 7)
                elif menu_change_letter == '6':
                    all_words = WordBank("common6letter.txt")
                    common_words = WordBank("common6letter.txt")
                    settings.setSetting("how many letter", 6)
                elif menu_change_letter == '5':
                    all_words = WordBank("words_alpha.txt")
                    common_words = WordBank("common5letter.txt")
                    settings.setSetting("how many letter", 5)
                elif menu_change_letter == '4':
                    all_words = WordBank("common4letter.txt")
                    common_words = WordBank("common4letter.txt")
                    settings.setSetting("how many letter", 4)
                elif menu_change_letter == '3':
                    all_words = WordBank("common3letter.txt")
                    common_words = WordBank("common3letter.txt")
                    settings.setSetting("how many letter", 3) 

            #menu change rage quit preferences
            elif change_set_in == "R" or change_set_in == 'r':
                menu_change_rq = input("""
Rage Quit Mode: Type 'I Rage Quit' while playing Wordle to end the game and see the answer
Enabled by default.
===================================
N = Disable Rage Quit Mode
Y = Keep enabled
===================================
Choice: """)
                if menu_change_rq == 'N' or menu_change_rq == 'n':
                    settings.setSetting('rage quit', False)
                elif menu_change_rq == 'Y' or menu_change_rq == 'y':
                    settings.setSetting('rage quit', True)
                    
            #menu change family friendly preferences
            elif change_set_in == "F" or change_set_in == "f":
                menu_change_ffm = input("""
Family Friendly Mode: Uses a list of clean words.
===================================
Y = Yes
N = No
===================================
Choice: """)
                if menu_change_ffm == "N" or menu_change_ffm == "n":
                    settings.setSetting("ffm", False)
                elif menu_change_ffm == "Y" or menu_change_ffm == 'y':
                    settings.setSetting("ffm", True)
            
def main():
    playWordle()

if __name__ == "__main__":
    main()

# existing features:
    # guess listing
    # intro
    # input checking
    # ability to change maximum umber of tries
    # rage quit mode
    # menu
    # make wrong letters red instead of gray