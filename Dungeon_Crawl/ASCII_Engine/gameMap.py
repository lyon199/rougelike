class GameMap:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows


class GameMapObject:
    def __init__(self, char):
        self.char = char

class GameMaster:
    def __init__(self, map, ):
        self.map = map

COLUMNS = 204
ROWS = 65

game_map = []

def create_game():
    for x in range(COLUMNS):
        list = []
        for y in range(ROWS):
            list.append("*")
        game_map.append(list)

def print_map():
    for x in range(COLUMNS-1):
        for y in range(ROWS-1):
            print(game_map[x][y], sep="", end="")
