import curses
import time
import random

def main(stdscr):
    # Set up the game window
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Non-blocking input
    sh, sw = stdscr.getmaxyx()
    w = stdscr.subwin(sh, sw, 0, 0)

    # Initialize the paddle and ball positions
    paddle_x = sw // 2
    ball_x = random.randint(1, sw - 1)
    ball_y = 1
    ball_direction_x = random.choice([-1, 1])
    ball_direction_y = 1

    # Game variables
    score = 0
    game_over = False

    # Main game loop
    while not game_over:
        # Clear the screen
        w.clear()

        # Get user input
        key = w.getch()
        if key == ord('q'):
            break

        # Move the paddle
        if key == curses.KEY_RIGHT and paddle_x < sw - 3:
            paddle_x += 1
        elif key == curses.KEY_LEFT and paddle_x > 0:
            paddle_x -= 1

        # Move the ball
        ball_x += ball_direction_x
        ball_y += ball_direction_y

        # Check for collision with walls
        if ball_x >= sw - 1 or ball_x <= 0:
            ball_direction_x *= -1

        # Check for collision with paddle
        if ball_y == sh - 2 and paddle_x - 2 <= ball_x <= paddle_x + 2:
            ball_direction_y *= -1
            score += 1

        # Check for game over
        if ball_y >= sh - 1:
            game_over = True

        # Display the paddle, ball, and score
        w.addch(sh - 1, paddle_x - 2, '|')
        w.addch(sh - 1, paddle_x - 1, '|')
        w.addch(sh - 1, paddle_x, '|')
        w.addch(sh - 1, paddle_x + 1, '|')
        w.addch(sh - 1, paddle_x + 2, '|')

        w.addch(ball_y, ball_x, 'o')

        w.addstr(0, 0, f'Score: {score}')
        w.refresh()
        time.sleep(0.1)

    # Game over message
    w.clear()
    game_over_message = "Game Over! Your Score: {}".format(score)
    w.addstr(sh // 2, sw // 2 - len(game_over_message) // 2, game_over_message)
    w.refresh()
    stdscr.getch()

# Run the game
curses.wrapper(main)
