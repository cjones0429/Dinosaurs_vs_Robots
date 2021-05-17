from weapon import Weapon
#import random


class Robot:
    def __init__(self, name):
        self.name = name
        self.power_level = 200
        self.health = 100
        self.weapon = [Weapon("AR-18", 60),
                       Weapon("Flame Thrower", 45),
                       Weapon("Baseball Bat", 30)]

    def robot_attack_dinosaur(self, dinosaur_being_attacked):
        #attack = random.choice(weapon)
        if self.power_level > 10:
            selected_weapon: int(input(f"Choose your weapon using the number keys 1, 2, or 3: (1) {self.weapon[0]}, (2) {self.weapon[1]}, or (3) {self.weapon[2]}."))
        if selected_weapon == 1:
            print(f'Beep Boop! {self.name} attacked {dinosaur_being_attacked} by {self.weapon[0]}')
        elif selected_weapon == 2:
            print(f'Beep Boop! {self.name} attacked {dinosaur_being_attacked} by {self.weapon[1]}')
        elif selected_weapon == 3:
            print(f'Beep Boop! {self.name} attacked {dinosaur_being_attacked} by {self.weapon[2]}')

        self.power_level -= 10
        dinosaur_being_attacked.health -= self.weapon











