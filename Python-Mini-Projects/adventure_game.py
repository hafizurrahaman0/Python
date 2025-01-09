def level(level):
    print('\n')
    print('=' * 20)
    print(level.center(20, '='))
    print('=' * 20)

def start_game():
    level(" Level 1 ")
    print("Welcome to the Adventure Game!")
    print("You find yourself standing at the entrance of a dark forest. Do you want to enter?")
    choice = input("Type 'yes' to enter or 'no' to stay: ").lower()
    
    if choice == "yes":
        enter_forest()
    elif choice == "no":
        print("You decide to stay where you are. The adventure ends here.")
    else:
        print("Invalid choice, please try again.")
        start_game()

def enter_forest():
    level(" Level 2 ")
    print("You walk into the forest and soon come across a fork in the path.")
    print("Do you go left towards the sound of water or right towards the light in the trees?")
    choice = input("Type 'left' to go towards the water or 'right' to go towards the light: ").lower()
    
    if choice == "left":
        river_path()
    elif choice == "right":
        light_path()
    else:
        print("Invalid choice, please try again.")
        enter_forest()

def river_path():
    level(" Level 3 ")
    print("You follow the sound of water and find a beautiful river.")
    print("There is a boat tied to a tree. Do you take the boat or follow the river on foot?")
    choice = input("Type 'boat' to take the boat or 'foot' to follow on foot: ").lower()
    
    if choice == "boat":
        boat_ride()
    elif choice == "foot":
        foot_path()
    else:
        print("Invalid choice, please try again.")
        river_path()

def boat_ride():
    level(" Level 4")
    print("You untie the boat and start rowing down the river.")
    print("Suddenly, you see a waterfall ahead! Do you jump out or stay in the boat?")
    choice = input("Type 'jump' to jump out or 'stay' to stay in the boat: ").lower()
    
    if choice == "jump":
        print("You jump out just in time and swim to the shore. You find a treasure chest! You win!")
    elif choice == "stay":
        print("You go over the waterfall and crash. The adventure ends here.")
    else:
        print("Invalid choice, please try again.")
        boat_ride()

def foot_path():
    level(" Level 5 ")
    print("You decide to follow the river on foot.")
    print("After a while, you encounter a bear! Do you run or try to climb a tree?")
    choice = input("Type 'run' to run away or 'climb' to climb a tree: ").lower()
    
    if choice == "run":
        print("You try to run, but the bear is faster. The adventure ends here.")
    elif choice == "climb":
        print("You climb a tree and wait until the bear leaves. You find a safe path home. You win!")
    else:
        print("Invalid choice, please try again.")
        foot_path()

def light_path():
    level(" Level 6 ")
    print("You follow the light and find a small village.")
    print("Do you enter the village or explore the surrounding forest?")
    choice = input("Type 'enter' to enter the village or 'explore' to explore the forest: ").lower()
    
    if choice == "enter":
        village()
    elif choice == "explore":
        forest_explore()
    else:
        print("Invalid choice, please try again.")
        light_path()

def village():
    level(" Level 7 ")
    print("You enter the village and meet friendly villagers who invite you to a feast.")
    print("Do you accept the invitation or politely decline and continue your adventure?")
    choice = input("Type 'accept' to join the feast or 'decline' to continue: ").lower()
    
    if choice == "accept":
        print("You enjoy a wonderful feast and make new friends. You win!")
    elif choice == "decline":
        print("You continue your adventure and find an ancient artifact. You win!")
    else:
        print("Invalid choice, please try again.")
        village()

def forest_explore():
    level(" Level 8 ")
    print("You decide to explore the forest and find a hidden cave.")
    print("Do you enter the cave or go back to the village?")
    choice = input("Type 'enter' to enter the cave or 'back' to go back: ").lower()
    
    if choice == "enter":
        cave()
    elif choice == "back":
        village()
    else:
        print("Invalid choice, please try again.")
        forest_explore()

def cave():
    level(" Level 9 ")
    print("You enter the cave and find it filled with glittering crystals.")
    print("Do you take some crystals or leave them and explore further?")
    choice = input("Type 'take' to take crystals or 'explore' to explore further: ").lower()
    
    if choice == "take":
        print("You take some crystals and find your way out of the forest. You win!")
    elif choice == "explore":
        print("You explore further and discover a hidden underground city. You win!")
    else:
        print("Invalid choice, please try again.")
        cave()

start_game()
