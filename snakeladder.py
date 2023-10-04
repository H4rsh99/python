import random

# Initialize player positions
player1_position = 0
player2_position = 0

# Define the snake and ladder board as a dictionary
snake_ladder_board = {
    2: 38, 7: 14, 8: 31, 16: 6, 15: 26,
    28: 84, 21: 42, 36: 44, 47: 26, 49: 11,
    51: 67, 62: 19, 64: 60, 71: 91, 74: 53,
    89: 68, 92: 88, 95: 75, 99: 80
}

# Function to roll a die
def roll_die():
    return random.randint(1, 6)

# Function to play a turn
def play_turn(player_name, player_position):
    input(f"{player_name}, press Enter to roll the dieceee...")
    die_value = roll_die()
    print(f"{player_name} rolled a {die_value}")
    player_position += die_value

    if player_position in snake_ladder_board:
        new_position = snake_ladder_board[player_position]
        if new_position > player_position:
            print(f"{player_name} found a ladder! Climbing to {new_position}")
        else:
            print(f"{player_name} encountered a snake! Going down to {new_position}")
        player_position = new_position

    return player_position

# Main game loop
while player1_position < 100 and player2_position < 100:
    print("\nPlayer 1's Turn:")
    player1_position = play_turn("Player 1", player1_position)
    if player1_position >= 100:
        print("Player 1 wins!")
        break

    print("\nPlayer 2's Turn:")
    player2_position = play_turn("Player 2", player2_position)
    if player2_position >= 100:
        print("Player 2 wins!")

print("\nGame Over!")
