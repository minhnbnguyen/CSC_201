"""
 Name: Minh Nguyen
 Date: Oct 12, 2024
 Course: CSC 201
 Assignment: Project 2
 
 Description: This program reads a text file with an art extension and draws
              the "pointillistic" version of an image from the data in the file.
              The largest dimension is specified and the smaller dimension set
              proportionally.   
     
"""
from graphics2 import *
import tkinter as tk
from tkinter import filedialog

MAX_WINDOW_DIMENSION = 600

def main():
    #allows you to choose a file
    root = tk.Tk()
    root.withdraw()
    artFileName = filedialog.askopenfilename()
#    artFileName = 'gallery/fall_retangular_scene.art' # use this code if the file chooser doesn't work
    
    #add your code here
    # error message
    fileType = artFileName[-3:]
    if fileType != 'art':
        print("Invalid file format. Must choose a 'art' file.")
        print('Ending execution.')
        exit(-1)
    
    # read the first 2 lines
    fin = open(artFileName, 'r')
    dimension = fin.readline()
    dimensionList = dimension.split()
    background_color = int(fin.readline())
    
    # open GraphWin window
    width = int(dimensionList[0])
    height = int(dimensionList[1])
    
    if height < width:
        heightScaled = MAX_WINDOW_DIMENSION * (height/width)
        widthScaled = MAX_WINDOW_DIMENSION
    elif height > width:
        widthScaled = MAX_WINDOW_DIMENSION * (width/height)
        heightScaled = MAX_WINDOW_DIMENSION
    else: #height = width
        heightScaled = MAX_WINDOW_DIMENSION
        widthScaled = MAX_WINDOW_DIMENSION
        
    win = GraphWin('Art Viewer', widthScaled, heightScaled)
    
    if background_color == 1:
        win.setBackground('white')
    else:
        win.setBackground('black')
    
    # draw circles
    for line in fin:
        circlesList = line.split()
        xCenter = int(circlesList[0])
        yCenter = int(circlesList[1])
        radius = int(circlesList[2])
        red = int(circlesList[3])
        green = int(circlesList[4])
        blue = int(circlesList[5])
        
        xCenter = xCenter * (widthScaled/width)
        yCenter = yCenter * (heightScaled/height)
            
        randomCircle = Circle(Point(xCenter, yCenter), radius)
        randomCircle.draw(win)
        randomCircle.setFill(color_rgb(red, green, blue))
        randomCircle.setOutline(color_rgb(red, green, blue))
        
    print('Picture completed.')
    fin.close()
main()