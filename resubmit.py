
# lists and functions go here
inventory=[]
equiplist=[]
itemlist=["sword", "shield", "potion", "boot"]
# enemies
enemies=["goblin"=={"name"=="Goblin", "atk"==1, "blk"==0, "hel"==5, "dmg"==1}, "orc"=={"name"=="Orc", "atk"==2, "blk"==1, "hel"==10, "dmg"==2},]
goblin={"name": "Goblin", "atk": 1, "blk": 0, "hel": 5, "dmg": 1}

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
def playerturn():
    playerturn=input("Your turn! Will you attack/block/escape?")
    if playerturn == "attack":
            if random.randint(1, 3)+(enemies[goblin["blk"]]) <= atk:
                input("You hit the goblin for {} damage!".format(dmg))
                goblin["hel"] -= dmg
                if enemies[goblin["hel"]] <= 0:
                    input("The goblin has been defeated!")
                else:
                    input("The goblin has {} health remaining.".format(enemies[goblin["hel"]]))   
            else:
                input("You missed!")
    elif playerturn == "block":
            blk+=1
            input("You brace for the goblin's attack, increasing your block chance!")
    elif playerturn == "escape":
            if random.randint(1, 3)+(goblin["agi"]) <= agi:
                input("You successfully escaped the goblin!")
                return
            else:
                input("You failed to escape!")

def fight():
    input("Something appears in front of you!")
    enemy=random.choices(enemies, weights=[10,6], k=1)[0]
    input("it's a {}!".format(enemy))
    if enemy == "goblin":
        goblinfight()

#stats (atk=attack success chance, blk=block success chance, agi=escape success chance, hp=health points, dmg=damage)
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