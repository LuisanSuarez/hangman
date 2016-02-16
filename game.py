import random
import string

WORDLIST_FILENAME = "C:\Users\DELL\Desktop\Luis Angel\Programming\Python\Hangman\words.txt"
#this is where I have my word list. You will need to download your own. One is available in this repository. 

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
#    secretWord = 'apple'
    letras = list(secretWord)
#    print letras
#    letterGuessed = ['p', 'l', 'e', 'a']
#    print letterGuessed
    #ans = True
    for i in letterGuessed:
        if i not in letras:
            ans = False
            #print False
            break
        else:
            ans = True
    print ans



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    #secretWord = 'apples'
    tralist = list(secretWord)
    #print tralist
    #letterGuessed = ['c', 'l', 'p', 'e', 'a']
    mago = ''
    base = []
    for o in range(len(secretWord)):
        base.append('_')
    for i in lettersGuessed:
        if i not in secretWord:
            ans = 'fresh'
        elif i in secretWord:
            while tralist.count(i) != 0:
                n = tralist.index(i)
                del base[n]
                del tralist[n]
                base.insert(n, i)
                tralist.insert(n,'*')
    for l in base:
        mago += l
        mago += ' '
    #return 'Now you have: ' + str(mago)
    return mago
    

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    t = []
    for i in lettersGuessed:
        if i not in t:
            t.append(i)
    
    # FILL IN YOUR CODE HERE...
    import string
    
    #inputLetters.append(lettersGuessed)
    s = string.ascii_lowercase
    #lettersGuessed = ['c', 'l', 'p', 'e', 'a']
    ultima = list(s)
    #print ultima
    for i in t:
        ultima.remove(i)
    so = ''.join(ultima)
    #print ultima 
    #return 'Available letters: ' + str(s)
    return so
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    print 'Welcome' + ' to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    numGuesses = 8
    lettersGuessedA = []
    s = string.ascii_lowercase
    player = 'loser'
    while numGuesses > 0:
        if '_' not in getGuessedWord(secretWord, lettersGuessedA):
            player = 'winner'
            print 'CONGRATS! YOU ARE THE WINNER!'
            break
        print 'You have ' + str(numGuesses) + ' guesses left.'
        print 'Available Letters: ' + getAvailableLetters(lettersGuessedA)
        guessX = str(raw_input('Please guess a letter: '))
        guess = guessX.lower()
        if len(guess) == 1 and guess in s:    
            if guess not in lettersGuessedA:
            a    lettersGuessedA.append(guess)
                if guess in secretWord:
                    numGuesses -= 0
                    getAvailableLetters(lettersGuessedA)
                    print 'Good guess: ' + getGuessedWord(secretWord, lettersGuessedA)
                elif guess not in secretWord:
                    numGuesses -= 1
                    getAvailableLetters(lettersGuessedA)
                    print 'Oops! That letters is not in my word: ' + getGuessedWord(secretWord, lettersGuessedA)
            else:
                print 'Wops! You already guessed that letter! Try again.' +  getGuessedWord(secretWord, lettersGuessedA)
        else:
            print 'Uh-oh! Your guess must be one alphabet letter only.'
            print "So far you've guessed" +  getGuessedWord(secretWord, lettersGuessedA)
            
    if player != 'winner':
        print 'Pay attention: ' + str(secretWord) 
    




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
