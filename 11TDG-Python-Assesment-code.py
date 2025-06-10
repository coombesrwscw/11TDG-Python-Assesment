#psudocode:
#code:

#Welcome!
print("Welcome to my text adventure game! I made this game for my Python assessment. I hope you enjoy it!")
#scene
print("You find yourself in a dark forest. The trees are tall and the path is narrow. You can hear the sound of leaves rustling in the wind.")
#Investigate? Action? Inventory? Move? or Back?
step1 = input("What would you like to do? (Investigate/Action/Inventory/Back/Move): ").strip().lower()
#   If Investigate: further detail scene/objects
if step1 == "investigate":
    print("Looking around, you notice that one of the trees has a strange marking on it.")
#       Investigate? Action? Inventory? Move? or Back?
    step2 = input("What would you like to do? (Investigate/Action/Inventory/Back/Move): ").strip().lower()
    if step2 == "investigate":
        print("You approach the tree and see that the marking is a symbol of some kind. Touching it, you realize it is strangely warm...")
        print("Before you can investigate further, however, you hear a strange popping sound behind you...")
        print("Whirling around, you see a massive lupine beast before you, having seemingly appeared out of nowhere!")
        qtime1 = input("The beast growls... What would you like to do? (Attack/Dodge/Run): ").strip().lower()
        if qtime1 == "attack":
            print("Full of false pride, you raise a bare fist and swing at the strange creature, but it easily dodges your feeble attempts at rebuff, swiping at you with its claws!")
            print("You take a hit and fall to the ground, defeated.")
            print("As your lifeblood pools on the forest floor, you feel the warmth of the tree's marking fade away...")
            print("YOU DIED.")
        elif qtime1 == "dodge":
            print("In a burst of combative brilliance, you notice the beast tensing, and roll swiftly to the side as the beast lunges at you, narrowly avoiding its deadly claws!")
            print("The beast's claws tear through the space in which you were standing, and get get stuck in the tree behind you!")
            print("You manage to get back on your feet and prepare for another move.")
            print("before you can do anything, you feel a wrenching sense of loss, the warmth of the tree's marking now gone.")
            print("Collapsing to your knees, you notice the gaps between your heartbeats growing longer, and the world around you fading to black.")
            print("YOU DIED.")
        elif qtime1 == "run":
            print("You turn and sprint down the path, leaving the strange beast behind. You think that you have managed to escape, but you know it won't be long before it finds you again.")
            print("As you run further and further, you eventually come to a small village. The villagers take you in and help you recover from your ordeal.")
            print("You realize that you have escaped the beast, but you know that it is still out there, waiting for you to return to the forest.")
            print("With this firm belief, you decide to never return to the forest again, and live out the rest of your days in peace.")
            print("YOU LIVED!")
            

#   If Action: display actions
if step1 == "action":

#   If Inventory: display inventory
if step1 == "inventory":
#       Use Item? Drop Item? or Back?

#   If Move: display directions
if step1 == "move":

#   If Back: exit game
if step1 == "back":