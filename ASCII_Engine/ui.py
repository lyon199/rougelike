#shows various stats to the player
class Ui:
    def __init__(self, ascii_display):
        self.display = ascii_display

    def render_obj(self, obj):
        concat_str = obj.string+str(obj.var)
        x = obj.x
        y = obj.y
        for letter in concat_str:
            self.display.display[x][y] = letter
            y+=1

    def print(self):
        for i in range(self.display.rows):
            for j in range(self.display.cols):
                print(self.display.display[i][j], sep='', end='')
            print("")