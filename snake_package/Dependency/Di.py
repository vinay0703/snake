import pygame, random
from enum import Enum
from collections import namedtuple
import constants as constants
import Utils.SnakeGame as SnakeGame

class Di(object):
    # packages
    pygame, enum, namedtuple, random = None, None, None, None

    # utils
    snake_game, constants = None, None

    def __init__(self) -> None:
        # packages
        Di.pygame = pygame
        Di.enum = Enum
        Di.namedtuple = namedtuple
        Di.random = random

        # utils
        Di.constants = constants
        Di.snake_game = SnakeGame()