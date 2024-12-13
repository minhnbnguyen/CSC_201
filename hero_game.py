'''
Name(s): Minh Nguyen and Duy Luong
CSC 201
Project 3

This program plays the game of "Luffy vs Gecko Moria" where the user tries to shoot a devil fruit (fireball) to defeat the enemy, Gecko Moria.
Users are prompt to use mouse click to move the hero, Luffy, and press Space to shoot the devil fruit to Gecko Moria.
For every Gecko Moria defeated by the devil fruit, they are added 1 point.
For every Gecko Moria falling out of the window, they are minus 1 point.
If the user let Luffy collide with Gecko Moria, they will loose and exit the game.
If they reach 20 points (or other number defined by the NUM_WIN), they will win.

Bonus points:
1. Main menu, instructions menu and quit button
2. Background music: we used playsound package. It runs perfectly on Mac. However, we may receive an error in the Shell on Window.
The code should still run on both systems.

Assistance document:
    We searched google to import the playsound package and its syntax.
    
    We helped Chau Tran, Samyam Bista, and Nhi Nguyen to import the playsound package.
'''

from graphics2 import *
import time
import random
import math
import sys
from playsound import playsound

ENEMY_SPEED = 5
HERO_SPEED = 50
FIREBALL_SPEED = 10
NUM_WIN = 1
STALL_TIME = 0.05
WINDOW_WIDTH = 666
WINDOW_HEIGHT = 666

def background(window):
    """
    Creates a background on the given window
    
    Parameters:
    - window: the GraphWin object where the background will be inserted
    
    Returns:
    - The background Image
    """
    backgroundImg = Image(Point(WINDOW_WIDTH/2,WINDOW_HEIGHT/2), 'background.png')
    backgroundImg.draw(window)
    
    return backgroundImg

def button(window, x1, y1, x2, y2, color):
    """
    Creates a button on a given window
    
    Parameters:
    - window: the GraphWin object where the button will be drawn.
    - x1, y1: Coordinate of the top-left corner of the rectangle button
    - x2, y2: Coordinate of the botton-right corner of the button
    - color: The color that will be fill in the button
    
    Returns:
    - The Rectangle object representing the button.
    """
    button = Rectangle(Point(x1, y1), Point(x2, y2))
    button.setFill(color)
    button.draw(window)
    
    return button

def buttonText(window, button, text):
    """
    Creates the text on a given button
    
    Parameters:
    - window: the GraphWin object where the button will be drawn.
    - button: the button that will have the text on it
    - text: the button text
    
    Returns:
    - the text on the button
    """
    buttonText = Text(button.getCenter(), text)
    buttonText.draw(window)
    
    return buttonText

def mainMenu(window):
    """
    Sets up the main menu for the game.

    Parameters:
    - window: The GraphWin object for the game window.

    Returns:
    - A tuple containing the start button, instructions button, quit button,
      title text, and their corresponding text objects.
    """
    
    background(window)
    
    title = Text(Point(WINDOW_WIDTH / 2, 100), "Luffy vs Gecko Moria")
    title.setSize(36)
    title.setTextColor('white')
    title.setStyle('bold')
    title.draw(window)
    
    startButton = button(window, 250, 200, 400, 250, 'white')
    startButtonText = buttonText(window, startButton, 'Start Game')
    
    instructionsButton = button(window, 250, 300, 400, 350, 'white')
    instructionsButtonText = buttonText(window, instructionsButton, 'Instructions')
    
    quitButton = button(window, 250, 400, 400, 450, 'white')
    quitButtonText = buttonText(window, quitButton, 'Quit')

    return startButton, instructionsButton, quitButton, title, startButtonText, instructionsButtonText, quitButtonText

def instructionsMenu(window):
    """
    Sets up the instructions menu for the game.

    Parameters:
    - window: The GraphWin object for the game window.

    Returns:
    - The back button from the instructions menu.
    """
    
    background(window)
    
    instructionsText = Text(Point(WINDOW_WIDTH / 2, 100), "Instructions")
    instructionsText.setSize(24)
    instructionsText.setTextColor('white')
    instructionsText.setStyle('bold')
    instructionsText.draw(window)

    controls = Text(Point(WINDOW_WIDTH / 2, 200),
                    "Control Luffy, the hero, by clicking LEFT and RIGHT of the hero to move.\n"
                    "Press SPACE to shoot the devil fruit and defeat Gecko Maria,\n"
                    "or else he will steal your shadow.")
    controls.setTextColor('white')
    controls.setSize(16)
    controls.draw(window)
    
    backButton = button(window, 250, 350, 400, 400, 'white')
    backButtonText = buttonText(window, backButton, 'Back')

    return backButton

