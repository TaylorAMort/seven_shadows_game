import pygame

def load_all():
    return {
        "SHADOW_IMAGE": pygame.image.load("assets/cowled.png").convert_alpha(),
        "BLOOD_IMAGE": pygame.image.load("assets/bleeding-wound.png").convert_alpha(),
        "FLAME_IMAGE": pygame.image.load("assets/fire.png").convert_alpha(),
        "MEMORY_IMAGE": pygame.image.load("assets/gift-of-knowledge.png").convert_alpha(),
        "STONE_IMAGE": pygame.image.load("assets/stone-block.png").convert_alpha(),
        "TIDE_IMAGE": pygame.image.load("assets/wave-crest.png").convert_alpha(),
        "WIND_IMAGE": pygame.image.load("assets/wind-slap.png").convert_alpha(),
        }