from herd import Herd

class Dinosaur:
    def __init__(self, type, energy, attack_power, health):
        self.type = type
        self.energy = energy
        self.attack_power = attack_power
        self.health = 100

    def dinosaur_attack_robot(self, robot):
        print("Dinosaur attacked Robot!!")
        self.herd.attack_power -= robot.health
