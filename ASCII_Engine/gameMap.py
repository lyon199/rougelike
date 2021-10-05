#Where player movements will take place
class GameMap:
    def __init__(self, ascii_display, objects_stored=[]):
        self.display = ascii_display
        self.objs = objects_stored

    def print(self):
        for i in range(self.display.rows):
            for j in range(self.display.cols):
                print(self.display.display[i][j], sep='', end='')
            print("")