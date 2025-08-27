
# lists and functions go here
inventory=[]
equiplist=[]
itemlist=["sword", "shield", "potion", "boot"]
eventtypes=["fight", "freeitem", "camp",]
# enemies
enemies=[{"name": "Goblin", "atk": 1, "blk": 0, "hel": 5, "dmg": 1, "agi":1}, {"name": "Orc", "atk": 2, "blk": 1, "hel": 10, "dmg": 2, "agi":0},]

import random

# once an item is equipped, i can use this function to apply its effects to player stats
def applyequips():
    global atk, blk, agi, hel, dmg
    for item in equiplist:
        if item == "sword":
            atk += 1
            dmg += 1
        elif item == "shield":
            blk += 1
        elif item == "potion":
            hel += 5
        elif item == "boot":
            agi += 1

# function to be called when input is invalid, needs while true loop around question and breaks after successful inputs to work properly
def invalid_input():
    input("Invalid input. Please reinput your choice.")
    return

# function to give player a chance to get an item after defeating an enemy
def grantitem():
    global inventory
    global equiplist
    if enemy["name"] == ("Goblin","Orc",):
        if enemy["hel"] <= 0:
            if enemy["name"] == "Goblin":
                itemchance=random.choices([True, False], weights=[7,3], k=1)[0]
            elif enemy["name"] == "Orc":
                itemchance=random.choices([True, False], weights=[10,3], k=1)[0]
        elif enemy["hel"] > 0:
            if enemy["name"] == "Goblin":
                itemchance=random.choices([True, False], weights=[3,7], k=1)[0]
            elif enemy["name"] == "Orc":
                itemchance=random.choices([True, False], weights=[5,8], k=1)[0]
    else:
        itemchance=True
    if itemchance == True:
        newitem=random.choices(itemlist, weights=[0.5, 0.3, 0.1, 0.1], k=1)[0]
        input("You found a {} on the defeated enemy!".format(newitem))
        inventory.append(newitem)
        while True:
            step3 = input("Would you like to equip it? (yes/no): ").strip().lower()
            if step3 == "yes":
                equiplist.append(newitem)
                input("You equip the {}.".format(equiplist[-1]))
                applyequips()
                break
            elif step3 == "no":
                input("You leave the {} in your inventory.".format(newitem))
                inventory.append(newitem)
                break
            else:
                invalid_input()
    else:
        input("The enemy had no items.")

def fight():
    global enemy
    input("...And something jumps out of the bushes!")
    enemychoice=random.choices(enemies, weights=[10,6], k=1)[0]
    enemy=enemychoice.copy()
    input("it's a {}!".format(enemy["name"]))
    while enemy["hel"] > 0:
        escaped=playerturn()
        if escaped:
            return
        if enemy["hel"] <= 0:
            input("The {} has been defeated!".format(enemy["name"]))
            grantitem()
            return
        enemyturn()

def playerturn():
    while True:
        playeraction=input("Your turn! Will you attack/block/escape?")
        if playeraction == "attack":
            enemyblkcheck=random.randint(-1, 1)+(enemy["blk"])
            if enemyblkcheck <= atk:
                dmgcheck=random.randint(0, 1)+(dmg)
                enemy["hel"] -= (dmgcheck)
                input("You hit the {} for {} damage!".format(enemy["name"], dmgcheck))
                input("The {} has {} health remaining.".format(enemy["name"], enemy["hel"]))   
            else:
                input("You missed!")
            return False
        elif playeraction == "block":
            global blk
            blk += 1
            input("You brace for the {}'s attack, increasing your block chance!".format(enemy["name"]))
            return False
        elif playeraction == "escape":
            if random.randint(-1, 1)+(enemy["agi"]) <= agi:
                input("You successfully escaped the {}!".format(enemy["name"]))
                return True
            else:
                input("You failed to escape!")
            return False
        else:
            invalid_input()

