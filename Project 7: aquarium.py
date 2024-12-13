'''
Name(s): Minh Nguyen
CSC 201

The program displays a virtual aquarium with animated fish and floating bubbles.
It utilizes a Fish and Bubble class.
    
'''


from graphics2 import *
import random
import time

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
DEFAULT_FISH_NUM = 10
DEFAULT_BUBBLE_NUM = 25
MAX_COLOR_NUM = 255

#***********
# FISH CLASS
#***********

class Fish:
    def __init__(self, x, y, color, speed, count):
        self.fishBody = Oval(Point(x - 30, y - 20), Point(x + 30, y + 20))
        self.fishTail = Oval(Point(x - 20, y - 30), Point(x - 5, y + 30))
        self.fishBody.setFill(color)
        self.fishTail.setFill(color)
        self.fishEye = Circle(Point(x + 20, y), 3)
        self.fishEye.setFill('white')
        self.fishSpeed = speed
        self.count = count
    
    def draw(self, win):
        self.fishTail.draw(win)
        self.fishBody.draw(win)
        self.fishEye.draw(win)
    
    def move(self):
        self.count = self.count + 1
        
        if self.count < 10:
            dy = -1
        elif self.count < 20:
            dy = 1
        else:
            self.count = 0
            dy = -1
            
        self.fishBody.move(self.fishSpeed, dy)
        fishBodyX = self.fishBody.getCenter().getX()
        
        if fishBodyX > WINDOW_WIDTH + 30:
            self.fishBody.move(- WINDOW_WIDTH - 30, dy)

        self.fishTail.move(self.fishSpeed, dy)
        fishTailX = self.fishTail.getCenter().getX()
        
        if fishTailX > WINDOW_WIDTH + 30:
            self.fishTail.move(- WINDOW_WIDTH - 30, dy)

        self.fishEye.move(self.fishSpeed, dy)
        fishEyeX = self.fishEye.getCenter().getX()
        
        if fishEyeX > WINDOW_WIDTH + 30:
            self.fishEye.move(- WINDOW_WIDTH - 30, dy)

#*****************
# 
#*************
# BUBBLE CLASS
#*************

class Bubble:
    def __init__(self, x, y, speed, count):
        self.bubble = Circle(Point(x, y), 5)
        self.bubble.setFill('white')
        self.bubbleSpeed = speed
        self.count = count
    
    def draw(self, win):
        self.bubble.draw(win)
    
    def move(self):

        self.count = self.count + 1
            
        if self.count < 10:
            dx = -1
        elif self.count < 20:
            dx = 1
        else:
            self.count = 0
            dx = -1
            
        self.bubble.move(dx, self.bubbleSpeed)
        bubbleY = self.bubble.getCenter().getY()
            
        if bubbleY < - 5:
            self.bubble.move(dx, WINDOW_HEIGHT + 5)

#*****************
# HELPER FUNCTIONS
#*****************

def setupInput(win, point, text):
    '''
    creates an Entry box with a label
    
    Params:
        win (GraphWin): the window the Entry box and label with be drawn in.
        point (Point): the location od the center of the text label
        text (str): the words that will be used to label the Entry box
    
    Returns:
        Entry: the Entry object created
    '''
    winText = Text(point, text)
    winText.setSize(18)
    winText.draw(win)
    winBox = Entry(Point(point.getX() + 225, point.getY()), 5)
    winBox.setSize(18)
    winBox.draw(win)
    return winBox

