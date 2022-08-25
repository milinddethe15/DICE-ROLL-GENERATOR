import random 
#asking user to input number of dice to roll
while True:
    times = (input("How many dice you want to roll? "))
    try:
        times = int(times)
        break
    #if user entered a string 
    except ValueError:
        print("PLease enter a number") 
results = [] #list to save outcomes     
for _ in range(times):
    roll = random.randint(1,6) #random outcomes from randint between 1-6
    results.append(roll)
#Die art to display the result
DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
#dimensions of a die 
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])

dice_faces = []  #list to assign dice faces to results 
for result in results:
    dice_faces.append(DICE_ART[result])
#to print the dice faces 
#we will print faces row wise 
dice_faces_rows=[] 
for num_row in range(DIE_HEIGHT):
    row_components=[] 
    for die in dice_faces:
        row_components.append(die[num_row]) #row wise components from each required dice faces 
    row_string = " ".join(row_components) #converting string using space" " as separator
    dice_faces_rows.append(row_string) 

dice_faces_diagram = "\n".join(dice_faces_rows) #creating string of all row components with "\n" as separator

print(dice_faces_diagram) #displaying result
