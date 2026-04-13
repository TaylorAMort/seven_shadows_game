import pygame
from UI_focus.buttons import *
from UI_focus.font_render import create_surface_with_text_fancy, create_surface_with_text
from assets import assets
from playervariables.playertypes import *
from constants import *
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
    start_btn = TextButton(
        center_position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50),
        font_size=30,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Start",
        action=GameState.NEWGAME,
    )
    quit_btn = TextButton(
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

def get_player_name(screen, clock, assets):

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

        title_surf = create_surface_with_text(
            text="Enter your name:",
            font_size=36,
            text_rgb=(255, 255, 255),
            bg_rgb=(0, 0, 0),
        )
        screen.blit(title_surf, title_surf.get_rect(centerx=SCREEN_WIDTH // 2, y=180))


        pygame.draw.rect(screen, (100, 100, 100), box_rect, border_radius=8)
        pygame.draw.rect(screen, (200, 200, 200), box_rect, width=2, border_radius=8)

        name_surf = create_surface_with_text(
            text=name,
            font_size=28,
            text_rgb=(255, 255, 255),
            bg_rgb=(0, 0, 0),
        )
        text_x = box_rect.x + 14
        text_y = box_rect.centery - name_surf.get_height() // 2
        screen.blit(name_surf, (text_x, text_y))

        hint_surf = create_surface_with_text(
            text="Press Enter to confirm",
            font_size=18,
            text_rgb=(255, 255, 255),
            bg_rgb=(0, 0, 0),
        )
        screen.blit(hint_surf, hint_surf.get_rect(centerx=SCREEN_WIDTH // 2, y=box_rect.bottom + 18))

        pygame.display.flip()


    return class_selection_screen(screen, name, assets)


def class_selection_screen(screen, name, assets):
    
    
    selection = create_surface_with_text(
        text=f"Welcome, {name}. Select your class:",
        font_size=40,
        text_rgb=(255, 255, 255),
        bg_rgb=(0, 0, 0),
    )

    selection_rect = selection.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
    first_row = selection_rect.bottom + 20
    second_row = first_row + 120
    positions_row_1 = [(SCREEN_WIDTH // 4 * (i + 1), first_row) for i in range(4)]
    positions_row_2 = [(SCREEN_WIDTH // 3 * (i + 1), second_row) for i in range(4)]

    shadow_btn = ImageButton(
        center_position=positions_row_1[0],
        image=assets["SHADOW_IMAGE"],
        font_size=30,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Shadow",
        action=Shadow(name, 100, 10, 10, 10, 10),
    )

    flame_btn = ImageButton(
        center_position=positions_row_1[1],
        image=assets["FLAME_IMAGE"],
        font_size=30,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Flame",
        action=Flame(name, 100, 10, 10, 10, 10),
    )

    blood_btn = ImageButton(
        center_position=positions_row_1[2],
        image=assets["BLOOD_IMAGE"],
        font_size=30,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Blood",
        action=Blood(name, 100, 10, 10, 10, 10),
    )
        

    memory_btn = ImageButton(
        center_position=positions_row_1[3],
        image=assets["MEMORY_IMAGE"],
        font_size=30,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Memory",
        action=Memory(name, 100, 10, 10, 10, 10),
    )

    stone_btn = ImageButton(
        center_position=positions_row_2[0],
        image=assets["STONE_IMAGE"],
        font_size=30,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Stone",
        action=Stone(name, 100, 10, 10, 10, 10),
    )

    tide_btn = ImageButton(
        center_position=positions_row_2[1],
        image=assets["TIDE_IMAGE"],
        font_size=30,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Tide",
        action=Tide(name, 100, 10, 10, 10, 10),
    )

    wind_btn = ImageButton(
        center_position=positions_row_2[2],
        image=assets["WIND_IMAGE"],
        font_size=30,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Wind",
        action=Wind(name, 100, 10, 10, 10, 10),
    )
    buttons = RenderUpdates(shadow_btn, flame_btn, blood_btn, memory_btn, stone_btn, tide_btn, wind_btn)
    player = game_loop(screen, buttons, extra_draw_callback=lambda surface: surface.blit(selection, selection_rect))
    
    return play_level(screen, player)
    

    

def inventory_screen(screen, player):
    for item in player.inventory:
        print(item)
    
    
    return_btn = TextButton(
        center_position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 * 3.5),
        image=None,
        font_size=20,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Return to game",
        action=GameState.PLAYING,
    )

    buttons = RenderUpdates(return_btn)
    return game_loop(screen, buttons)

def play_level(screen, player):
    return_btn = TextButton(
        center_position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 * 3.5),
        font_size=20,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Return to main menu",
        action=GameState.TITLE,
    )

    inventory_btn = TextButton(
        center_position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 * 3),
        font_size=20,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Inventory",
        action=GameState.INVENTORY,
    )

    buttons = RenderUpdates(return_btn, inventory_btn)
    return game_loop(screen, buttons)
