from pygame.sprite import Sprite
from UI_focus.font_render import create_surface_with_text, create_surface_with_text_fancy
from enum import Enum

class TextButton(Sprite):
    def __init__(self, center_position, text, font_size, text_rgb, bg_rgb, action=None):
        self.mouse_over = False
        self.action = action
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
    
    def update(self, mouse_pos, mouse_up):
        if self.rect().collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False
    
    def draw(self, surface):
        surface.blit(self.image(), self.rect())

class ImageButton(Sprite):
    def __init__(self, center_position, text, image, font_size, text_rgb, bg_rgb, action=None):
        self.mouse_over = False
        self.action = action
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
        symbol_rect = self.symbol.get_rect(centerx=self.rect().centerx, bottom=self.rect().top)
        surface.blit(self.symbol, symbol_rect)
        surface.blit(self.image(), self.rect())

class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAME = 1
    INVENTORY = 2
    PLAYING = 3
