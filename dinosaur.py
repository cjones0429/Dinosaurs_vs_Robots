from attack_type import Attack_type


class Dinosaur:
    def __init__(self, type):
        self.type = type
        self.energy = 200
        self.health = 100
        self.attack_type = [Attack_type("Claw Slash", 65),
                            Attack_type("Tail Whip", 30),
                            Attack_type("Dagger", 55)]

    def dinosaur_attack_robot(self, robot_being_attacked):
        if self.energy > 10:
            selected_attack_type: int(input(f"Choose your attack type using the number keys 1, 2, or 3: (1) {self.attack_type[0]}, (2) {self.attack_type[1]}, or (3) {self.attack_type[2]}."))
        if selected_attack_type == 1:
            print(f'Rawr! {self.type} attacked {robot_being_attacked} by {self.attack_type[0]}')
        elif selected_attack_type == 2:
            print(f'Rawr! {self.type} attacked {robot_being_attacked} by {self.attack_type[1]}')
        elif selected_attack_type == 3:
            print(f'Rawr! {self.type} attacked {robot_being_attacked} by {self.attack_type[2]}')

        self.energy -= 10
        robot_being_attacked -= self.attack_type


