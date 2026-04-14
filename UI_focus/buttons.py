import pygame
from pygame.sprite import Sprite
from UI_focus.font_render import create_surface_with_text
from enum import Enum

class Button(Sprite):
    def __init__(self, center_position, text, font_size, text_rgb, bg_rgb,
                 action=None, image=None, subtitle=None, subsubtitle=None, border_rgb=None):
        self.mouse_over = False
        self.action = action
        self.border_rgb = border_rgb
        self.symbol = image
        default_image = create_surface_with_text(text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb)
        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )
        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]
        self.subtitle_surf = (
            create_surface_with_text(text=subtitle, font_size=font_size * 0.6, text_rgb=text_rgb, bg_rgb=bg_rgb)
            if subtitle else None
        )
        self.subsubtitle_surf = (
            create_surface_with_text(text=subsubtitle, font_size=font_size * 0.6, text_rgb=text_rgb, bg_rgb=bg_rgb)
            if subsubtitle else None
        )

        super().__init__()

    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        if self.rect().collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        if self.symbol:
            symbol_rect = self.symbol.get_rect(centerx=self.rect().centerx, bottom=self.rect().top)
            surface.blit(self.symbol, symbol_rect)
        surface.blit(self.image(), self.rect())
        if self.border_rgb:
            pygame.draw.rect(surface, self.border_rgb, self.rect().inflate(20,20), width=2, border_radius=8)
        if self.subtitle_surf:
            subtitle_rect = self.subtitle_surf.get_rect(centerx=self.rect().centerx, top=self.rect().bottom + 4)
            surface.blit(self.subtitle_surf, subtitle_rect)
        if self.subsubtitle_surf:
            subsubtitle_rect = self.subsubtitle_surf.get_rect(centerx=self.rect().centerx, top=self.rect().bottom + 4 + self.subtitle_surf.get_height() + 2)
            surface.blit(self.subsubtitle_surf, subsubtitle_rect)

# Keep old names as aliases for backwards compatibility
TextButton = Button
ImageButton = Button

class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAME = 1
    INVENTORY = 2
    PLAYING = 3
    LEVEL_2 = 4
