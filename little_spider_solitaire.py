'''
Name: Minh Nguyen
CSC 201
Programming Project 4

This program plays a version of Little Spider Solitaire. In this version
the foundation piles starting with two red aces and two black kings
are created when the game begins. The eight tableau piles are in
one horizontal line. At any time, cards can be moved from the
tableau to the foundation piles or to another tableau, as long as
it is a valid move. One point is earned for every valid move to
a foundation pile.

'''

from board import *
from button import *
from deck import *
from card import *
import time

GAME_WINDOW_WIDTH = 750
GAME_WINDOW_HEIGHT = 500

def displayDirections():
    """
    Gives the directions for Little Spider Solitaire. To continue the game,
    the "Click to Begin" button must be clicked.

    """
    win = GraphWin("Directions", 700, 600)
    win.setBackground("white")
    string = ("Welcome to Little Spider Solitaire\n\n"
                "The objective is to get all cards\n"
                "into the foundation piles which are built\n"
                "sequentially from cards of the same suit.\n\n"
                "The top card in any tableau can be moved\n"
                "either to a foundation pile, to another\n"
                "tableau if its rank is one above or\n"
                "below the tableau's current top card, or\n"
                "moved to an empty tableau.\n\n"
                "No more moves? Click the stock pile to get\n"
                "eight more cards.\n\n"
                "Good luck!")
    directions = Text(Point(win.getWidth()/ 2, win.getHeight()/2), string)
    directions.setSize(16)
    directions.draw(win)
    startButton = Button(Point(350, 525), 120, 40, "Click to Begin")
    startButton.draw(win)
    startButton.activate()
    click = win.getMouse()
    while not startButton.isClicked(click):
        click = win.getMouse()
    win.close()

def setUpGame():
    '''
    Creates the window with a start button, the tableaus, the stock pile, the
    foundation, and the label for scoring an Aces Up solitaire game. When the
    start button is clicked one card is dealt to each tableau and the button
    is renamed Quit.
    
    Returns:
        the window where the game will be played, the board managing the cards,
        the button now labeled Quit, and the scoring label.
    '''
    win = GraphWin('Little Spider Solitaire', GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT)
    win.setBackground('lightgreen')
    
    gameBoard = LittleSpiderBoard(win)
    
    button = Button(Point(675, 50), 80, 40, "Start")
    button.draw(win)
    button.activate()
    
    scoreLabel = Text(Point(70, 450), "Score: 0")
    scoreLabel.setSize(16)
    scoreLabel.draw(win)
    
    click = win.getMouse()
    while not button.isClicked(click):
        click = win.getMouse()
    
    button.setLabel("Quit")
    
    gameBoard.dealFromStock(win)
    return win, gameBoard, button, scoreLabel

def playGame(window, gameBoard, button, scoreLabel):
    '''
    Plays the Little Spider Solitaire game enforcing the rules
    
    Params:
        window (GraphWin): the window where the game is played
        gameBoard (LittleSpiderBoard): the board managing the cards
        button (Button): the button to click to end the game
        scoreLabel (Text): the label showing the game score as the game progresses
        
    Returns:
        score (int): the score earned by the player determined by the number of
        cards moved to the foundation piles
    '''
    score = 0
    click = window.getMouse()
    while not gameBoard.isWin() and not button.isClicked(click):
        if gameBoard.isPointInStockCard(click) and not gameBoard.isStockEmpty():
            gameBoard.dealFromStock(window)
            
        elif gameBoard.isPointInTableauCard(click):
            card1 = gameBoard.getCardAtPoint(click)
            click2 = window.getMouse()
            
            if gameBoard.isPointInEmptyTableau(click2):
                gameBoard.moveCardToAnotherTableauPile(card1, click2, window)
                
            elif gameBoard.isPointInTableauCard(click2):
                card2 = gameBoard.getCardAtPoint(click2)
                if card1.getRank() == 1 and card2.getRank() == 13:
                    gameBoard.moveCardToAnotherTableauPile(card1, click2, window)
                elif card1.getRank() == 13 and card2.getRank() == 1:
                    gameBoard.moveCardToAnotherTableauPile(card1, click2, window)
                elif card1.getRank() == card2.getRank() + 1 or card1.getRank() == card2.getRank() - 1:
                    gameBoard.moveCardToAnotherTableauPile(card1, click2, window)    

            elif gameBoard.isPointInFoundationCard(click2):
                card2 = gameBoard.getCardAtPoint(click2)
                if card1.getSuit() == card2.getSuit() and card1.getSuit() in ('h','d'):
                    if card1.getRank() == card2.getRank() + 1:
                        gameBoard.moveCardToFoundationPile(card1, click2, window)
                        score = score + 1
                        scoreLabel.setText(f'Score: {score}')
                elif card1.getSuit() == card2.getSuit() and card1.getSuit() in ('s','c'):
                    if card1.getRank() == card2.getRank() - 1:
                        gameBoard.moveCardToFoundationPile(card1, click2, window)
                        score = score + 1
                        scoreLabel.setText(f'Score: {score}')
                        
        click = window.getMouse()
    return score

def main():
    displayDirections()
    
    window, gameBoard, button, scoreLabel = setUpGame()
    
    score = playGame(window, gameBoard, button, scoreLabel)
    
    if gameBoard.isWin():
        message = Text(Point(window.getWidth()/2, window.getHeight()/2 + 25), "You Won! Wooohooo!")
        
    elif score == 0:
        message = Text(Point(window.getWidth()/2, window.getHeight()/2 + 25), "Disappointed")
     
    elif score < 10:
        message = Text(Point(window.getWidth()/2, window.getHeight()/2 + 25), "Were you even trying?")
      
    elif score < 20:
        message = Text(Point(window.getWidth()/2, window.getHeight()/2 + 25), "Not bad bro")
     
    elif score < 48:
        message = Text(Point(window.getWidth()/2, window.getHeight()/2 + 25), "Your mom loves you :3")
        
    message.setSize(26)
    message.setTextColor('red')
    message.setStyle('bold')
    message.draw(window)
       
    time.sleep(2)    
    window.close()

if __name__ == '__main__':
    main()
