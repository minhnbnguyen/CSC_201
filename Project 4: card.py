'''
Name: Minh Nguyen
CSC 201
Programming Project 4--Card Class

The Card class represents one standard poker card from a poker deck. Each Card has an image, rank, and suit.
The card stores its position in a graphics window. It can be drawn and undrawn, moved a distance
in the x or y directions, and determine if a point is within the boundaries of the card.

'''
from graphics2 import *
import time

class Card:
    # Add your methods above __eq__
    def __init__(self, imageFileName):
        self.imageFileName = imageFileName
        
        rankStartIndex = imageFileName.find('/') + 1
        rankEndIndex = imageFileName.find('.') - 1
        rank = int(imageFileName[rankStartIndex:rankEndIndex])
        self.rank = rank
        
        suitIndex = imageFileName.find('.')
        suit = imageFileName[suitIndex-1]
        self.suit = suit
        
        image = Image(Point(0,0), imageFileName)
        self.image = image
    
    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit
    
    def getImage(self):
        return self.image
        
    def draw(self, window):
        return self.image.draw(window)
    
    def undraw(self):
        return self.image.undraw()
        
    def isRed(self):
        if self.suit in ('h','d'):
            return True
        else:
            return False
        
    def move(self, dx, dy):
        self.image.move(dx, dy)
        
    def containsPoint(self,point):
        imageCenter = self.image.getCenter()
        imageCenterX = imageCenter.getX()
        imageCenterY = imageCenter.getY()
        
        imageHeight = self.image.getHeight()
        imageHeightRadius = imageHeight/2
        imageWidth = self.image.getWidth()
        imageWidthRadius = imageWidth/2
        
        imageMaxX = imageCenterX + imageWidthRadius
        imageMinX = imageCenterX - imageWidthRadius
        imageMaxY = imageCenterY + imageHeightRadius
        imageMinY = imageCenterY - imageHeightRadius
        
        if point.getX() < imageMaxX and point.getX() > imageMinX:
            if point.getY() < imageMaxY and point.getY() > imageMinY:
                return True
            else:
                return False
        else:
            return False
        
    def __eq__(self, cardToCompare):
        '''
        Allows users of the Card class to compare two cards using ==
        
        Params:
            cardToCompare (Card): the Card to check for equality with this Card
        
        Returns:
            True if the two cards have the same rank and suit. Otherwise, False
        '''
        return self.suit == cardToCompare.suit and self.rank == cardToCompare.rank
        
    def __str__(self):
        return f'suit = {self.suit}, rank = {self.rank}, center = {self.image.getCenter()}'
        
def main():  
    window = GraphWin("Card Class Testing", 500, 500)
    
    # create King of Hearts card
    fileName = 'cards/13h.gif'
    card = Card(fileName)

    # print card using __str__ and test getRank, getSuit, getImage
    print(card)
    print(card.getRank())
    if (isinstance(card.getRank(), int)):
        print('Rank stored as an int')
    else:
        print('Rank was not stored as an int. Fix it!')
    print(card.getSuit())
    print(card.getImage())
    print(card.isRed())
    
    # move card to center of window and display it
    card.move(250, 250)
    card.draw(window)
    
    # click only on the card should move it 100 pixels left
    point = window.getMouse()
    while not card.containsPoint(point):
        point = window.getMouse()
    card.move(-100, 0)
    
    # click only on the card should move it 200 pixels right and 100 pixels down
    point = window.getMouse()
    while not card.containsPoint(point):
        point = window.getMouse()
    card.move(200, 100)
    
    # print the card using __str__
    print(card)
    
    # stall 2 seconds
    time.sleep(2)
    
    # create 2 of Spades card
    fileName = 'cards/2s.gif'
    card2 = Card(fileName)

    # print card2 using __str__ and test getRank, getSuit
    print(card2)
    print(card2.getRank())
    print(card2.getSuit())
    print(card2.isRed())
    
    # move card2 to center of window and display it
    card2.move(250, 250)
    card2.draw(window)
    
    # stall 2 seconds then remove both cards from the window
    time.sleep(2)
    card.undraw()
    card2.undraw()
    
    # stall 2 seconds then close the window
    time.sleep(2)
    window.close()
    
if __name__ == '__main__':
    main()
        
        
