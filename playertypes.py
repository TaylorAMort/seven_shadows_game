import pygame

class Player:
    def __init__(self, name, health, strength, dexterity, intelligence):
        self.name = name
        self.health = health
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence

class Shadow(Player):
    def __init__(self, name, health, strength, dexterity, intelligence):
        super().__init__(name, health, strength, dexterity, intelligence)
        
class Flame(Player):
    def __init__(self, name, health, strength, dexterity, intelligence):
        super().__init__(name, health, strength, dexterity, intelligence)

class Blood(Player):
    def __init__(self, name, health, strength, dexterity, intelligence):
        super().__init__(name, health, strength, dexterity, intelligence)

class Memory(Player):
    def __init__(self, name, health, strength, dexterity, intelligence):
        super().__init__(name, health, strength, dexterity, intelligence)

class Stone(Player):
    def __init__(self, name, health, strength, dexterity, intelligence):
        super().__init__(name, health, strength, dexterity, intelligence)

class Tide(Player):
    def __init__(self, name, health, strength, dexterity, intelligence):
        super().__init__(name, health, strength, dexterity, intelligence)

class Wind(Player):
    def __init__(self, name, health, strength, dexterity, intelligence):
        super().__init__(name, health, strength, dexterity, intelligence)

