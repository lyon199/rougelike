import asciiDisplay, gameMapObject, gameMaster, os

USER_STOP = ""
os.system("clear")
USER_STOP = input("Please make the terminal full screen. Hit enter to continue.")
#204, 65 - full screen columns and rows
var_map = asciiDisplay.AsciiDisplay(204, 53, " ")
var_map1 = asciiDisplay.AsciiDisplay(204, 8)
var_map.set_border(1)
var_map.print()
var_map1.print()
while True:
    print("next prompt goes here - user input after")
    take = input(">>")