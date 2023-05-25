from enum import Enum
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

class HumanSnakeGame:
    def __init__(self, Di, w=640, h=480):
        # Dependency
        self.di = Di

        # required packages
        self.pygame, self.random, self.namedtuple = Di.pygame, Di.random, Di.namedtuple

        # required utils
        self.constants = Di.constants

        # # Initialize Pygame window
        # self._init_pygame_window()

        # Set inital score to 0
        self.score = 0

        # Initial Food
        self.food = None
        self._place_food()

    def _init_pygame_window(self):
        self.pygame.init()
        # Setting up font parameters
        # font = self.pygame.font.Font('arial.ttf', 25)
        print(self.constants.FONT_STYLE)
        self.font = self.pygame.font.SysFont(self.constants.FONT_STYLE, self.constants.FONT_SIZE)
        # Pygame window dimensions
        self.w, self.h = self.constants.WIDTH, self.constants.HEIGHT
        self.Point = self.namedtuple('Point', 'x, y')
        # Snake paramters
        self.block_size = self.constants.BLOCK_SIZE
        self.speed = self.constants.SPEED
        # init display
        self.display = self.pygame.display.set_mode((self.w, self.h))
        self.pygame.display.set_caption('Snake')
        self.clock = self.pygame.time.Clock()
        # init game state
        self.direction = Direction.RIGHT
        self.head = self.Point(self.w/2, self.h/2)
        self.snake = [self.head, 
                      self.Point(self.head.x-self.block_size, self.head.y),
                      self.Point(self.head.x-(2*self.block_size), self.head.y)]
        

    def _place_food(self):
        x = self.random.randint(0, (self.w-self.block_size )//self.block_size )*self.block_size 
        y = self.random.randint(0, (self.h-self.block_size )//self.block_size )*self.block_size
        self.food = self.Point(x, y)
        if self.food in self.snake:
            self._place_food()
        
    def play_step(self):
        # 1. collect user input
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.pygame.quit()
                quit()
            if event.type == self.pygame.KEYDOWN:
                if event.key == self.pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == self.pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == self.pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == self.pygame.K_DOWN:
                    self.direction = Direction.DOWN
        
        # 2. move
        self._move(self.direction) # update the head
        self.snake.insert(0, self.head)
        
        # 3. check if game over
        game_over = False
        if self._is_collision():
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
        self.clock.tick(self.speed)
        # 6. return game over and score
        return game_over, self.score
    
    def _is_collision(self):
        # hits boundary
        if self.head.x > self.w - self.block_size or self.head.x < 0 or self.head.y > self.h - self.block_size or self.head.y < 0:
            return True
        # hits itself
        if self.head in self.snake[1:]:
            return True
        
        return False
        
    def _update_ui(self):
        self.display.fill(self.constants.BLACK)
        
        for pt in self.snake:
            self.pygame.draw.rect(self.display, self.constants.BLUE1, self.pygame.Rect(pt.x, pt.y, self.block_size, self.block_size))
            self.pygame.draw.rect(self.display, self.constants.BLUE2, self.pygame.Rect(pt.x+4, pt.y+4, 12, 12))
            
        self.pygame.draw.rect(self.display, self.constants.RED, self.pygame.Rect(self.food.x, self.food.y, self.block_size, self.block_size))
        
        text = self.font.render("Score: " + str(self.score), True, self.constants.WHITE)
        self.display.blit(text, [0, 0])
        self.pygame.display.flip()
        
    def _move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += self.block_size
        elif direction == Direction.LEFT:
            x -= self.block_size
        elif direction == Direction.DOWN:
            y += self.block_size
        elif direction == Direction.UP:
            y -= self.block_size
            
        self.head = self.Point(x, y)
            
