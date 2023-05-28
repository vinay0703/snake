import Dependency.Di as Di
"""This class refers to the agent."""
class Agent:
    def __init__(self):
        self.point = Di.namedtuple('Point', 'x, y')
        self.auto_snake_game = Di.AutoSnakeGame.AutoSnakeGame
        # agent variables
        self.number_of_games = 0
        # Tradeoff between exploitation and exploration
        self.epsilon = 0
        # Discount factor 
        self.gamma = Di.constants.DISCOUNT_FACTOR
        # NN model
        self.model = None
        self.trainer = None

    def get_state(self, game):
        head = game.snake[0]
        # 4 corner points of snake head
        point_l = self.point(head.x - Di.constants.BLOCK_SIZE, head.y)
        point_r = self.point(head.x + Di.constants.BLOCK_SIZE + 20, head.y)
        point_u = self.point(head.x, head.y - Di.constants.BLOCK_SIZE)
        point_d = self.point(head.x, head.y + Di.constants.BLOCK_SIZE)

        dir_l = game.direction == Di.Direction.direction.LEFT
        dir_r = game.direction == Di.Direction.direction.RIGHT
        dir_u = game.direction == Di.Direction.direction.UP
        dir_d = game.direction == Di.Direction.direction.DOWN

        # State consists of 11 elements
        state = [
            # 1. Danger Straight
            (dir_r and game.if_collision(point_r)) or 
            (dir_l and game.if_collision(point_l)) or 
            (dir_u and game.if_collision(point_u)) or 
            (dir_d and game.if_collision(point_d)),
            # 2. Danger right
            (dir_u and game.if_collision(point_r)) or 
            (dir_d and game.if_collision(point_l)) or 
            (dir_l and game.if_collision(point_u)) or 
            (dir_r and game.if_collision(point_d)),
            # 3. Danger left
            (dir_d and game.if_collision(point_r)) or 
            (dir_u and game.if_collision(point_l)) or 
            (dir_r and game.if_collision(point_u)) or 
            (dir_l and game.if_collision(point_d)),
            # 4, 5, 6, 7 Move directions
            dir_l,
            dir_r,
            dir_u,
            dir_d,
            # 8, 9, 10, 11 Food locations
            game.food.x < game.head.x,  # food left
            game.food.x > game.head.x,  # food right
            game.food.y < game.head.y,  # food up
            game.food.y > game.head.y  # food down
        ]
        return Di.numpy.array(state, dtype=int)

    def get_action(self, state):
        # Randomness - exploitation or exploration
        self.epsilon = Di.constants.EPSILON - self.number_of_games
        final_move = [0, 0, 0]
        # Exploration
        if Di.random.randint(0, Di.constants.EXPLORATION_THRESHOLD) < self.epsilon:
            move = Di.random.randint(0, 2)
        # Exploitation
        else:
            move = None # TODO
        final_move[move] = 1
        return final_move