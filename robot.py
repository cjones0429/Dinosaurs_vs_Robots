class Robot:
    def __init__(self, name, power_level, health, weapon):
        self.name = name
        self.power_level = power_level
        self.health = 100
        self.weapon = weapon

    def robot_attack_dinosaur(self, dinosaur):
        print("Robot attacked Dinosaur!!")
        self.weapon.attack_power -= dinosaur.health
