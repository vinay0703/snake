import pygame, random
from enum import Enum
from collections import namedtuple
import snake.constants as constants

class Di(object):
    # packages
    pygame, enum, namedtuple, random = None, None, None, None

    # utils
    human_snake_game, constants = None, None

    def __init__(self) -> None:
        # packages
        Di.pygame = pygame
        Di.enum = Enum
        Di.namedtuple = namedtuple
        Di.random = random

        # utils
        Di.constants = constants
    