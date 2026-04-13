import pygame
import random

class Player:
    def __init__(self, name, health, str, dex, int, wis):
        self.name = name
        self.health = health
        self.strength = str
        self.dexterity = dex
        self.intelligence = int
        self.wisdom = wis
        self.inventory = []
    
    def attack(self, other, weapon):
        damage = self.strength + weapon.damage
        other.health -= damage
        return print(f"You attack {other.name} with {weapon.name} for {damage} damage! {other.name} has {other.health} health remaining.")
    
    def defend(self, damage):
        return damage // 2

    def sneak(self, other):
        if self.dexterity + random.randint(1, 20) > other.wisdom + random.randint(1, 20):
            return print(f"You successfully sneak past {other.name}!")
        return print(f"You fail to sneak past {other.name} and alert them to your presence!")
        

class Shadow(Player):
    def __init__(self, name, health, str, dex, int, wis):
        super().__init__(name, health, str, wis)
        self.dexterity = dex + 10
        self.intelligence = int + 5

class Flame(Player):
    def __init__(self, name, health, str, dex, int, wis):
        super().__init__(name, health, int, wis)
        self.strength = str + 10
        self.dexterity = dex + 5

class Blood(Player):
    def __init__(self, name, health, str, dex, int, wis):
        super().__init__(name, health, str, wis)
        self.intelligence = int + 10
        self.dexterity = dex + 5

class Memory(Player):
    def __init__(self, name, health, str, dex, int, wis):
        super().__init__(name, health, str, dex)
        self.wisdom = wis + 10
        self.intelligence = int + 5

class Stone(Player):
    def __init__(self, name, health, str, dex, int, wis):
        super().__init__(name, health, str, dex, int, wis)
        self.strength = str + 10
        self.wisdom = wis + 5

class Tide(Player):
    def __init__(self, name, health, str, dex, int, wis):
        super().__init__(name, health, str, wis)
        self.intelligence = int + 10
        self.dexterity = dex + 5

class Wind(Player):
    def __init__(self, name, health, str, dex, int, wis):
        super().__init__(name, health, str, int, wis)
        self.dexterity = dex + 10
        self.wisdom = wis + 5

