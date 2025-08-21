
# lists and functions go here
inventory=[""]
equiplist=[""]
itemlist=["sword, shield, potion, boot"]

# game starts here
input=("Hello, this is a text and probability based fighting game for my python assesment. (press ENTER)")
input=("Light. That is all you see, as your mind slowly surfaces from the depths of REM sleep.")
input=("Sitting up, you see that you are seemingly alone in an empty forest.")
while True:    
    step1=input("would you like to take a look around? (yes/no): ").strip().lower()
    if step1 == "yes":
        startitem=input(random.choices(itemlist, weights=[0.5, 0.3, 0.1, 0.1], k=1))
        input("As you glance around, you notice a {} lying on the ground.".format(startitem))
        step2 = input("Equip? (yes/no): ").strip().lower()
        if step2==input("yes"):
            equiplist.append(startitem)

    elif step1 == "no":
        input("placeholder text")


    else:
        input("Invalid input. Please reinput your choice.")
        continue

