"""Snake game class which is common to both human control and computer control."""
import Dependency.Di as Di

class SnakeGame:
    def __init__(self):
        self.direction_enum = Di.Enum('Direction', ['RIGHT', 'LEFT', 'UP', 'DOWN'])
        self.point = Di.namedtuple('Point', 'x, y')
        # Initializing pygame
        Di.pygame.init()
        # Initializing pygame font
        self.font = Di.pygame.font.Font(Di.constants.FONT_STYLE, Di.constants.FONT_SIZE)
        self.clock = Di.pygame.time.Clock()

    def _init_display(self):
        self.w = Di.constants.WIDTH
        self.h = Di.constants.HEIGHT
        self.display = Di.pygame.display.set_mode((self.w, self.h))
        Di.pygame.display.set_caption(Di.constants.DISPLAY_CAPTION)
    
    def _init_game_state(self):
        self.block_size = Di.constants.BLOCK_SIZE
        self.game_speed = Di.constants.SNAKE_SPEED
        # Initial snake direction is right
        self.direction = self.direction_enum.RIGHT
        # Initial snake head position is at centre of pygame display
        self.head = self.point(self.w/2, self.h/2)
        # Inital snake body contains of 3 blocks # TODO
  ################################################################################
        self.snake = [self.head, self.point(self.head.x - self.block_size, self.head.y), self.point(self.head.x - 2 * self.block_size, self.head.y)]
        # Initally score is 0 and no food
        self.score, self.food = 0, None
        # Placing food
        self._place_food()

    def _place_food(self):
        x = Di.random.randint(0, (self.w - self.block_size)//self.block_size) * self.block_size
        y = Di.random.randint(0, (self.h - self.block_size)//self.block_size) * self.block_size
        self.food = self.point(x, y)
        # If snake eats food then place another food, i.e; when snake body contains the food point
        if self.food in self.snake:
            self._place_food()

    def _if_collision(self):
        # If the snake its the boundary of pygame display, then it is considered as collision.
        # RIGHT boundary or LEFT boundary or UP boundary or DOWN boundary
        if (self.head.x > self.w - self.block_size) or (self.head.x < 0) or (self.head.y > self.h - self.block_size) or (self.head.y < 0):
            return True
        # If the snake hits itself, then also it is considered as collision.
        elif self.head in self.snake[1:]:
            return True
        # else not a collision
        else:
            return False

    def _update_ui(self):
        # Background in black color
        self.display.fill(Di.constants.BLACK)
        # Displaying snake head and body in blue color variation
        for pt in self.snake:
            Di.pygame.draw.rect(self.display, Di.constants.BLUE1, Di.pygame.Rect(pt.x, pt.y, self.block_size, self.block_size))
            Di.pygame.draw.rect(self.display, Di.constants.BLUE2, Di.pygame.Rect(pt.x+4, pt.y+4, 12, 12))
            
        # Displaying food in red color
        Di.pygame.draw.rect(self.display, Di.constants.RED, Di.pygame.Rect(self.food.x, self.food.y, self.block_size, self.block_size))
        
        # Displaying updated score
        text = self.font.render("Score: " + str(self.score), True, Di.constants.WHITE)
        self.display.blit(text, [0, 0])
        Di.pygame.display.flip()
    
    def _move(self, direction):
        x, y = self.head.x, self.head.y
        if direction == self.direction_enum.RIGHT:
            x += self.block_size
        elif direction == self.direction_enum.LEFT:
            x -= self.block_size
        elif direction == self.direction_enum.UP:
            y -= self.block_size # Pygame window y-axis starts from top
        else:
            y += self.block_size
        self.head = self.point(x, y)