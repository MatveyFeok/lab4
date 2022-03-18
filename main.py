class Pokemon:
    id = 0
    name = ''
    health = 0
    attack = 0
    type = ''
    height = 0
    weight = 0
    def __init__(self, health, attack):
        return health * attack
    def pulse_check(self):
        if health > 0:
            print("pokemon is alive!")
        else:
            print("pokemon died!")

class Ability:
    abilities = ''
    type = ''
    spell_time = 0
    mana_cost = 0
    def __init__(self, type):
        if type == "Poison":
            return print("be careful! Pokemon is poisonous!")
    def speed(self):
        if spell_time > 10:
            return print("your pokemon is so slow!")


