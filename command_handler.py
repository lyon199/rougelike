#takes the user input and checks to see if it an acceptable function, if so then it runs that function
#to accomplish the desired task

import sys, pickle
import config

choice = " "

#gives the player a help menu for guidance
def help():
    print("""
                    Help Menu
    Type a command presented to you to navigate the game
    
        List of commands:
        help, stop
    """)

#the menu to save and quit
def stop():
    print("""

        Type snq to save and quit. 
        Otherwise continue on your
        quest.
    
    """)  

def snq():
    with open("playerFile", "wb") as f:
        pickle.dump(config.character, f)
    sys.exit()

function_dictionary = {"help" : help, "stop" : stop, "snq" : snq}

def command_taker():
    global choice
    choice = input(" >>")
    if choice in function_dictionary:
        function_dictionary[choice]()
        command_taker()
    else:
        print("Enter a valid command!")
        command_taker()