from robot import Robot
from weapon import Weapon


class Fleet:
    def __init__(self):
        self.fleet = [Robot("wall-e", 15, 100, Weapon("Baseball Bat", 30)),
                      Robot("C3PO", 25, 100, Weapon("Flame Thrower", 45)),
                      Robot("Terminator", 50, 100, Weapon("AR-18", 60))]

