#!/usr/bin/python
'''
   filename: aMap.py
       date: 2015-11-20
description: class definition for the basic map 
     author: T Flynn
'''
# DEPENDANCIES
import Tkinter
import tkMessageBox

# GLOBALS
GRID_SCALE = 10 #pixel length of each grid cell
GRID_LINE_WIDTH = GRID_SCALE / 10 #pixel width of grid lines

#----------------------------------------------------------------
# CLASSES 
#----------------------------------------------------------------

# AnewMap is the underlying structure to create a map object using Tkinter canvas object/methods

class AnewMap:
    def __init__(self, mapName, parentWindow, height, width):
        self.mapName = mapName
        #Height and width are scaled to pixel counts 
        self.height = height * GRID_SCALE
        self.width = width * GRID_SCALE
        self.parentWindow = parentWindow
    
    #Initate configures the canvas object 
    def initiate(self, grid, debug):
        theMap = Tkinter.Canvas(self.parentWindow, bg="green", height=self.height, width=self.width, cursor="dot")
       
        # draw a grid to mark each cell on the map
        if (grid=='grid'):
            self.drawGrid(self.height, self.width, theMap)
        # place the tkCanvas in the GUI window
        theMap.pack()

     #function for overlaying a grid of cells on the canvas
    def drawGrid(self, mapHeight, mapWidth, aMapObject):
       
        numberOfLinesH = mapHeight/GRID_SCALE + 1
        numberOfLinesV = mapWidth/GRID_SCALE + 1  
        countY = 1; countX = 1
        y0 = 0; x0 = 0 
        y1 = mapHeight; x1 = mapWidth
        Hlines = []
        Vlines = []
        
        #With while loop, populate lists with line objects of vertical and horizontals
        while countY <= numberOfLinesH:
        #List of line objects with (number of cells + 1) lines
            Hlines.extend([aMapObject.create_line(x0, y0, x1, y0, width=GRID_LINE_WIDTH)])
           
            countY += 1
            y0 = y0 + GRID_SCALE

        y0 = 0 #reinitialise the coordinate value

        while countX <= numberOfLinesV:
            Vlines.extend([aMapObject.create_line(x0, y0, x0, y1, width=GRID_LINE_WIDTH)])

            countX += 1
            x0 = x0 + GRID_SCALE

    #Print current values
    def info(self):
        print(self.mapName, self.height, self.width)
#----------------------------------------------------------------
# AnewParticle creates an object containing information for the map to model a 2D particle, represented by a Tkinter canvas item        
class AnewParticle:
    def __init__(self, particleName, xiyi):
        self.name = particleName
        self.startPos = xiyi
        self.position = xiyi

   #Print current values
    def info(self):
        print('Name:', self.name)
        print('Start Position:', self.startPos)
        print('Current Positon:', self.position)
'''
     #addParticle adds a particle to the 2D space
    def addParticle(xiyi, colour):
'''        
#----------------------------------------------------------------
# MODULE TEST
if __name__ == '__main__':
    Top = Tkinter.Tk()
    mapSize = [50, 50]
    particleStart = [mapSize[0] / 2, mapSize[1]/2]

    testMap = AnewMap('testMap', Top, mapSize[0], mapSize[1])
    testParticle = AnewParticle('testParticle', particleStart)

    testMap.info()
    testParticle.info()
    testMap.initiate('grid', 10)
    Top.mainloop()    
    
