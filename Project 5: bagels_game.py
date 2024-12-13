'''
Name(s): Minh Nguyen
CSC 201
Lab 5

This program plays the game of "Bagels" where the user tries to guess a number.
After each guess the user is given clues:
    "fermi" for correct digit in the correct position
    "pico" for correct digit is the wrong position
    "bagels" when every digit is incorrect
When the user guesses the number, the user is asked whether they want to play again.

'''
import random
NUM_DIGITS = 4    # number of digits in the number to be guessed

def intro():
    '''
    Introduces the game and explains the clues
    '''
    print('Welcome to Bagels!')
    print()
    print(f"I'm thinking of a {NUM_DIGITS} digit number. Each digit is between")
    print("1 and 9. Try to guess my number.")
    print()
    print("I'll say \"fermi\" for each correct digit in the correct position.")
    print("I'll say \"pico\" for each correct digit in the wrong position.")
    print("I'll say \"bagels\" if all of the digits are wrong.")
  
  
def getClues(secretString, guessString):
    """
    Creates the clues for the user depending on how of the user's guess match
    the secret number to be guessed.
    
    Params:
        secretString: The number to be guessed as a string
        guessString: The number guessed by the user as a string
    
    Returns:
        str: a string of clues
    """
    # create lists to cleverly use to determine the clues
    secretList = list(secretString)
    guessList = list(guessString)
    clues = ''
    
    # check for any correct digits in the correct position
    for index in range(NUM_DIGITS):
        if guessList[index] == secretList[index]:
            clues = clues + 'fermi '
            guessList[index] = 'X'
            secretList[index] = 'Y'
    
    # check for any correct digits in the wrong position
    for index in range(NUM_DIGITS):
        for index2 in range(NUM_DIGITS):
            if secretList[index] == guessList[index2]:
                clues = clues + 'pico '
                secretList[index] = 'Y'
                guessList[index2] = 'X'
   
    # if clues is '' then there were no correct digits
    if clues == '':
        clues = 'bagels'
        
    return clues


def getSecretNumber():
    '''
    Randomly generates the number the user will guess stored as a string
    Each digit must be 1-9 inclusive
    
    Returns:
        str: the secret number as a string of digits each digit 1-9
    '''
    secretNumber = ""
    
    for count in range(NUM_DIGITS):
        randomDigit = str(random.randrange(1,10))
        secretNumber = secretNumber + randomDigit
        
    return secretNumber

def isGuessValid(guess):
    """
    Determines if the guess is valid. To be valid, it must have NUM_DIGIT characters,
    each character must be a digit, and none of the characters can be a '0'.
    
    Param:
        guess (str): the guess made by the user
    Returns:
        bool: True if the guess is valid; False otherwise
    """
    guessLen = len(guess)
    
    if guessLen == NUM_DIGITS and guess.isdigit() and "0" not in guess:
        return True
    else:
        return False


def getUserGuess():
    '''
    This function repeatedly asks the user to make a guess until the guess is valid.
    
    Returns:
        str: The valid guess entered by the user as a string
    '''
    userGuess = input('Your guess? ')
    
    while str(isGuessValid(userGuess)) == 'False':
        print(f'You must enter {NUM_DIGITS} with no zeros. Try again.')
        userGuess = input('Your guess? ')
    return userGuess


def playOneRound():
    """
    Plays one round from generating the number to be guessed until the user guesses the number.
    When the user guesses the number, the number of guesses it took is displayed.
    """
    secretNumber = getSecretNumber()
    print(f'Secret number is {secretNumber}')

    userGuess = getUserGuess()
    guessNum = 0

    guessCorrect = False
    
    while not guessCorrect:
        guessNum = guessNum + 1
        
        if userGuess != secretNumber:
            guessCorrect = False
            message = getClues(secretNumber, userGuess)
            print(message)
            userGuess = getUserGuess()
        else:
            guessCorrect = True
            
    if guessNum == 1:
        print('You got it in 1 guess.')
    else:
        print(f'You got it in {guessNum} guesses.')
    
def playAgain():
    """
    The function asks the user if they want to play again until
    the user answers 'y' or 'n', upper or lower case.
    
    Returns:
        str: the lowercase version of the user's y/n response lower case
    """    
    response = input('Do you want to play again (y/n)? ')
    response = response.lower()
    
    while response not in ('y','n'):
        print('You must answer y or n. Try again.')
        response = input('Do you want to play again(y/n)? ')
        response = response.lower()
        
    return response

def main():
    intro()  
    response = 'y'
    while response == 'y':
        print()
        playOneRound()
        print()
        response = playAgain()
            
main()         