def createGameWindow():
    """
    Creates and sets up the game window.

    Returns:
    - The GraphWin object for the game window.
    """
    window = GraphWin("Gomu Gomu Nooo", WINDOW_WIDTH, WINDOW_HEIGHT)
    
    background(window)
    
    return window

def addEnemyToWindow(window):
    """
    Adds an enemy image to the game window at a random x position at the top.

    Parameters:
    - window: The GraphWin object where the enemy will be drawn.

    Returns:
    - The Image object representing the enemy.
    """
    xPosition = random.randrange(0, WINDOW_WIDTH - 5)
    enemyImg = Image(Point(xPosition, 0), 'enemy.png')
    enemyImg.draw(window)
    return enemyImg

def addFireballToWindow(window, hero):
    """
    Adds a fireball image to the game window at the hero's position.

    Parameters:
    - window: The GraphWin object where the fireball will be drawn.
    - hero: The Image object representing the hero.

    Returns:
    - The Image object representing the fireball.
    """
    fireballImg = Image(hero.getCenter(), 'balls.png')
    fireballImg.draw(window)
    return fireballImg

def moveEnemies(enemyImgList):
    """
    Moves all enemies downwards in the game window.

    Parameters:
    - enemyImgList: A list of Image objects representing enemies.
    """
    for enemy in enemyImgList: 
        enemy.move(0, ENEMY_SPEED)
        
def moveFireballs(fireballs):
    """
    Moves all fireballs upwards in the game window.

    Parameters:
    - fireballs: A list of Image objects representing fireballs.
    """
    for fireball in fireballs:
        fireball.move(0, -FIREBALL_SPEED)  # Move the fireball upwards

def moveHero(window, heroImg):
    """
    Moves the hero based on mouse position within specific bounds.

    Parameters:
    - window: The GraphWin object for the game window.
    - heroImg: The Image object representing the hero.
    """
    mouseMove = window.checkMouse()
    heroCenter = heroImg.getCenter()
    heroX = heroCenter.getX()
    heroY = heroCenter.getY()
    
    heroHeight = heroImg.getHeight()
    heroHeightRadius = heroHeight / 2
    yMouseMax = heroY + heroHeightRadius
    yMouseMin = heroY - heroHeightRadius
    
    heroWidth = heroImg.getWidth()
    heroWidthRadius = heroWidth / 2
    xMouseMax = heroX + heroWidthRadius
    xMouseMin = heroX - heroWidthRadius
    
    if mouseMove is not None:
        xMouse = mouseMove.getX()
        yMouse = mouseMove.getY()
        if yMouse < yMouseMax and yMouse > yMouseMin:
            if xMouse > xMouseMax:
                heroImg.move(HERO_SPEED, 0)
            elif xMouse < xMouseMin:
                heroImg.move(-HERO_SPEED, 0)
                
def distanceBetweenPoints(point1, point2):
    """
    Calculates the distance between two points.

    Parameters:
    - point1: The first Point object.
    - point2: The second Point object.

    Returns:
    - The distance between the two points as a float.
    """
    dx = point2.getX() - point1.getX()
    dy = point2.getY() - point1.getY()                     
    return math.sqrt(dx**2 + dy**2)

def losingPoint(enemyImg, score, enemyList):
    """
    Checks if an enemy has moved off the bottom of the screen,
    and updates the score accordingly.

    Parameters:
    - enemyImg: The Image object representing the enemy.
    - score: The current score as an integer.
    - enemyList: A list of Image objects representing enemies.

    Returns:
    - The updated score as an integer.
    """

    enemyCenter = enemyImg.getCenter()
    enemyY = enemyCenter.getY() - enemyImg.getHeight() / 2
    
    if enemyY > WINDOW_HEIGHT:
        score -= 1
        enemyList.remove(enemyImg)  
    return score

def checkCollision(object1, object2):
    """
    Checks if two objects are colliding based on their centers.

    Parameters:
    - object1: The first Image object.
    - object2: The second Image object.

    Returns:
    - True if the objects are colliding, False otherwise.
    """
    return distanceBetweenPoints(object1.getCenter(), object2.getCenter()) < 50  # Adjust collision threshold

