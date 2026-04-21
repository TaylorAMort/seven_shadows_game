import pygame
from UI_focus.buttons import GameState, Button
from UI_focus.font_render import create_surface_with_text_fancy, create_surface_with_text
from playervariables.playertypes import *
from constants import *
from pygame.sprite import RenderUpdates
from UI_focus.UI_functions import *

def inventory_screen(screen, player):
    def draw_inventory(surface):
        y = SCREEN_HEIGHT // 5
        for item in player.inventory:
            object = create_surface_with_text(
                text=f"{item.name}: {item.description}",
                font_size=20,
                text_rgb=(255, 255, 255),
                bg_rgb=(0, 0, 0),
            )
            surface.blit(object, object.get_rect(left= 30, y=y))
            y += 40    
    
    return_btn = Button(
        center_position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 * 3.5),
        image=None,
        font_size=20,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Return to game",
        action=GameState.PLAYING,
    )

    buttons = RenderUpdates(return_btn)
    return game_loop(screen, buttons, extra_draw_callback=draw_inventory)


def fight_screen(screen, player, story):


def title_screen(screen):
    start_btn = Button(
        center_position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50),
        font_size=30,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Start",
        action=GameState.NEWGAME,
    )
    quit_btn = Button(
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
    return game_loop(screen, buttons, extra_draw_callback=lambda surface: surface.blit(title, title_rect)).action

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
    first_row = selection_rect.bottom + 140
    second_row = first_row + 200
    positions_row_1 = [(SCREEN_WIDTH // 5 * (i + 1), first_row) for i in range(4)]
    positions_row_2 = [(SCREEN_WIDTH // 4 * (i + 1), second_row) for i in range(3)]

    shadow_btn = Button(
        center_position=positions_row_1[0],
        image=assets["SHADOW_IMAGE"],
        font_size=30,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Shadow",
        action=Shadow(name, 100, 10, 10, 10, 10),
        subtitle="Large boost to dexterity",
        subsubtitle="Moderate boost to intelligence"
    )

    flame_btn = Button(
        center_position=positions_row_2[2],
        image=assets["FLAME_IMAGE"],
        font_size=30,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Flame",
        action=Flame(name, 100, 10, 10, 10, 10),
        subtitle="Large boost to strength",
        subsubtitle="Moderate boost to dexterity"
    )

    blood_btn = Button(
        center_position=positions_row_2[0],
        image=assets["BLOOD_IMAGE"],
        font_size=30,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Blood",
        action=Blood(name, 100, 10, 10, 10, 10),
        subtitle="Large boost to intelligence",
        subsubtitle="Moderate boost to dexterity"
    )
        

    memory_btn = Button(
        center_position=positions_row_1[3],
        image=assets["MEMORY_IMAGE"],
        font_size=30,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Memory",
        action=Memory(name, 100, 10, 10, 10, 10),
        subtitle="Large boost to wisdom",
        subsubtitle="Moderate boost to intelligence"
    )

    stone_btn = Button(
        center_position=positions_row_1[2],
        image=assets["STONE_IMAGE"],
        font_size=30,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Stone",
        action=Stone(name, 100, 10, 10, 10, 10),
        subtitle="Large boost to strength",
        subsubtitle="Moderate boost to wisdom"
    )

    tide_btn = Button(
        center_position=positions_row_1[1],
        image=assets["TIDE_IMAGE"],
        font_size=30,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Tide",
        action=Tide(name, 100, 10, 10, 10, 10),
        subtitle="Large boost to intelligence",
        subsubtitle="Moderate boost to strength"
    )

    wind_btn = Button(
        center_position=positions_row_2[1],
        image=assets["WIND_IMAGE"],
        font_size=30,
        bg_rgb=(0, 0, 0),
        text_rgb=(255, 255, 255),
        text="Wind",
        action=Wind(name, 100, 10, 10, 10, 10),
        subtitle="Large boost to dexterity",
        subsubtitle="Moderate boost to wisdom"
    )
    buttons = RenderUpdates(shadow_btn, flame_btn, blood_btn, memory_btn, stone_btn, tide_btn, wind_btn)
    player = game_loop(screen, buttons, extra_draw_callback=lambda surface: surface.blit(selection, selection_rect)).action
    
    return player