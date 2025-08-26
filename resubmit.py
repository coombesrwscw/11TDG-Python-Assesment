
# lists and functions go here
inventory=[]
equiplist=[]
itemlist=["sword", "shield", "potion", "boot"]
# enemies
enemies=[{"name": "Goblin", "atk": 1, "blk": 0, "hel": 5, "dmg": 1, "agi":1}, {"name": "Orc", "atk": 2, "blk": 1, "hel": 10, "dmg": 2, "agi":0},]

import random

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

def invalid_input():
    input("Invalid input. Please reinput your choice.")
    return

def grantitem():
    global inventory
    global equiplist
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
    if itemchance == True:
        newitem=random.choices(itemlist, weights=[0.5, 0.3, 0.1, 0.1], k=1)[0]
        input("You found a {} on the defeated enemy!".format(newitem))
        inventory.append(newitem)
        step3 = input("Would you like to equip it? (yes/no): ").strip().lower()
        if step3 == "yes":
            equiplist.append(newitem)
            input("You equip the {}.".format(equiplist[-1]))
            applyequips()
        elif step3 == "no":
            input("You leave the {} in your inventory.".format(newitem))
            inventory.append(newitem)
        else:
            invalid_input()
    else:
        input("The enemy had no items.")

def fight():
    global enemy
    input("Something appears in front of you!")
    enemychoice=random.choices(enemies, weights=[10,6], k=1)[0]
    enemy=enemychoice.copy()
    input("it's a {}!".format(enemy["name"]))
    while enemy["hel"] > 0:
        playerturn()
        enemyturn()

def playerturn():
    playerturn=input("Your turn! Will you attack/block/escape?")
    if playerturn == "attack":
            enemyblkcheck=random.randint(-1, 1)+(enemy["blk"])
            if enemyblkcheck <= atk:
                dmgcheck=random.randint(0, 1)+(dmg)
                enemy["hel"] -= (dmgcheck)
                input("You hit the {} for {} damage!".format(enemy["name"], dmgcheck))
                input("The {} has {} health remaining.".format(enemy["name"], enemy["hel"]))   
            else:
                input("You missed!")
    elif playerturn == "block":
            global blk
            blk+=1
            input("You brace for the {}'s attack, increasing your block chance!".format(enemy["name"]))
    elif playerturn == "escape":
            if random.randint(-1, 1)+(enemy["agi"]) <= agi:
                input("You successfully escaped the {}!".format(enemy["name"]))
                return
            else:
                input("You failed to escape!")
    if enemy["hel"] <= 0:
        input("The {} has been defeated!".format(enemy["name"]))
        grantitem()

def enemyturn():
    if enemy["hel"] > 1:
        enemyturn=random.choices(["attack", "block"],weights=[10,1])
        if enemyturn == "attack":
            blkcheck=random.randint(-1, 1)+(blk)
            if blkcheck <= enemy["atk"]:
                global hel
                enemydmgcheck=random.randint(0, 1)+(enemy["dmg"])
                hel -= (enemydmgcheck)
                input("The {} hit you for {} damage!".format(enemy["name"], enemydmgcheck))
            if hel <= 0:
                input("You have been defeated by the {}...".format(enemy["name"]))
                input("Game Over. Press ENTER/RETURN to exit.")
                exit()
            else:
                input("The {} missed!".format(enemy["name"]))
        elif enemyturn == "block":
            enemy["blk"]+=1
            input("The {} braces for your attack, increasing its block chance!".format(enemy["name"]))
    elif enemy["hel"] == 1:
        input("The {} is trying to escape!".format(enemy["name"]))
        if random.randint(-3, 1)+(enemy["agi"]) <= agi:
            input("You successfully stopped the {} from escaping!".format(enemy["name"]))
        else:
            input("The {} escaped!".format(enemy["name"]))

# player stats (atk=attack success chance, blk=block success chance, agi=escape success chance, hp=health points, dmg=damage)
atk=1
blk=1
agi=1
hel=10
dmg=1

# game starts here
input("Hello, this is a text and probability based fighting game for my python assesment. (press ENTER/RETURN to continue)")
input("Light. That is all you see, as your mind slowly surfaces from the depths of REM sleep.")
input("Sitting up, you see that you are seemingly alone in an empty forest.")
while True:    
    step1 = input("would you like to take a look around? (yes/no): ").strip().lower()
    if step1 == "yes":
        startitem=random.choices(itemlist, weights=[0.5, 0.3, 0.1, 0.1], k=1)[0]
        input("As you glance around, you notice a {} lying on the ground.".format(startitem))
        step2 = input("Equip? (yes/no): ").strip().lower()
        if step2 == "yes":
            equiplist.append(startitem)
            input("You equip the {}.".format(equiplist[-1]))
            break

        elif step2 == "no":
            input("You leave the {} on the ground.".format(startitem))
            break

        input("looking around a bit more, you notice that some of the nearby bush is rustling strangely.")

    elif step1 == "no":
        input("Continuing to sit for a while, you eventually hear a loud rustling in the bushes nearby.")
        break

    else:
        invalid_input()

applyequips()
fights=random.randint(1, 15)
for i in range(fights):
    fight()
