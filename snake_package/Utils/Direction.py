import Dependency.Di as Di
"""This class is about snake direction."""
class Direction(object):
    direction = Di.Enum(Di.constants.DIRECTION_ENUM_NAME, Di.constants.DIRECTION_ENUM_VALUE)