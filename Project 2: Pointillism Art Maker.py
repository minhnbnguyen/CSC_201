"""
 Name: Minh Nguyen
 Date: Oct 5, 2024
 Course: CSC 201
 Assignment: Project 2

 Description: This program begins with a gif image and creates a text file storing
              data for a "pointillistic" version of the image. The user can choose
              whether the background will be either white or black.

"""
from graphics2 import *
import random
import tkinter as tk
from tkinter import filedialog

NUM_CIRCLES = 7500
   
def main():
    # allows you to choose a file 
    root = tk.Tk()
    root.withdraw()
    filenameWithPath = filedialog.askopenfilename()
#    filenameWithPath = 'gallery/fall_retangular_scene.gif' # use this code if the file chooser doesn't work
    
    # add your code here
    # error message
    fileType = filenameWithPath[-3:]
    fileName = filenameWithPath[:-3]
    if fileType != 'gif':
        print("Invalid file format. Must choose a 'gif' file.")
        print('Ending execution.')
        exit(-1)
        
    # create an image object
    win = GraphWin ("Window", 100, 100)
    image = Image(Point(0,0), filenameWithPath)
    
    # create a new file type
    fileType = 'art'
    newFile = fileName + fileType
    fout = open(newFile, 'w')
    
    # width and height
    widthInPixels = image.getWidth()
    heightInPixels = image.getHeight()
    
    # write to file
    fout.write(f'{widthInPixels} {heightInPixels}\n')
    
    #  background color
    backgroundColor = int(input('Color for background? (1 white, 2 black) '))
    if backgroundColor == 1:
        backgroundColor == 'white'
    elif backgroundColor == 2:
        backgroundColor == 'black'
    else:
        print('Invalid color choice. Using black.')
        backgroundColor == 'black'
    
    fout.write(f'{backgroundColor}\n')
    
    # random point
    for count in range(NUM_CIRCLES):
        randomX = random.randrange(widthInPixels)
        randomY = random.randrange(heightInPixels)
        radius = random.randrange(1, 8)
        rgb = image.getPixel(randomX, randomY)
        red = rgb[0]
        green = rgb[1]
        blue = rgb[2]
        #write to file
        fout.write(f'{randomX} {randomY} {radius} {red} {green} {blue}\n')
        
    fileNameIndex = filenameWithPath.rfind('/')
    fileName = filenameWithPath[fileNameIndex+1:-3]

    print(f'File created: {fileName}art')
    print('Program ending.')
    
    fout.close()
main()
