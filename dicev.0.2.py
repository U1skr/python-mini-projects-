import random
def roll_dice():

    dice_drawing = {
        0: (),
        1: (
            "____",
            "|  o   |",
            "`````",
            
        ),
        2: (
             "____",
            "|   o   |",
            "|   o   |",
            "`````",
        ),
        3: (
             "____",
            "|   o   |",
            "| o  o |",
            "``````",
        ),
        4: (
            "_____",
            "|o     o|",
            "|o     o|",
            "`````````",
        ),
        5: (
             "_____",
            "|o      o|",
            "|    o    | ",
            "|o      o|",
            "```````",
        ),
        6: (
            "_____",
            "|o     o|",
            "|o     o|",
            "|o     o|",
            "``````",
        ),

    }
    a=input("Press X to roll the dice ")
    if (a.lower()=='x'):
        d1=random.randint(1,6)
        print("\n".join(dice_drawing[d1]))
        return d1
    else:
        print("You've entered the wrong ,kindly restart the game" )
        return 0

print("roll the dice ")
value=[]
total=[]
players=[]
no=int(input("Enter the no.of players : "))
x=no+1
for j in range(1,x):
    players.append(j)
    print("\n\tPlayer ",j)
    for k in range(1,3):
        print("Turn",k,":")
        z=roll_dice()
        value.append(z)
    s=sum(value)
    total.append(s)
    value.clear()
    print("\t\tYour Turns are Over ,well played ")
print(players)
print(total)     
print(" \t\tthe winner is ",players[total.index(max(total))])


    
        
        
       
