import pygame
import json
from events import *
from UI_focus.buttons import GameState, UIElement
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def main():
    pygame.init()
    pygame.display.set_caption("Seven Shadows of the Shattered Blade")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_state = GameState.TITLE

    while True:
        mouse_up = False
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)
        if game_state == GameState.NEWGAME:
            game_state = play_level(screen)
        if game_state == GameState.QUIT:
            pygame.quit()
            return
        screen.fill((0, 0, 0))
        pygame.display.flip()
        
    
    


if __name__ == "__main__":
    main()
