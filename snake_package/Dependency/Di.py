import pygame, random, numpy
from enum import Enum
from collections import namedtuple
import constants as constants
import Utils.ManualSnakeGame as ManualSnakeGame

class Di(object):
    # packages
    pygame, namedtuple, random, numpy, enum = None, None, None, None, None
    # utils
    constants, manual_snake_game = None, None
    
    def __init__(self) -> None:
        # packages
        Di.pygame = pygame
        Di.namedtuple = namedtuple
        Di.random = random
        Di.enum = Enum
        Di.numpy = numpy
        # utils
        Di.constants = constants
    
    def _init_manual_snake_game(self):
        Di.manual_snake_game = ManualSnakeGame()