def enemyturn():
    global hel
    if enemy["hel"] <= 0:
        return
    if enemy["hel"] == 1:
        input("The {} is trying to escape!".format(enemy["name"]))
        if random.randint(-3, 1)+(enemy["agi"]) <= agi:
            input("You successfully stopped the {} from escaping!".format(enemy["name"]))
            return
        else:
            input("The {} escaped!".format(enemy["name"]))
            enemy["hel"] = 0
            return
    enemyaction=random.choices(["attack", "block"], weights=[10,1], k=1)[0]
    if enemyaction == "attack":
        blkcheck=random.randint(-1, 1)+(blk)
        if blkcheck <= enemy["atk"]:
            enemydmgcheck=random.randint(0, 1)+(enemy["dmg"])
            hel -= (enemydmgcheck)
            input("The {} hits you for {} damage!".format(enemy["name"], enemydmgcheck))
            input("You have {} health remaining.".format(hel))
            if hel <= 0:
                input("You have been defeated! Game over.")
                exit()
        else:
            input("The {} missed!".format(enemy["name"]))
    else:
        enemy["blk"] += 1
        input("The {} braces itself for your attack, increasing it's block chance!".format(enemy["name"]))

        
# player stats (atk=attack success chance, blk=block success chance, agi=escape success chance, hp=health points, dmg=damage)
atk=1
blk=1
agi=1
hel=10
dmg=1

# game starts here
input("Hello, this is a text and probability based fighting game for my python assesment. (press ENTER/RETURN to continue)")
print("Light. That is all you see, as your mind slowly surfaces from the depths of REM sleep.")
input("Sitting up, you see that you are seemingly alone in an empty forest.")
print("Recognizing your surroundings, you remember that you were on your way to a nearby village when bandits ambushed you and knocked you out.")
print("If you can get to the village, you can get help to defeat the bandits!")
input("...After a bit more sitting, perhaps...")
input("...")
input(".....")
input("..........")
while True:    
    step1 = input("would you like to take a look around? (yes/no): ").strip().lower()
    if step1 == "yes":
        startitem=random.choices(itemlist, weights=[0.5, 0.3, 0.1, 0.1], k=1)[0]
        print("As you glance around, you notice a {} lying on the ground.".format(startitem))
        step2 = input("Equip? (yes/no): ").strip().lower()
        if step2 == "yes":
            equiplist.append(startitem)
            input("You equip the {}.".format(equiplist[-1]))
        elif step2 == "no":
            input("You leave the {} on the ground.".format(startitem))
        input("looking around a bit more, you notice that some of the nearby bush is rustling strangely.")
        break
    elif step1 == "no":
        input("Continuing to sit for a while, you eventually hear a loud rustling in the bushes nearby.")
        break
    else:
        invalid_input()
fight()

applyequips()
events=random.randint(1, 15)
for i in range(events):
    eventtype=random.choices(eventtypes, weights=[10,4,4], k=1)[0]
    if eventtype == "fight":
        fight()
        input("After defeating your enemy, you continue on your way.")
    if eventtype == "freeitem":
        freeitem=random.choices(itemlist, weights=[0.5, 0.3, 0.1, 0.1], k=1)[0]
        input("...And you find a {} lying on the ground in the exact centre of the clearing.".format(freeitem))
        while True:
            step4 = input("Equip? (yes/no): ").strip().lower()
            if step4 == "yes":
                equiplist.append(freeitem)
                input("You equip the {}.".format(equiplist[-1]))
                applyequips()
            elif step4 == "no":
                input("You leave the {} on the ground.".format(freeitem))
            else:
                invalid_input()
            input("You continue on your way.")
    if eventtype == "camp":
        input("...And you find a safe clearing to rest in for a while, with a burnt out firepit in the centre.")
        while True:
            firepit = input("Do you want to try lighting the firepit? (yes/no)")
            if firepit == "yes":
                fire=random.randint(1, 10)
                if fire >= 4:
                    hel += 5
                    input("...And you succeed in lighting the firepit!")
                    input("You feel refreshed, and gain 5 health!")
                    break
                else:
                    input("...But you don't really succeed, and eventually get a splinter from the firewood, so you give up.")
                    break
            elif firepit == "no":
                input("You decide not to try lighting the firepit.")
                break
            else:
                invalid_input()
        input("After resting for a while, you continue on your way.")
    applyequips()
    print("You have {} health remaining.".format(hel))
    print("You have {} events remaining before you reach the village.".format(events-(i+1)))
    print("After this check of yourself, and where you are, you begin moving again.")
    input("After a while more walking, you come across a clearing...")
