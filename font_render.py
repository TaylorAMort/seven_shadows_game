import pygame
import pygame.freetype
from pygame.rect import Rect

def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    font = pygame.freetype.SysFont("Helvetica", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()