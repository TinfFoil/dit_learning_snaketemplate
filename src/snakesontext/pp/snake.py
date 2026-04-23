
import os
import random
import time

# Game dimensions
width = 10 #20
height = 10 # 20
# snake_block = 1
snake_speed = 0.05  # Adjust this for speed


arrows =  "  w  \n"
arrows += "a s d\n"

# Definition of the "board" border
border = "#"
top_frame_border = border * width * 2 + border

# Directions
directions = {
    'UP':    (0, -1),
    'DOWN':  (0,  1),
    'LEFT':  (-1, 0),
    'RIGHT': (1,  0)
}

# Initial position and direction
snake = [(width//2, height//2)]
direction = 'RIGHT'

# Food
food = (random.randint(0, width - 1), random.randint(0, height - 1))
score = 0

# Game over flag
game_over = False

def clear_screen():
    """Clears the contents from the screen to refresh the board
    after every interaction
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board():
    """
    Updates  the screen after each interaction with the user. 
    It...

    - Sets up an empty board
    - Adds the snake to the board
    - Adds the food to the board
    - Resets the screen and displays the board
    """

    board = [[' ' for _ in range(width)] for _ in range(height)]

    # Draw snake
    for x, y in snake:
        board[y][x] = 'S'

    # Draw food
    board[food[1]][food[0]] = 'F' # '⏺'

    # Print the board
    clear_screen()
    print(top_frame_border)
    for row in board:
        print(border + ' '.join(row) + border)
    print(top_frame_border)

    print(f"{arrows} Score: {score}")

def move():
    """
    Determines the new position of the snake and alters
    it depending on the situation (i.e. moving and growing)
    """
    global snake, food, score, game_over

    # TODO this function has a bug: when the direction is
    # and the key are incompatible, it "bumps"

    # Move snake
    x, y = snake[0]
    dx, dy = directions[direction]
    new_x, new_y = x + dx, y + dy

    # Check boundaries
    if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
        game_over = True
        return

    # Check self-collision
    if (new_x, new_y) in snake:
        game_over = True
        return

    # Add new head
    snake.insert(0, (new_x, new_y))

    # Check food collision
    if (new_x, new_y) == food:
        score += 1
        food = (random.randint(0, width - 1), random.randint(0, height - 1))
    else:
        # Remove tail
        snake.pop()

def game_over_message():
    """Displays the game over message,
    including the final score
    """
    clear_screen()
    print("*" * 18)
    print("*   Game Over!   *")
    print(f"* Final Score: {score} *")
    print("*" * 18)
    
def run_game():

    # TODO Every time this is launched, the
    # snake should be initialized
    global direction, game_over

    game_over = False


    print("Welcome to Snake in Text Mode!")
    print("Use 'w', 'a', 's', 'd' to control the snake")
    print("Press 'q' to quit")

    print("\nLoading...")

    time.sleep(5)

    # while True:
    while game_over == False:
        print_board()

        # Get user input
        cmd = input().strip().lower()

        if cmd == 'q':
            game_over = True # not really necessary, given the break
            break

        # Change directionw
        if cmd == 'w' and direction != 'DOWN':
            direction = 'UP'
        elif cmd == 's' and direction != 'UP':
            direction = 'DOWN'
        elif cmd == 'a' and direction != 'RIGHT':
            direction = 'LEFT'
        elif cmd == 'd' and direction != 'LEFT':
            direction = 'RIGHT'

        move()
        time.sleep(snake_speed)

    game_over_message()