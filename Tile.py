import math

class Tile:
    def __init__(self, position, number):
    	#position should be a list [i,j]
    	#isMine = true means it is a mine
    	self.clicked = False
    	self.number = number
    	self.position = position
    	self.isMine = True
    	if self.number < 9:
    		self.isMine = False

