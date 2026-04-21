import random
from playervariables.objects import Weapon, HealthPotion
from UI_focus.font_render import create_surface_with_text_fancy, create_surface_with_text

class Player:
    def __init__(self, name, health, str, dex, int, wis):
        self.name = name
        self.health = health
        self.strength = str
        self.dexterity = dex
        self.intelligence = int
        self.wisdom = wis
        self.karma = 0
        self.inventory = [Weapon("Rusty Dagger", 5, "A dull and worn dagger. Better than nothing, but not by much."),
                          HealthPotion("Minor Healing Potion", 20, "A small vial filled with a red liquid. Restores a small amount of health when consumed.")]
    
    def attack(self, other, weapon):
        alive = True
        damage = self.strength + weapon.damage
        other.health -= damage
        if other.health < 0: 
            alive = False
        return damage, alive
    
    def defend(self, damage):
        return create_surface_with_text(
            text=f"You defend against the attack and take {damage // 2} damage!",
            font_size=10,
            text_rgb=(255, 255, 255),
            bg_rgb=(0, 0, 0)
        )

    def sneak(self, other):
        passed = False
        if self.dexterity + random.randint(1, 20) > other.wisdom + random.randint(1, 20):
            passed = True
        return passed

        

class Shadow(Player):
    def __init__(self, name, health, str, dex, int, wis):
        super().__init__(name, health, str, dex, int, wis)
        self.dexterity = dex + 10
        self.intelligence = int + 5

class Flame(Player):
    def __init__(self, name, health, str, dex, int, wis):
        super().__init__(name, health, str, dex, int, wis)
        self.strength = str + 10
        self.dexterity = dex + 5

class Blood(Player):
    def __init__(self, name, health, str, dex, int, wis):
        super().__init__(name, health, str, dex, int, wis)
        self.intelligence = int + 10
        self.dexterity = dex + 5

class Memory(Player):
    def __init__(self, name, health, str, dex, int, wis):
        super().__init__(name, health, str, dex, int, wis)
        self.wisdom = wis + 10
        self.intelligence = int + 5

class Stone(Player):
    def __init__(self, name, health, str, dex, int, wis):
        super().__init__(name, health, str, dex, int, wis)
        self.strength = str + 10
        self.wisdom = wis + 5

class Tide(Player):
    def __init__(self, name, health, str, dex, int, wis):
        super().__init__(name, health, str, dex, int, wis)
        self.intelligence = int + 10
        self.dexterity = str + 5

class Wind(Player):
    def __init__(self, name, health, str, dex, int, wis):
        super().__init__(name, health, str, dex, int, wis)
        self.dexterity = dex + 10
        self.wisdom = wis + 5

