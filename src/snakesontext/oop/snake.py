import os
import random
import time

# Allows for capturing key strokes
from readchar import readkey, key

class SnakeOnText():

    ARROWS =  "  w  \n"
    ARROWS += "a s d\n"

    # Directions
    DIRECTIONS = {
        'UP':    (0, -1),
        'DOWN':  (0,  1),
        'LEFT':  (-1, 0),
        'RIGHT': (1,  0)
    }

    def __init__(self, board_width=10, board_height=10, snake_speed=0.01, initial_direction="RIGHT", border="#"):
        # Board size
        self.board_width = board_width
        self.board_height = board_height

        self.snake_speed = snake_speed
    
        # Board border
        self.border = border
        self.top_frame_border = border * self.board_width * 2 + border

        # Starting position and direction
        self.snake = [(self.board_width//2, self.board_height//2)]
        self.direction = initial_direction

        # Food
        self.food = self._get_food_coordinates()
        self.score = 0
        
        # Game over flag
        self.game_over = False

    def _get_food_coordinates(self):
        tmp = (random.randint(0, self.board_width - 1), random.randint(0, self.board_height - 1))
        if tmp in self.snake:
            print("RECURSIVITY")
            time.sleep(0.3)
            tmp = self._get_food_coordinates()

        return tmp
    
    # def set_snake_speed(self, speed):
    #     self.snake_speed = speed

    @staticmethod
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

        board = [[' ' for _ in range(self.board_width)] for _ in range(self.board_height)]

        # Draw snake
        for x, y in self.snake:
            board[y][x] = 'S'

        # Draw food
        board[self.food[1]][self.food[0]] = 'F' # '⏺'

        # Print the board
        self.clear_screen()
        print(self.top_frame_border)
        for row in board:
            print(self.border + ' '.join(row) + self.border)
        print(self.top_frame_border)

        print(f"{self.ARROWS} Score: {self.score}")

    def move(self):
        """
        Determines the new position of the snake and alters
        it depending on the situation (i.e. moving and growing)
        """

        # TODO this function has a bug: when the direction 
        # and the key are incompatible, it "bumps"

        # Move snake
        x, y = self.snake[0]
        dx, dy = self.DIRECTIONS[self.direction]
        new_x, new_y = x + dx, y + dy

        # Check boundaries
        if new_x < 0 or new_x >= self.board_width or new_y < 0 or new_y >= self.board_height:
            self.game_over = True
            return

        # Check self-collision
        if (new_x, new_y) in self.snake:
            self.game_over = True
            return

        # Add new head
        self.snake.insert(0, (new_x, new_y))

        # TODO perhaps shift before collisions. Otherwise, the head might crash against 
        # a leaving tail       
        # Check food collision
        if (new_x, new_y) == self.food:
            self.score += 1
            self.food = self._get_food_coordinates()
            # (random.randint(0, self.board_width - 1), random.randint(0, self.board_height - 1))
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
                self.direction = 'UP'
            elif cmd == 's' and self.direction != 'UP':
                self.direction = 'DOWN'
            elif cmd == 'a' and self.direction != 'RIGHT':
                self.direction = 'LEFT'
            elif cmd == 'd' and self.direction != 'LEFT':
                self.direction = 'RIGHT'

            self.move()
            time.sleep(self.snake_speed)
            if len(self.snake) == self.board_width * self.board_height - 1:
                return True

        self.game_over_message()
        return False