def gameLoop(window, hero):
    """
    Main game loop where the game is played.

    Parameters:
    - window: The GraphWin object for the game window.
    - hero: The Image object representing the hero.

    """
    score = 0
    missedEnemyCount = 0
    enemyList = []
    fireballs = []
    directions = Text(Point(333, 650), f'Points: {score}')
    directions.setSize(16)
    directions.setTextColor('white')
    directions.setStyle('bold')
    directions.draw(window)

    playsound('Background Music.mp3', False)    

    while True:
        
        if random.randrange(100) < 5:
            enemy = addEnemyToWindow(window)
            enemyList.append(enemy)
            
        moveEnemies(enemyList)
        moveFireballs(fireballs)  # Move fireballs each frame

        for enemyImg in enemyList[:]:  # Iterate over a copy of the list
            score = losingPoint(enemyImg, score, enemyList)
            directions.setText(f'Points: {score}')
            
            # Check collision with hero
            if checkCollision(hero, enemyImg):
                background(window)
                
                heroSad = Image(Point(WINDOW_WIDTH/2,WINDOW_HEIGHT/2), 'Sad Luffy.png')
                heroSad.draw(window)
                
                losingMessage = Text(Point(WINDOW_WIDTH / 2, 200),
                    "GAME OVER!\n"
                    "Oh no Luffy got caught :<\n"
                    "Now Gecko Moria is gonna steal your shadow.")

                losingMessage.setTextColor('white')
                losingMessage.setStyle('bold')
                losingMessage.setSize(26)
                losingMessage.draw(window)
                
                time.sleep(4)
                exit(1)  # End the program
            
            # Check collision with fireballs
            for fireball in fireballs[:]:
                if checkCollision(fireball, enemyImg):
                    score += 1
                    directions.setText(f'Points: {score}')
                    enemyList.remove(enemyImg)
                    fireballs.remove(fireball)
                    enemyImg.undraw()
                    fireball.undraw()
                    break  # Exit the loop after removing the enemy and fireball
        
        # Launch fireball on key press
        if window.checkKey() == 'space':
            fireball = addFireballToWindow(window, hero)
            fireballs.append(fireball)

        if score == NUM_WIN:
            background(window)
            
            heroHappy = Image(Point(WINDOW_WIDTH/2,WINDOW_HEIGHT/2), 'Happy Luffy.png')
            heroHappy.draw(window)
            
            winningMessage = Text(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT/2), "You win! You're the best! ")
            winningMessage.setSize(36)
            winningMessage.setTextColor('white')
            winningMessage.setStyle('bold')
            winningMessage.draw(window)
            
            break
        
        moveHero(window, hero)
        time.sleep(STALL_TIME)
        
    time.sleep(4)  # Pause before closing the game
    exit(1) #Exit the game

def main():
    window = GraphWin("Gomu Gomu Noooo!!!!!!", WINDOW_HEIGHT, WINDOW_WIDTH)
    window.setBackground("white")
    
    startButton, instructionsButton, quitButton, title, startText, instructionsText, quitText = mainMenu(window)
    
    while True:
        clickPoint = window.getMouse()
        
        # Check if start game Button is clicked:
        if startButton.getP1().getX() < clickPoint.getX() < startButton.getP2().getX() and startButton.getP1().getY() < clickPoint.getY() < startButton.getP2().getY():
            window.close()
            gameWindow = createGameWindow( )
            hero = Image(Point(333, 580), "hero.png")
            hero.draw(gameWindow)
            gameLoop(gameWindow, hero)
            break
        
        #Check if instructions button is clicked:
        elif instructionsButton.getP1().getX() < clickPoint.getX() < instructionsButton.getP2().getX() and instructionsButton.getP1().getY() < clickPoint.getY() < instructionsButton.getP2().getY():
            
            title.undraw()
            startButton.undraw()
            instructionsButton.undraw()
            quitButton.undraw()
            startText.undraw()
            instructionsText.undraw()
            quitText.undraw()
            
            backButton = instructionsMenu(window)

            while True:
                clickPoint = window.getMouse()
                # Check if Back Button is clicked
                if backButton.getP1().getX() < clickPoint.getX() < backButton.getP2().getX() and \
                   backButton.getP1().getY() < clickPoint.getY() < backButton.getP2().getY():
                    
                    window.clear()
                    startButton, instructionsButton, quitButton, title, startText, instructionsText, quitText = mainMenu(window)
                    break
                
        #Check if quit button is clicked
        elif quitButton.getP1().getX() < clickPoint.getX() < quitButton.getP2().getX() and \
             quitButton.getP1().getY() < clickPoint.getY() < quitButton.getP2().getY():
             
             window.close()
             sys.exit(1)

main()