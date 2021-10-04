##Initialization of variable to recieve the players choices
import config
import pickle, items

##character class

##Handles the creation of a player and the player object
def characterInit():

    player_choice_holder = "" #holds the race and class options
    temp_choice = "" #handles the confirmation for the character creator
    character_class = ""
    char_race = ""
    char_name = " "
    hitPoints = 0
    char_defense = 0
    con_bonus = 0
    str_bonus = 0
    dex_bonus = 0
    int_bonus = 0
    luck_bonus = 0

    #Has player create character in the order of Class, Race, and Name
    print('''
    --------------------------------
            Character Creator
    --------------------------------
    ''')
    while True:
        print("            Choose a class\n     Cleric\n        Wizard\n        Warrior")
        player_choice_holder = input(" >>").lower()
        if player_choice_holder == "cleric":
            print("""Through the power of their god, the Cleric can sustain 
                    themselves in battle with healing powers.""")
            print("Choose this class? (y/n)")
            temp_choice = input(" >>")
            if temp_choice.lower() == "y":
                character_class = player_choice_holder
                hitPoints = 25
                char_defense = 5
                break          
        elif player_choice_holder == "wizard":
            print("""The wizard devestates enemies with spells.
                    They have the ability to hit multiple enemies
                    at once.""")
            print("Choose this class? (y/n)")
            temp_choice = input(" >>")
            if temp_choice.lower() == "y":
                character_class = player_choice_holder
                hitPoints = 20
                char_defense = 5
                break   
        elif player_choice_holder == "warrior":
            print("""The warrior utilizes their martial training to
                    devestate foes, they are unrivaled in skill.""")
            print("Choose this class? (y/n)")
            temp_choice = input(" >>")
            if temp_choice.lower() == "y":
                hitPoints = 30
                char_defense = 10
                character_class = player_choice_holder
                break   
    while True:
        print("Choose a race\n   Human\n    Elf\n   Orc\n")
        player_choice_holder = input(" >>").lower()
        if player_choice_holder == "human":
            print("""Humans are adaptable, able to live in many enviroments
                  their many cities have no problems expanding.""")
            print("Choose this race? (y/n)")
            temp_choice = input(" >>")
            if temp_choice.lower() == "y":
                char_race = player_choice_holder
                luck_bonus = 5
                break         
        if player_choice_holder == "elf":
            print("""One of the oldest races to live with extreme
                  longevity, this has overed them great wisdom 
                  over the years.""")
            print("Choose this race? (y/n)")
            temp_choice = input(" >>")
            if temp_choice.lower() == "y":
                char_race = player_choice_holder
                int_bonus = 5
                break         
        if player_choice_holder == "orc":
            print("""Hardy and strong, orcs are fiercesom creatures 
                    to be sure. The mountains are their home but 
                    sometimes outcasts will wander down.""")
            print("Choose this race? (y/n)")
            temp_choice = input(" >>")
            if temp_choice.lower() == "y":
                char_race = player_choice_holder
                str_bonus = 3
                con_bonus = 2
                break       
    while True:
        print("What would you like to name your character?")
        char_name = input(" >>")
        temp_choice = input("Confirm this name? (y/n)").lower()
        if temp_choice == "y":
            break


    #config.character = config.PlayerCharacter(character_class, char_race, level=1, xp=0, name=char_name, backpack=[], helmet=None, breastplate=None, leggings=None, gloves=None, footwear=None, defense=char_defense, weaponI=None, weaponII=None, hp=hitPoints, luck=luck_bonus, constitution=con_bonus, strength=str_bonus, dexterity=dex_bonus, intelligence=int_bonus)

    config.character.char_class = character_class
    config.character.race = char_race
    config.character.level = 1
    config.character.xp = 0
    config.character.name = char_name
    config.character.weaponI = items.Weapon("Starter Sword", "Shortsword", 0, 0, "Chipped and rusty, it won't do much.", 1, "None", 0)
    config.character.hp = hitPoints
    config.character.luck = luck_bonus
    config.character.constitution = con_bonus
    config.character.strength = str_bonus
    config.character.dexterity = dex_bonus
    config.character.intelligence = int_bonus

    with open("playerFile", "wb") as f:
        pickle.dump(config.character, f)