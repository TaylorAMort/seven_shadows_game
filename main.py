import pygame
from sprite import UIElement
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def main():
    pygame.init()
    pygame.display.set_caption("Seven Shadows of the Shattered Blade")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    uielement = UIElement(
        center_position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Seven Shadows of the Shattered Blade",
    )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        uielement.update(pygame.mouse.get_pos())
        uielement.draw(screen)
        pygame.display.flip()
        
    
    


if __name__ == "__main__":
    main()
