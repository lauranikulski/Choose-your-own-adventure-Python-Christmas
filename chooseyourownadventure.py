def start_adventure(): # functions - covered by William in lecture # 4#-
    print("Welcome to A Very Python Christmas ")
    print("The snow falls softly outside, blanketing the town of Hollybrooke in a thick layer of white.  You're curled up by the fire, sipping hot cocoa, when suddenly, there's a rustling at the door. You open it to find a small, green Python named Pythius shivering in the cold.")
    print("'Hello,' he whispers, his voice barely audible over the wind. 'My name is Pythius, and I need your help! Santa's sleigh has been stolen!'")
    print("(A) Help Pythius find Santa's sleigh without delay?")
    print("(B) Offer Pythius some hot cocoa and have him sit down first?")
    print("Press A or B to continue")

    choice = input("Enter A or B: ") # user input - was covered in the first lecture! 

    if choice == "A":
        find_sleigh()
    elif choice == "B":
        hot_cocoa()
    else:
        print("Invalid choice. Try again!")
        start_adventure()

def find_sleigh(): 
    print("You decide to help Pythius. 'Don't worry,' you say,'We'll find Santa's sleigh!'")
    print("'Thank you! I know it was the Grinch,' he says with a shudder. 'He hates Christmas and always tries to ruin it.")
    print("'Well, we can't let that happen,' you say resolutely.") 
    print("Pythius tells you that Santa usually stores his sleigh in a hidden cave on Mount Evergreen.") 
    print("Do you:")
    print("(A) Take Pythius directly to Mount Evergreen? You know the way.")
    print("(B) Ask Pythius if he knows any other clues about where the Grinch might have taken the sleigh?")
    print("Press A or B to continue")
    
    choice = input("Enter A or B: ") # user input - was covered in the first lecture! 
    
    if choice == "A":
        go_to_mountain()
    elif choice == "B":
        hot_cocoa()
    else:
        print("Invalid choice. Try again!")
        find_sleigh()
    
def hot_cocoa():
    print("You decide to gather more information before heading straight to Mount Evergreen. 'Pythius,' you ask, 'do you know anything else about where the Grinch might have taken Santa's sleigh?'")
    print("Pythius sips his cocoa thoughtfully. 'Hmm,' he says, stroking his chin. 'The Grinch loves shiny things, and he's always complaining about how boring Hollybrooke is. Maybe he took the sleigh to a place with lots of sparkle and excitement!'")
    print("He pauses for a moment, then adds, 'Oh! And I heard him muttering something about a stage where everything shines bright. Could it be...the Ice Palace?'")
    print("The Ice Palace is a famous winter festival in Hollybrooke, known for its dazzling ice sculptures and glittering decorations.")
    print("Do you:")
    print("(A) Head straight to the Ice Palace? It sounds like the Grinch's style.")
    print("(B) Ask Pythius if he knows anything else about the Grinch's plans or possible hiding places? You don't want to jump to conclusions.")
    
    choice = input("Enter A or B: ") # user input - was covered in the first lecture! 
    
    if choice == "A":
        go_to_ice_palace()
    elif choice == "B":
        more_info()
    else:
        print("Invalid choice. Try again!")
        find_sleigh()
    
    
def go_to_mountain():
    pass

def go_to_ice_palace():
    pass

def more_info():
    pass