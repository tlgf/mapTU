#!/usr/bin/python
'''
   filename: mapTU.py
       date: 2015-11-20
description: generates a 2D space using Tkinter canvas for odometry
             simulations
     author: T Flynn
'''

print 'mapTU version 0.1'
print 'loading...'

userHeight = input('Enter map height: ')
userWidth = input('Enter map width: ')
gridSetting = input('Type yes for grid overlay: ')

if (gridSetting == 'yes'):
    gridSetting = 'grid'

# DEPENDENCIES
from aMap import * #Get EVERYTHING

# GLOBALS
Top = Tkinter.Tk()

# OBJECTS
MapOne = AnewMap('mapTU', Top, userHeight, userWidth)
ParticleOne = AnewParticle('vehicleA', [100, 200])

# configuration data 
ParticleOne.info()
MapOne.info()

# BEGIN
MapOne.initiate(gridSetting, 10)

# MAIN LOOP 
Top.mainloop()