def getInput(win):
    '''
    Allows the user to enter the number of fish and bubbles for the aquarium.
    If a value is not entered or an invalid value (like a letter) is entered,
    the default number is used for that value.
    
    Params:
        win (GraphWin): the window the Entry box is in
    
    Returns:
        (int, int): the number of fish and number of bubbles that will be drawn in the aquarium
    as a tuple
    '''
    directions = Text(Point(WINDOW_WIDTH/2 , 400), 'Enter the number of fish and bubbles, then click in the window.')
    directions.draw(win)
    fishEntry = setupInput(win, Point(300, 200), "Enter number of fish:")
    bubbleEntry = setupInput(win, Point(300, 300), "Enter number of bubbles:")
    win.getMouse()
    if fishEntry.getText().isdigit() and int(fishEntry.getText()) >= 0:
        numFish = int(fishEntry.getText())
    else:
        numFish = DEFAULT_FISH_NUM
    if bubbleEntry.getText().isdigit() and int(bubbleEntry.getText()) >= 0:
        numBubbles = int(bubbleEntry.getText())
    else:
        numBubbles = DEFAULT_BUBBLE_NUM
    fishEntry.undraw()
    bubbleEntry.undraw()
    directions.undraw()
    cover = Rectangle(Point(0, 0), Point(WINDOW_WIDTH, WINDOW_HEIGHT))
    cover.setFill("cyan")
    cover.draw(win)
    return numFish, numBubbles

def randColor():
    '''
    Returns a random color created from randomly generated red, green, and blue values
    
    Returns:
        Color: a random color
    '''
    red = random.randrange(0,MAX_COLOR_NUM + 1)
    green = random.randrange(0,MAX_COLOR_NUM + 1)
    blue = random.randrange(0,MAX_COLOR_NUM + 1)
    return color_rgb(red, green, blue)


def setupFish(numFish):
    '''
    Creates the list of fish with random position, color and speed
    
    Params:
        numFish (int): the number of fish to be added to the list
    
    Returns:
        list: the list of fish
    '''
    fishList = []
    
    for index in range(numFish):
        count = random.randrange(0, 20)
        fishX = random.randrange(WINDOW_WIDTH)
        fishY = random.randrange(30, WINDOW_HEIGHT - 31)
        fishSpeed = random.randrange(1,6)
        color = randColor()
        fish = Fish(fishX, fishY, color, fishSpeed, count)
        
        fishList.append(fish)
    
    return fishList

def setupBubbles(numBubbles):
    '''
    Creates the list of bubbles with random position and speed
    
    Params:
        numBubbles (int): the number of bubbles to be added to the list
    
    Returns:
        list: the list of bubbbles
    '''
    bubbleList = []
    
    for index in range(numBubbles):
        count = random.randrange(0, 20)   
        bubbleX = random.randrange(WINDOW_WIDTH)
        bubbleY = random.randrange(WINDOW_HEIGHT)
        bubbleSpeed = random.randrange(-5,0)
        bubble = Bubble(bubbleX, bubbleY, bubbleSpeed, count)
        
        bubbleList.append(bubble)
    
    return bubbleList

#*****
# MAIN
#*****
def main():

    # make the graphics window (use autoflush=False to update more frequently)
    # makes the animation move more smoothly
    win = GraphWin("Swimming Fish", WINDOW_WIDTH, WINDOW_HEIGHT, autoflush=False)
    win.setBackground("cyan2")
    
    numFish, numBubbles = getInput(win)
                      
    # call helper functions to setup the fish and bubble lists
    bubblesList = setupBubbles(numBubbles)
    fishList = setupFish(numFish)
    
    # draw the fish and bubbles in their initial locations
    for bubble in bubblesList:
        bubble.draw(win)
    
    for fish in fishList:
        fish.draw(win)
        
    # continue swimming until the user clicks
    keepSwimming = True
    
    while keepSwimming:
        # loop through all the fish calling move method on each fish
        for fish in fishList:
            fish.move()

        # loop through all the bubbles calling move method on each bubble
        for bubble in bubblesList:
            bubble.move()
        # The bubble are after the fish so that the bubbles are drawn in front of the fish

        
        update(50) # call update to flush the window
        # if user clicks: stop swimming
        if win.checkMouse() != None:
            keepSwimming = False

    win.close()

if __name__ == '__main__':
    main()
