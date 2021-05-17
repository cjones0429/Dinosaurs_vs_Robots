from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.fleet = Fleet
        self.herd = Herd

    def run_game(self):
        self.display_welcome()
        self.user_side = self.pick_robo_or_dino
        self.battle()

    def display_welcome(self):
        print("Welcome to Dinosaurs vs Robots!")

    def pick_robo_or_dino(self):
        user_pick_side = int(input('Choose your side using the number keys 1 or 2: (1) Dinosaurs or (2) Robots'))
        if user_pick_side == 1:
            print("You chose the Dinosaurs!")
            return user_pick_side
        elif user_pick_side == 2:
            print("You chose Robots!")
            return user_pick_side
        else:
            print("Invalid input. Please try again. Hint...remember to only use keys 1 or 2")
            self.pick_robo_or_dino()


    def battle(self):
        pass

    def dino_turn(self):
        pass



