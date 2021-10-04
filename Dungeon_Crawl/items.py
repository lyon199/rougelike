import random
import config

#item parent class to handle basic information every item type has
class Items:
    def __init__(self, name, iType, value, rarity, desc):
        self.name = name
        self.iType = iType
        self.value = value
        self.rarity = rarity
        self.desc = desc

#unique items
gold = Items("Gold Piece", "Money", 1, "1", "A small round of gold, stamped with a crown.")

#weapon information for random geneation
weapon_type_library = ["Sword", "Axe", "Shortsword"]
weapon_prefix_library = ["Legendary", "Common", "Weak", "Broken"]
weapon_name_library = ["Killer", "Slayer"]
weapon_ability_library = ["Life Steal", "Sharp Edges"]

#creates the rarity
def rarity_creator():
    rand_num = random.randint(0, 100)
    rand_num += (config.character.luck * 0.05)
    if rand_num > 99:
        return 5
    elif rand_num > 85:
        return 4
    elif rand_num > 70:
        return 3
    elif rand_num > 55:
        return 2
    else:
        return 1

def ability_generator():
    pass

def desc_generator(itype, slot=""):
    if itype == "g":
        return slot
    elif itype == "w":
        return "weapon"
    else:
        return "Wtf bro"

class Weapon(Items):
    def __init__(self, name, iType, value, rarity, desc, damage, ability, ability_value):
        super().__init__(name, iType, value, desc, rarity)
        self.damage = damage
        self.ability = ability
        self.a_value = ability_value

    #generates a random weapon and returns the object
    def create_weapon():
        global weapon_type_library
        global weapon_prefix_library
        global weapon_name_library

        name = random.choice(weapon_prefix_library) + " " + random.choice(weapon_name_library)
        iType = weapon_type_library[random.randint(0, (len(weapon_type_library)-1))]
        rarity = rarity_creator()
        value = ((random.randint(1, 30)^rarity))
        desc = desc_generator("w")
        damage = 1
        if (random.randint(0, 100) > (100 - (5*rarity))): #each rarity up increases chances of getting an ability attached
            ability = random.choice(weapon_ability_library)
        else:
            ability = ""
        ability_value = 0

        return Weapon(name, iType, value, desc, rarity, damage, ability, ability_value)

#gear libraries (same purpose as the ones for weapons)

slot_list = ["helmet", "breastplate", "leggings", "gloves", "footwear"]
gear_ability_library = ["negate"]

#class for armor pieces
class Gear(Items):

    def __init__(self, name, iType, value, rarity, desc, slot, armor_Value, ability, ability_value):
        super().__init__(name, iType, value, desc, rarity)
        self.slot = slot
        self.arm_value = armor_Value
        self.ability = ability
        self.a_value = ability_value

    def create_gear():
        global slot_list

        name = ""
        iType = ""
        rarity = rarity_creator()
        value = ((random.randint(1, 30)^rarity))
        slot = random.choice(slot_list)
        desc = desc_generator("g", slot)
        armor_value = 1
        damage = 1
        if (random.randint(0, 100) > (100 - (5*rarity))): #each rarity up increases chances of getting an ability attached
            ability = random.choice(gear_ability_library)
        ability_value = 0

        return Gear(name, iType, value, desc, rarity, slot, armor_value, ability, ability_value)

#class for potions     
class Potion(Items):
    def __init__(self, name, iType, value, rarity, desc, heal_value):
        super().__init__(name, iType, value, desc, rarity)
        self.hvalue = heal_value