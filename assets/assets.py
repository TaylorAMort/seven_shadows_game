import pygame
ICON_SIZE = (80, 80)
def load_all():
    def load(path):
        return pygame.transform.smoothscale(
            pygame.image.load(path).convert_alpha(), ICON_SIZE
        )
    return {
        "SHADOW_IMAGE": load("assets/cowled.png").convert_alpha(),
        "BLOOD_IMAGE": load("assets/bleeding-wound.png").convert_alpha(),
        "FLAME_IMAGE": load("assets/fire.png").convert_alpha(),
        "MEMORY_IMAGE": load("assets/gift-of-knowledge.png").convert_alpha(),
        "STONE_IMAGE": load("assets/stone-block.png").convert_alpha(),
        "TIDE_IMAGE": load("assets/wave-crest.png").convert_alpha(),
        "WIND_IMAGE": load("assets/wind-slap.png").convert_alpha(),
        }