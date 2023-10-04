import random

# Define the maze as a list of lists
maze = [
    ["S", " ", " ", " ", " ", " ", " ", " ", " ", "E"],
    ["#", "#", "#", "#", " ", "#", "#", "#", " ", "#"],
    [" ", " ", " ", " ", " ", " ", "#", " ", " ", " "],
    [" ", "#", "#", "#", "#", " ", "#", " ", "#", " "],
    [" ", "#", " ", " ", "#", " ", "#", " ", "#", " "],
    [" ", "#", "#", " ", "#", " ", "#", " ", "#", " "],
    [" ", "#", " ", " ", " ", " ", " ", " ", "#", " "],
    [" ", "#", "#", "#", "#", "#", "#", "#", "#", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", "#", "#", "#", "#", "#", "#", "#", "#", " "],
]

# Define the player's starting position
player_x, player_y = 0, 0

# Define the exit position
exit_x, exit_y = 9, 0

# Define player movement functions
def move_left():
    global player_x
    player_x -= 1

def move_right():
    global player_x
    player_x += 1

def move_up():
    global player_y
    player_y -= 1

def move_down():
    global player_y
    player_y += 1

# Main game loop
while True:
    # Clear the screen
    print("\033c", end="")

    # Print the maze
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if x == player_x and y == player_y:
                print("P", end=" ")
            else:
                print(cell, end=" ")
        print()

    # Check if the player has reached the exit
    if player_x == exit_x and player_y == exit_y:
        print("Congratulations! You've reached the exit.")
        break

    # Get the player's move
    move = input("Enter your move (W/A/S/D): ").upper()

    # Perform the move
    if move == "W":
        if player_y > 0 and maze[player_y - 1][player_x] != "#":
            move_up()
    elif move == "A":
        if player_x > 0 and maze[player_y][player_x - 1] != "#":
            move_left()
    elif move == "S":
        if player_y < 9 and maze[player_y + 1][player_x] != "#":
            move_down()
    elif move == "D":
        if player_x < 9 and maze[player_y][player_x + 1] != "#":
            move_right()

# End of the game
