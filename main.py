import pygame
from buttons import GameState, UIElement
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def main():
    pygame.init()
    pygame.display.set_caption("Seven Shadows of the Shattered Blade")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    quit_btn = UIElement(
        center_position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
        font_size=30,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Quit",
        action=GameState.QUIT,
    )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill((0, 0, 0))
        ui_action = quit_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return
        quit_btn.draw(screen)
        pygame.display.flip()
        
    
    


if __name__ == "__main__":
    main()
