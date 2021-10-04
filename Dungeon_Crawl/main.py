# Import all game modules #
import character_handler as charH
import command_handler as comH
import items as items
import config
import pickle

def is_file_empty_3(file_name):
    """ Check if file is empty by reading first character in it"""
    # open file in read mode
    with open(file_name, 'rb') as read_obj:
        # read first character
        one_char = read_obj.read(1)
        # if not fetched then file is empty
        if not one_char:
           return True
    return False

#checks if "playerFile.txt" has been writen to, if so then it puts the player into game, if not it start character creation
if not is_file_empty_3("playerFile"):
    f = open("playerFile", "rb")
    config.character = pickle.load(f) 
    f.close()


config.start_character()

print("""

        Insert Title Here

""")
input("    Hit Enter To Start")

if is_file_empty_3("playerFile"):    
        charH.characterInit()

print("""""")

print(config.character.backpack)

##print(config.character.backpack[1].desc)

comH.command_taker()