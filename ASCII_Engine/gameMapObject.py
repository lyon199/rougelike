#used to create symbols that are tied to objects on the game map 
class GameMapObject:
    def __init__(self, char, x_pos, y_pos, desc):
        self.char = char
        self.x = x_pos
        self.y = y_pos
        self.desc = desc

'''
    #inserts text at the given position
    def label(self, x, y, string):
        for letter in string:
            self.display[x][y] = letter
            y+=1
            if y == self.cols-2:
                x+=1
'''