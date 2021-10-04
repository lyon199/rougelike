#global variables hangout
import pickle

class PlayerCharacter:
    def __init__(self, char_class, race, level, xp, name, backpack, helmet, breastplate, leggings, gloves, footwear, defense, weaponI, weaponII, hp, luck, constitution, strength, dexterity, intelligence):
        self.char_class = char_class
        self.race = race
        self.level = level
        self.xp = xp
        self.name = name
        self.backpack = backpack
        self.helmet = helmet
        self.breastplate = breastplate
        self.leggings = leggings
        self.gloves = gloves
        self.footwear = footwear
        self.defense = defense
        self.weaponI = weaponI
        self.weaponII = weaponII
        self.hp = hp
        self.luck = luck
        self.constitution = constitution
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence

character = PlayerCharacter(char_class="", race="", level=1, xp=0, name="", backpack=[], helmet=None, breastplate=None, leggings=None, gloves=None, footwear=None, defense=0, weaponI=None, weaponII=None, hp=0, luck=0, constitution=0, strength=0, dexterity=0, intelligence=0)
