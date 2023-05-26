import Dependency.Di as Di
from Utils.SnakeGame import SnakeGame

"""This class inherits from SnakeGame and it is auto play mode of snake game."""
class AutoSnakeGame(SnakeGame):
    def __init__(self):
        super().__init__()
        self.frame_iteration = 0
    
    def play_step(self, action):
        self.frame_iteration += 1
        # 1. collect input
        for event in Di.pygame.event.get():
            if event.type == Di.pygame.QUIT:
                Di.pygame.quit()
                quit()
        # 2. move
        self._move(action) # update the head
        self.snake.insert(0, self.head)
        # 3. check if game over
        reward = 0
        game_over = False
        # If there is collision or snake is at same length after certain iterations
        # i.e; doesn't eat food just roam it is a bad action.
        if self.is_collision() or self.frame_iteration > Di.constants.ITER_THRESHOLD * len(self.snake):
            game_over = True
            reward = -10 # reward for a collision
            return reward, game_over, self.score
        # 4. place new food or just move
        if self.head == self.food:
            self.score += 1
            reward = 10 # reward for eating food
            self._place_food()
        else:
            self.snake.pop()
        # 5. update ui and clock
        self._update_ui()
        self.clock.tick(Di.constants.SNAKE_SPEED)
        # 6. return game over and score
        return reward, game_over, self.score

    def _move(self, action):
        # [straight, right, left] wrt snake head
        # straight -> [1, 0, 0]
        # right -> [0, 1, 0]
        # left -> [0, 0, 1]
        if Di.numpy.array_equal(action, [1, 0, 0]):
            self.direction = self.direction_enum.RIGHT
        elif Di.numpy.array_equal(action, [0, 1, 0]):
            self.direction = self.direction_enum.DOWN
        else:
            self.direction = self.direction_enum.UP
        
        x, y = self.head.x, self.head.y
        if self.direction == self.direction_enum.RIGHT:
            x += self.block_size
        elif self.direction == self.direction_enum.LEFT:
            x -= self.block_size
        elif self.direction == self.direction_enum.UP:
            y -= self.block_size # Pygame window y-axis starts from top
        else:
            y += self.block_size
        self.head = self.point(x, y)