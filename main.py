import pygame
import assets.assets as asset_loader
from events import *
from UI_focus.buttons import GameState
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def main():
    pygame.init()
    pygame.display.set_caption("Seven Shadows of the Shattered Blade")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_state = GameState.TITLE
    clock = pygame.time.Clock()
    player = None
    assets = asset_loader.load_all()
    
    while True:
        clock.tick(60)
        mouse_up = False
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)
        if game_state == GameState.NEWGAME:
            player = get_player_name(screen, clock, assets)
            game_state = GameState.PLAYING
        if game_state == GameState.INVENTORY:
            game_state = inventory_screen(screen, player)
        if game_state == GameState.PLAYING:
            game_state = play_level_1(screen, player)
        if game_state == GameState.LEVEL_2:
            game_state = play_level_2(screen, player)
        if game_state == GameState.QUIT:
            pygame.quit()
            return
        screen.fill((0, 0, 0))
        pygame.display.flip()
        
    
    


if __name__ == "__main__":
    main()
