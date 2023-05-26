import Dependency.Di as Di
from Utils.SnakeGame import SnakeGame
"""This class inherits from SnakeGame and it is manual control of snake game."""
class ManualSnakeGame(SnakeGame):
    def __init__(self):
        super().__init__()
    
    def play_step(self):
        # 1. Collect user input from keyboard
        for event in Di.pygame.event.get():
            if event.type == Di.pygame.QUIT:
                Di.pygame.quit()
                quit()
            if event.type == Di.pygame.KEYDOWN:
                if event.key == Di.pygame.K_LEFT:
                    self.direction = self.direction_enum.LEFT
                elif event.key == Di.pygame.K_RIGHT:
                    self.direction = self.direction_enum.RIGHT
                elif event.key == Di.pygame.K_UP:
                    self.direction = self.direction_enum.UP
                elif event.key == Di.pygame.K_DOWN:
                    self.direction = self.direction_enum.DOWN
        # 2. move
        self._move(self.direction) # update the head
        self.snake.insert(0, self.head)
        
        # 3. check if game over
        game_over = False
        if self._if_collision():
            game_over = True
            return game_over, self.score
            
        # 4. place new food or just move
        if self.head == self.food:
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()
        
        # 5. update ui and clock
        self._update_ui()
        self.clock.tick(Di.constants.SNAKE_SPEED)

        # 6. return game over and score
        return game_over, self.score
            
    def play_manual_snake_game(self):
        # Initializing pygame display
        self._init_display()
        # Initalizing game state
        self._init_game_state()
        # Starting game through infintite loop
        while True:
            game_over, score = self.play_step()
            if game_over == True:
                break
        print(Di.constants.FINAL_GAME_SCORE + str(score))
        Di.pygame.quit()
