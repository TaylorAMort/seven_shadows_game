import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.font.init()
    pygame.display.set_caption("Seven Shadows of the Shattered Blade")
    print pygame.font.get_fonts()


if __name__ == "__main__":
    main()
