import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def opening_screen():
    font = pygame.font.Font("fonts/elvencommonspeak-2.ttf", 120)
    text_surface = font.render("Seven Shadows of the Shattered Blade", True, (255, 255, 255))
    return screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, SCREEN_HEIGHT // 2 - text_surface.get_height() // 2))