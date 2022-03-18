class Pokemon:
    count = 0

    def info(self, id,  name, type, species):
        self.id = id
        self.name = name
        self.type = type
        self.species = species
        Pokemon.count += 1

    def stats(self, id, health, attack, speed):
        self.id = id
        self.health = health
        self.attack = attack
        self.speed = speed


class Ability:
    
    def info(self, id, abilities, type):
        self.id = id
        self.abilities = abilities
        self.type = type

    def stats(self, id, spell_time, mana_cost):
        self.id = id
        self.spell_time = spell_time
        self.mana_cost = mana_cost



