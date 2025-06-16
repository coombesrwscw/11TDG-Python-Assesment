#psudocode:
#code:
while True:
#Welcome!
    input("Welcome to my text adventure game! I made this game for my Python assessment. I hope you enjoy it!")
#scene
    input("You find yourself in a dark forest. The trees are tall and the path is narrow. You can hear the sound of leaves rustling in the wind.")
#Investigate? Action? Inventory? Move? or Back?
    step1 = input("What would you like to do? (Investigate/Action/Inventory/Back/Move): ").strip().lower()
#   If Investigate: further detail scene/objects
    if step1 == "investigate":
        while True:
            input("Looking around, you notice that one of the trees has a strange marking on it.")
#       Investigate? Action? Inventory? Move? or Back?
    
            step2 = input("What would you like to do? (Investigate/Action/Inventory/Back/Move): ").strip().lower()
            if step2 == "investigate":
                input("You approach the tree and see that the marking is a symbol of some kind. Touching it, you realize it is strangely warm...")
                input("Before you can investigate further, however, you hear a strange popping sound behind you...")
                input("Whirling around, you see a massive lupine beast before you, having seemingly appeared out of nowhere!")                
                qtime1 = input("The beast growls... What would you like to do? (Attack/Dodge/Run): ").strip().lower()
                if qtime1 == "attack":
                    input("Full of false pride, you raise a bare fist and swing at the strange creature, but it easily dodges your feeble attempts at rebuff, swiping at you with its claws!")
                    input("You take a hit and fall to the ground, defeated.")
                    input("As your lifeblood pools on the forest floor, you feel the warmth of the tree's marking fade away...")
                    input("YOU DIED.")
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
            elif step2 == "action":
                step3 = input("Which action do you want to use? (None/Back)").strip().lower()
                if step3 == "back":
                    input("Returning to previous choice...")
                    continue        
                elif step3 == "none":
                    input("You have no actions to take.")
                    continue
            elif step2 == "inventory":
                input("you take a look in your pockets")
                input("Your inventory is empty. You have nothing to use.")
                step3 = input("Would you like to use an item? (Yes/Back): ").strip().lower()
                if step3 == "yes":
                    input("You have no items to use.")
                elif step3 == "back":
                    input("Exiting iventory...")
                    continue
            elif step2 == "back":
                input("Restarting game...")
                continue
            elif step2 == "move":
                step3 = input("Which direction do you want to move? (North/South/East/West/Back): ").strip().lower()
                if step3 == "back":
                    input("Restarting game...")
                    continue
                elif step3 in ["north", "south", "east", "west"]:
                    input("You move {} down the path, leaving the strange tree behind. You feel a sense of unease as you leave the marking behind, but you know that you must keep moving.") .format(step3)
                    input("As you walk down the path, you feel a strange crawling sensation on the back of your neck, as if something is watching you. You quicken your pace, hoping to leave the forest behind.")
                    input("out of the corner of your vision, your eyes are drawn to a tree with a strange marking on it, similar to the one you saw before.")
                    input("You feel a strange compulsion to touch it, but you resist the urge and keep moving.")
                    input("Now running, you ocasionally glance at a tree, and every time you do, you see the strange marking on it, identical to the one you saw before.")
                    input("Occasionally hearing growls and howls from behind you continue to run, never seeming to ecsape the presumably immense forest.")
                    input("Sometimes, you star feeling too tired to run anymore, but then you see the marking on the tree, and you recieve a strange burst of energy, allowing you to contiue running.")
                    input("For eternity, you run. You can no longer think of anything but running, and the mark.")
                    input("YOU ARE LOST.")

#   If Action: display actions
    if step1 == "action":
        step2 = input("Which action do you want to use? (Item/Back): ").strip().lower()
        if step2 == "item":
            input("You have no items to use.")
        elif step2 == "back":
            input("Returning to previous choice...")
            continue

#   If Inventory: display inventory
    if step1 == "inventory":
        input("You check your pockets, but there is nothing in your inventory.")
        continue
#       Use Item? Drop Item? or Back?

#   If Move: display directions
    if step1 == "move":   
#       North? South? East? West? or Back?
        step2 = input("Please choose a direction to move (North/South/East/West/Back): ").strip().lower()
        
#   If Back: exit game
    if step1 == "back":
        input("Restarting game...")
        continue