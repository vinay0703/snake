import pygame, random
from enum import Enum
from collections import namedtuple
import constants as constants
import Utils.ManualSnakeGame as ManualSnakeGame

class Di:
    # packages
    pygame, namedtuple, random, enum = None, None, None, None

    # utils
    constants, manual_snake_game = None, None

    def __init__(self) -> None:
        # packages
        Di.pygame = pygame
        Di.namedtuple = namedtuple
        Di.random = random
        Di.enum = Enum

        # utils
        Di.constants = constants
    
    def _init_manual_snake_game(self):
        Di.manual_snake_game = ManualSnakeGame()