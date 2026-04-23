import os
import random
import time

from readchar import readkey, key

class SnakeOnText():
    # Game dimensions
    # BOARD_WIDTH = 10 #20
    # BOARD_HEIGHT = 10 # 20
    # snake_block = 1
    # SNAKE_SPEED = 0.05  # Adjust this for speed

    ARROWS =  "  w  \n"
    ARROWS += "a s d\n"

    # Definition of the "board" border
    # BORDER = "#"

        # Directions
    DIRECTIONS = {
        'UP':    (0, -1),
        'DOWN':  (0,  1),
        'LEFT':  (-1, 0),
        'RIGHT': (1,  0)
    }


    def __init__(self, board_widht=10, board_height = 10, snake_speed=0.05, initial_direction="RIGHT", border="#"):
        # Game dimensions
        self.board_width = board_widht
        self.board_height = board_height
        self.snake_speed = snake_speed
    
        # Definition of the "board" border
        self.border = border
        self.top_frame_border = border * self.board_width * 2 + border

        # Initial position and direction
        self.snake = [(self.board_width//2, self.board_height//2)]
        self.direction = initial_direction

        # Food
        self.food = (random.randint(0, self.board_width - 1), random.randint(0, self.board_height - 1))
        self.score = 0
        
        # Game over flag
        game_over = False

    # def set_board_width(self, width):
    #      self.board_width = width

    # def set_board_height(self, height):
    #     self.board_height = height
    
    # def set_snake_speed(self, speed):
    #     self.snake_speed = speed

    # def set_border_character(self, character):
    #     if len(character) == 1:
    #         self.border_character = character
    #         # TODO this should be triggered when the board weight is changed too
    #         self.top_frame_border = border * BOARD_WIDTH * 2 + border

    #     else:
    #         exit(-1)

    def clear_screen():
        """Clears the contents from the screen to refresh the board
        after every interaction
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_board(self):
        """
        Updates  the screen after each interaction with the user. 
        It...

        - Sets up an empty board
        - Adds the snake to the board
        - Adds the food to the board
        - Resets the screen and displays the board
        """

        board = [[' ' for _ in range(self.board_widht)] for _ in range(self.board_height)]

        # Draw snake
        for x, y in self.snake:
            board[y][x] = 'S'

        # Draw food
        board[food[1]][food[0]] = 'F' # '⏺'

        # Print the board
        self.clear_screen()
        print(self.top_frame_border)
        for row in board:
            print(border + ' '.join(row) + border)
        print(self.top_frame_border)

        print(f"{self.ARROWS} Score: {self.score}")

    def move(self):
        """
        Determines the new position of the snake and alters
        it depending on the situation (i.e. moving and growing)
        """
        # global snake, food, score, game_over

        # TODO this function has a bug: when the direction is
        # and the key are incompatible, it "bumps"

        # Move snake
        x, y = self.snake[0]
        dx, dy = self.DIRECTIONS[self.direction]
        new_x, new_y = x + dx, y + dy

        # Check boundaries
        if new_x < 0 or new_x >= self.board_widht or new_y < 0 or new_y >= self.board_height:
            self.game_over = True
            return

        # Check self-collision
        if (new_x, new_y) in self.snake:
            self.game_over = True
            return

        # Add new head
        self.snake.insert(0, (new_x, new_y))

        # Check food collision
        if (new_x, new_y) == self.food:
            self.score += 1
            self.food = (random.randint(0, self.board_widht - 1), random.randint(0, self.board_height - 1))
        else:
            # Remove tail
            self.snake.pop()

    def game_over_message(self):
        """Displays the game over message,
        including the final score
        """
        self.clear_screen()
        print("*" * 18)
        print("*   Game Over!   *")
        print(f"* Final Score: {self.score} *")
        print("*" * 18)
        
    def run_game(self):

        # TODO Every time this is launched, the
        # snake should be initialized
        # global direction, game_over

        # game_over = False


        print("Welcome to Snake in Text Mode!")
        print("Use 'w', 'a', 's', 'd' to control the snake")
        print("Press 'q' to quit")

        print("\nLoading...")

        time.sleep(5)

        # while True:
        while self.game_over == False:
            self.print_board()

            # Get user input
            cmd = readkey()
            
            if cmd == 'q':
                self.game_over = True # not really necessary, given the break
                break

            # Change directionw
            if cmd == 'w' and self.direction != 'DOWN':
                direction = 'UP'
            elif cmd == 's' and self.direction != 'UP':
                direction = 'DOWN'
            elif cmd == 'a' and self.direction != 'RIGHT':
                direction = 'LEFT'
            elif cmd == 'd' and self.direction != 'LEFT':
                direction = 'RIGHT'

            self.move()
            time.sleep(SNAKE_SPEED)

        self.game_over_message()