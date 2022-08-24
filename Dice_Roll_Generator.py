import random

while True:
    times = (input("How many dices you want to roll? "))
    try:
        times = int(times)
        break
    except ValueError:
        print("Enter a number")
results = []     
for _ in range(times):
    roll = random.randint(1,6)
    results.append(roll)

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
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

dice_faces = []
for result in results:
    dice_faces.append(DICE_ART[result])

dice_faces_rows=[]
for num_row in range(DIE_HEIGHT):
    row_components=[]
    for die in dice_faces:
        row_components.append(die[num_row])
    row_string = " ".join(row_components)
    dice_faces_rows.append(row_string)

dice_faces_diagram = "\n".join(dice_faces_rows)

print(dice_faces_diagram)