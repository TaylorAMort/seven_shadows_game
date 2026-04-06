import pygame
from pygame.sprite import Sprite
from font_render import create_surface_with_text

class UIElement(Sprite):
    def __init__(self, center_position, text, font_size, text_rgb, bg_rgb):
        self.mouse_over = False
        default_image = create_surface_with_text(text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb)
        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )
        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        super().__init__()

    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]
    
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]
    
    def update(self, mouse_pos):
        if self.rect().collidepoint(mouse_pos):
            self.mouse_over = True
        else:
            self.mouse_over = False
    
    def draw(self, surface):
        surface.blit(self.image(), self.rect())
