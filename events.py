import pygame
import sys
from UI_focus.buttons import GameState, UIElement, Title
from UI_focus.font_render import create_surface_with_text_fancy, create_surface_with_text
from playervariables.playertypes import Player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from pygame.sprite import RenderUpdates


player_level = 0

def game_loop(screen, buttons, extra_draw_callback=None):
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))

        if extra_draw_callback is not None:
            extra_draw_callback(screen)

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
    
    title = create_surface_with_text_fancy(
        text="Seven Shadows of the Shattered Blade",
        font_size=80,
        text_rgb=(255, 255, 255),
        bg_rgb=(0, 0, 0),
    )

    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))

    buttons = RenderUpdates(start_btn, quit_btn)
    return game_loop(screen, buttons, extra_draw_callback=lambda surface: surface.blit(title, title_rect))

def get_player_name(screen, clock):
   
    title_font  = pygame.font.SysFont("Helvetica", 36, bold=True)
    input_font  = pygame.font.SysFont("Helvetica", 28)
    prompt_font = pygame.font.SysFont("Helvetica", 18)
    name   = ""
    active = True

    BOX_W, BOX_H = 400, 52
    box_rect = pygame.Rect(
        (SCREEN_WIDTH - BOX_W) // 2,
        SCREEN_HEIGHT // 2 - BOX_H // 2,
        BOX_W,
        BOX_H,
    )

    while active:
        dt_ms = clock.tick(60)          

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    if len(name) < 20:
                        name += event.unicode

        screen.fill((0, 0, 0))

        title_surf = title_font.render("Enter Your Name", True, (255, 255, 255))
        screen.blit(title_surf, title_surf.get_rect(centerx=SCREEN_WIDTH // 2, y=180))


        pygame.draw.rect(screen, (100, 100, 100), box_rect, border_radius=8)
        pygame.draw.rect(screen, (200, 200, 200), box_rect, width=2, border_radius=8)

        name_surf = input_font.render(name, True, (255, 255, 255))
        text_x = box_rect.x + 14
        text_y = box_rect.centery - name_surf.get_height() // 2
        screen.blit(name_surf, (text_x, text_y))

        hint_surf = prompt_font.render("Press  Enter  to continue",
                                       True, (255, 255, 255))
        screen.blit(hint_surf, hint_surf.get_rect(centerx=SCREEN_WIDTH // 2,
                                                   y=box_rect.bottom + 18))

        pygame.display.flip()


    return class_selection_screen(screen, name)


def class_selection_screen(screen, name):
    selection = create_surface_with_text(
        text=f"Welcome, {name}. Select your class:",
        font_size=40,
        text_rgb=(255, 255, 255),
        bg_rgb=(0, 0, 0),
    )

    selection_rect = selection.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))

    right_btn = UIElement(
        center_position=(SCREEN_WIDTH // 4 *2, SCREEN_HEIGHT // 2),
        font_size=30,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text=">",
        action=None,
    )
    left_btn = UIElement(
        center_position=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2),
        font_size=30,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="<",
        action=None,
    )

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

def play_level(screen, name):
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
