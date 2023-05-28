import pygame, random, numpy
from enum import Enum
from collections import namedtuple
import constants as constants
import Utils.Direction as Direction
import Utils.SnakeGame as SnakeGame
import Utils.ManualSnakeGame as ManualSnakeGame
import Utils.AutoSnakeGame as AutoSnakeGame

class Di(object):
    # packages
    pygame, namedtuple, random, numpy, enum = None, None, None, None, None
    # utils
    constants, direction, snake_game, manual_snake_game, auto_snake_game = None, None, None, None, None
    
    def __init__(self) -> None:
        # packages
        Di.pygame = pygame
        Di.namedtuple = namedtuple
        Di.random = random
        Di.enum = Enum
        Di.numpy = numpy
        # utils
        Di.constants = constants
        Di.direction = Direction
        Di.snake_game = SnakeGame()
    
    def _init_manual_snake_game(self):
        Di.manual_snake_game = ManualSnakeGame()
    
    def _init_auto_snake_game(self):
        Di.auto_snake_game = AutoSnakeGame()