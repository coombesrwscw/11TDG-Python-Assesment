#loops are there so that the player can go back via the 'continue' after selecting the back option
while True:
    #inputs are used so that the player has to press enter after each line, slowing down the pace and letting them properly read the text
    input("Press ENTER to see the next line of text.")
    input("Welcome to my text adventure game! I made this game for my Python assessment. It's mostly just a demo of the skills I have learnt, but I hope you still enjoy it!")
    while True:
        input("You find yourself in a dark forest. The trees are tall and the path is narrow. You can hear the sound of leaves rustling in the wind.")
        step1 = input("What would you like to do? (Investigate/Inventory/Back/Move): ").strip().lower()
        if step1 == "investigate":
            while True:
                input("Looking around, you notice that one of the trees has a strange marking on it.")
                step2 = input("What would you like to do? (Investigate/Action/Inventory/Back/Move): ").strip().lower()
                if step2 == "investigate":
                    input("You approach the tree and see that the marking is a symbol of some kind. Touching it, you realize it is strangely warm...")
                    input("Before you can investigate further, however, you hear a strange popping sound behind you...")
                    input("Whirling around, you see a massive lupine beast before you, having seemingly appeared out of nowhere!")                
                    while True:
                        qtime1 = input("The beast growls... What would you like to do? (Attack/Dodge/Run): ").strip().lower()
                        if qtime1 == "attack":
                            input("Full of false pride, you raise a bare fist and swing at the strange creature, but it easily dodges your feeble attempts at rebuff, swiping at you with its claws!")
                            input("You take a hit and fall to the ground, defeated.")
                            input("As your lifeblood pools on the forest floor, you feel the warmth of the tree's marking fade away...")
                            input("YOU DIED.") 
                            #exits are used to end the game after a succecsful or failed run
                            exit()
                        elif qtime1 == "dodge":
                            input("In a burst of combative brilliance, you notice the beast tensing, and roll swiftly to the side as the beast lunges at you, narrowly avoiding its deadly claws!")
                            input("The beast's claws tear through the space in which you were standing, and get get stuck in the tree behind you!")
                            input("You manage to get back on your feet and prepare for another move.")
                            input("before you can do anything, you feel a wrenching sense of loss, the warmth of the tree's marking now gone.")
                            input("Collapsing to your knees, you notice the gaps between your heartbeats growing longer, and the world around you fading to black.")
                            input("YOU DIED.")
                            exit()
                        elif qtime1 == "run":
                            input("You turn and sprint down the path, leaving the strange beast behind. You think that you have managed to escape, but you know it won't be long before it finds you again.")
                            input("As you run further and further, you eventually come to a small village. The villagers take you in and help you recover from your ordeal.")
                            input("You realize that you have escaped the beast, but you know that it is still out there, waiting for you to return to the forest.")
                            input("With this firm belief, you decide to never return to the forest again, and live out the rest of your days in peace.")
                            input("YOU LIVED!")
                            exit()
                        else:
                            print("Invalid input. Please reinput your choice.")
                            continue

                #actions and inventory haven't been properly implemented because as I said, this is mostly just an extremly simple demo
                elif step2 == "action":
                    step3 = input("Which action do you want to use? (None/Back)").strip().lower()
                    if step3 == "back":
                        input("Returning to previous choice...")
                        continue        
                    elif step3 == "none":
                        input("You have no actions to take.")
                        continue
                    else:
                        print("Invalid input. Returning to previous choice...")
                        continue

                elif step2 == "inventory":
                    input("you take a look in your pockets")
                    input("Your inventory is empty. You have nothing to use.")
                    step3 = input("Would you like to use an item? (Yes/Back): ").strip().lower()
                    if step3 == "yes":
                        input("You have no items to use.")
                        input("Returning to previous choice...")
                        continue
                    elif step3 == "back":
                        input("Exiting iventory...")
                        continue
                elif step2 == "back":
                    input("Returning...")
                    continue
                elif step2 == "move":
                    step3 = input("Which direction do you want to move? (North/South/East/West/Back): ").strip().lower()
                    if step3 == "back":
                        input("Returning")
                        continue
                    elif step3 in ["north", "south", "east", "west"]:
                        input("You move {} down the path, leaving the strange tree behind. You feel a sense of unease as you leave the marking behind, but you know that you must keep moving.") .format(step3)
                        input("As you walk down the path, you feel a strange crawling sensation on the back of your neck, as if something is watching you. You quicken your pace, hoping to leave the forest behind.")
                        input("out of the corner of your vision, your eyes are drawn to a tree with a strange marking on it, similar to the one you saw before.")
                        input("You feel a strange compulsion to touch it, but you resist the urge and keep moving.")
                        input("Now running, you occasionally glance at a tree, and every time you do, you see the strange marking on it, identical to the one you saw before.")
                        input("Occasionally hearing growls and howls from behind you continue to run, never seeming to escape the presumably immense forest.")
                        input("Sometimes, you start feeling too tired to run anymore, but then you see the marking on the tree, and you receive a strange burst of energy, allowing you to continue running.")
                        input("For eternity, you run. You can no longer think of anything but running, and the mark.")
                        input("YOU ARE LOST.")
                        exit()
                        #I was tempted to make different endings for each direction, but I decided against it, as it would have been too much work for such a simple game
                    else:
                        print("Invalid input. Please reinput your choice.")
                        continue
                else:
                    print("Invalid input. Please reinput your choice.")
                    continue

        if step1 == "inventory":
            input("You check your pockets, but there is nothing in your inventory.")
            input("Returning to previous choice...")
            continue

        if step1 == "move":  
            step2 = input("Please choose a direction to move (North/South/East/West/Back): ").strip().lower()
            input("You move {} down the path, leaving the dark forest behind. You feel a sense of unease as you leave the forest, but you know that you must keep moving.".format(step2))
            input("As you continue to walk down the unchanging path, you finally come to a spot that is slightly different from what you have seen on the path previously.")
            if step2 == "North":
                input("the path seems to just... END.")
                input("it's not like you would expect from a dirt path of this type, where the path would slowly fade away into a game trail, and then into the forest, but rather, it just stops.")
                input("You would liken it to a flat line where the path stops existing, with a completely normal -if rough, path on one side, and some of the densest forest you have ever seen on the other side.")
                input("Actually, now that you look a bit closer, the trees on all sides seem to be impossibly dense, such that in some places, their trunks have fused together, and what few gaps there are, are too small for you to fit through.")
                step3=input("DO YOU TURN AROUND? (Yes/No): ").strip().lower()
                if step3 == "yes":
                    input("You feel only pain.")
                    input("Before you can react, before you can even think, you feel a sharp pain in your stomach, and then nothing.")
                    input("YOU DIED.")
                    exit()
            elif step3 == "no":
                input("Nothing happens. You just stand there, staring at the path's end...")
                input("...")
                input("...")
                input("...")
                input("...")
                input("...")
                input("...")
                input("...")
                input("...")
                input("...")
                input("...")
                input("...")
                input("...")
                input("...")
                input("...")
                input("...")
                input("...")
                input("...")
                input("...")
                input("...")
                input("...")
                input("...")
                input("...WHY ARE YOU STILL HERE?")
                input("WHY HAVE YOU NOT CLOSED THE GAME?")
                input("WILL YOU LEAVE?")

        if step1 == "back":
            input("Restarting game...")
            continue
        else:
            print("Invaid input. Please reinput your choice.")
            continue
