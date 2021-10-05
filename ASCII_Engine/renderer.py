from ASCII_Engine.uiMaster import UiMaster
import gameMap, uiMaster, os, asciiDisplay

#functioning as a main.py at the moment

def print_display():
    while True:
        var_game_map.print()
        UiMaster.print()
        print("next prompt goes here - user input after")
        take = input(">>")

USER_STOP = ""
os.system("clear")
USER_STOP = input("Please make the terminal full screen. Hit enter to continue.")
#204, 65 - full screen columns and rows

var_game_map = gameMap.GameMap(asciiDisplay.AsciiDisplay(204, 53, " "))
game_ui = uiMaster.UiMaster()
var_game_map.display.set_border(1)

print_display()