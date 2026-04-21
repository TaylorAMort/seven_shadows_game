from pathlib import Path
import pygame
import pygame.freetype


FANCY_FONT = Path(__file__).resolve().parent.parent / "fonts" / "elvencommonspeak-2.ttf"

def create_surface_with_text_fancy(text, font_size, text_rgb, bg_rgb):
    font = pygame.freetype.Font(FANCY_FONT, font_size)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()

def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    font = pygame.freetype.SysFont("Helvetica", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()