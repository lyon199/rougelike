#the basis for the array for both the gamemap and the ui classes

import os

class AsciiDisplay:
    def __init__(self, cols, rows, blank_char='*'):
        self.cols = cols
        self.rows = rows
        self.blank_char = blank_char
        self.display = []

        for x in range(rows):
            list = []
            for y in range(cols):
                list.append(blank_char)
            self.display.append(list)

    def print(self):
        for x in range(self.rows):
            for y in range(self.cols):
                print(self.display[x][y], sep="", end="")
            print("")
    
    #Takes one int argument, sets the border of the GameMap to a different character based on the number chosen. 
    # Defaults to no border which sets it to the blank_char declared in the GameMap constructor.
    def set_border(self, border_type=0):
        available_borders = [[self.blank_char, self.blank_char],['-','|'],['.','.']]
        for x in range(self.rows):
            self.display[x][0] = available_borders[border_type][1]
            self.display[x][self.cols-1] = available_borders[border_type][1]
        for x in range(self.cols):
            self.display[0][x] = available_borders[border_type][0]
            self.display[self.rows-1][x] = available_borders[border_type][0]
