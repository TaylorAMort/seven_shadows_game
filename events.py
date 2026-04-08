import pygame
from UI_focus.buttons import GameState, UIElement, Title
from playervariables.playertypes import Player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from pygame.sprite import RenderUpdates


player_level = 0

def game_loop(screen, buttons):
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)
        pygame.display.flip()

def title_screen(screen):
    start_btn = UIElement(
        center_position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50),
        font_size=30,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Start",
        action=GameState.NEWGAME,
    )
    quit_btn = UIElement(
        center_position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 * 2.5),
        font_size=30,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Quit",
        action=GameState.QUIT,
    )
    title = Title(
        center_position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3),
        font_size=80,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Seven Shadows of the Shattered Blade",
    )

    buttons = RenderUpdates(start_btn, quit_btn, title)
    return game_loop(screen, buttons)

def inventory_screen(screen, player):
    for item in player.inventory:
        print(item)
    
    
    return_btn = UIElement(
        center_position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 * 3.5),
        font_size=20,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Return to game",
        action=GameState.PLAYING,
    )

    buttons = RenderUpdates(return_btn)
    return game_loop(screen, buttons)

def play_level(screen):
    return_btn = UIElement(
        center_position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 * 3.5),
        font_size=20,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Return to main menu",
        action=GameState.TITLE,
    )

    inventory_btn = UIElement(
        center_position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 * 3),
        font_size=20,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Inventory",
        action=GameState.INVENTORY,
    )

    buttons = RenderUpdates(return_btn, inventory_btn)
    return game_loop(screen, buttons)
