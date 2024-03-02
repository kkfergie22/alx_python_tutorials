# ---------- WARRIORS BATTLE ----------
# We will create a game with this sample output
"""
Sam attacks Paul and deals 9 damage
Paul is down to 10 health
Paul attacks Sam and deals 7 damage
Sam is down to 7 health
Sam attacks Paul and deals 19 damage
Paul is down to -9 health
Paul has Died and Sam is Victorious
Game Over
"""

import random
import math


class Warrior:
    def __init__(self, name="Warrior", health="100", attackMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attack_max = attackMax
        self.block_max = blockMax

    def attack(self):
        attack_amount = self.attack_max * (random.random() + 0.5)
        return attack_amount

    def block(self):
        block_amount = self.block_max * (random.random() + 0.5)
        return block_amount


class Battle:
    def start_fight(self, warrior1, warrior2):
        while True:
            if self.attack_result(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
            if self.attack_result(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def attack_result(warriorA, warriorB):
        warriorAAttkAmt = warriorA.attack()

        warriorBBlockAmt = warriorB.block()

        damage2WarriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)

        warriorB.health = warriorB.health - damage2WarriorB

        print(
            "{} attacks {} and deals {} damage".format(
                warriorA.name, warriorB.name, damage2WarriorB
            )
        )

        print("{} is down to {} health".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print(
                "{} has Died and {} is Victorious".format(warriorB.name, warriorA.name)
            )

            return "Game Over"
        else:
            return "Fight Again"
