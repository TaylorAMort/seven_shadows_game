import pygame
from pygame import surface
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
                text_rgb=WHITE,
                bg_rgb=BLACK,
            )
            surface.blit(object, object.get_rect(left= 30, y=y))
            y += 40    
    
    return_btn = Button(
        center_position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 * 3.5),
        image=None,
        font_size=20,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Return to game",
        action=GameState.PLAYING,
    )

    buttons = RenderUpdates(return_btn)
    return game_loop(screen, buttons, extra_draw_callback=draw_inventory)


def fight_screen(screen, player, story):
    rtn_btn, inventory_btn = nav_buttons(screen, player)
    monster = story.current_monster
    weapon = story.current_monster_weapon
    lines = [f"The {monster.name} sniffs the air, awaiting its moment to strike."]
    row = [(SCREEN_WIDTH // 4 * (i + 1), button_y(lines)) for i in range(3)]
    def reposition_buttons(btns, new_y):
        for btn in btns:
            for rect in btn.rects:
                rect.centery = new_y
    attack_btn = Button(
        center_position=(row[0]),
        image=None,
        font_size=20,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Attack",
        choice="Attack",
        border_rgb=WHITE
    )
    defend_btn = Button(
        center_position=(row[1]),
        image=None,
        font_size=20,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Defend",
        choice="Defend",
        border_rgb=WHITE
    )
    run_btn = Button(
        center_position=(row[2]),
        image=None,
        font_size=20,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Run",
        choice="Run",
        border_rgb=WHITE
    )
    resume_btn = Button(
        center_position=(row[1]),
        image=None,
        font_size=20,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Return",
        choice="Return to level",
        border_rgb=WHITE
    )
    
    buttons = RenderUpdates(rtn_btn, inventory_btn, attack_btn, defend_btn, run_btn)
    counter = 0
    while True:
        result = game_loop(screen, buttons, extra_draw_callback=lambda surface: draw_lines(surface, lines))
        if result.action == GameState.INVENTORY:
            inventory_screen(screen, player)
        elif result.choice == "Attack":
            damage, alive = player.attack(monster, player.inventory[0])
            if alive == True:
                m_damage, p_alive = monster.attack(player, story.current_monster_weapon)
                lines = [f"You attacked the {monster.name} for {damage} damage!",
                         f"The {monster.name} attacked for {m_damage} damage!",
                         f"Your health is {player.health}."]
                reposition_buttons([attack_btn, defend_btn, run_btn, resume_btn], button_y(lines))
                if p_alive == False:
                    lines = [f"You have been defeated by the {monster.name}...",
                             "You awaken just before the battle, your memories clear but your body whole."]
                    reposition_buttons([attack_btn, defend_btn, run_btn, resume_btn], button_y(lines))
                    buttons.remove(attack_btn, defend_btn, run_btn)
                    buttons.add(resume_btn)
            else:
                lines = [f"You have defeated the {monster.name}!"]
                reposition_buttons([attack_btn, defend_btn, run_btn, resume_btn], button_y(lines))
                buttons.remove(attack_btn, defend_btn, run_btn)
                buttons.add(resume_btn)
        elif result.choice == "Defend":
            defense = player.defend(monster.attack(player, story.current_monster_weapon)[0])
            lines = [f"You defended against the attack, taking only {defense} damage!"]
            reposition_buttons([attack_btn, defend_btn, run_btn, resume_btn], button_y(lines))
        elif result.choice == "Run":
            ran = player.run(monster)
            if ran == True:
                lines = [f"You successfully escaped from the {monster.name}!"]
                reposition_buttons([attack_btn, defend_btn, run_btn, resume_btn], button_y(lines))
                buttons.remove(attack_btn, defend_btn, run_btn)
                buttons.add(resume_btn)
            else:
                m_damage, p_alive = monster.attack(player, story.current_monster_weapon)
                if p_alive == True:
                    lines = [f"You failed to escape from the {monster.name}!",
                            f"The {monster.name} attacked for {m_damage} damage!",
                            f"Your health is {player.health}."]
                    reposition_buttons([attack_btn, defend_btn, run_btn, resume_btn], button_y(lines))
                else:
                    lines = [f"You have been defeated by the {monster.name}...",
                             "You awaken just before the battle, your memories clear but your body whole."]
                    reposition_buttons([attack_btn, defend_btn, run_btn, resume_btn], button_y(lines))
                    buttons.remove(attack_btn, defend_btn, run_btn)
                    buttons.add(resume_btn)
        elif result.choice == "Return to level":
            return story.fight_return
        else:
            return GameState.TITLE
        


def title_screen(screen):
    start_btn = Button(
        center_position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Start",
        action=GameState.NEWGAME,
    )
    quit_btn = Button(
        center_position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 * 2.5),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )
    
    title = create_surface_with_text_fancy(
        text="Seven Shadows of the Shattered Blade",
        font_size=80,
        text_rgb=WHITE,
        bg_rgb=BLACK,
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

        screen.fill(WHITE)

        title_surf = create_surface_with_text(
            text="Enter your name:",
            font_size=36,
            text_rgb=WHITE,
            bg_rgb=BLACK,
        )
        screen.blit(title_surf, title_surf.get_rect(centerx=SCREEN_WIDTH // 2, y=180))


        pygame.draw.rect(screen, (100, 100, 100), box_rect, border_radius=8)
        pygame.draw.rect(screen, (200, 200, 200), box_rect, width=2, border_radius=8)

        name_surf = create_surface_with_text(
            text=name,
            font_size=28,
            text_rgb=(BLACK),
            bg_rgb=(WHITE),
        )
        text_x = box_rect.x + 14
        text_y = box_rect.centery - name_surf.get_height() // 2
        screen.blit(name_surf, (text_x, text_y))

        hint_surf = create_surface_with_text(
            text="Press Enter to confirm",
            font_size=18,
            text_rgb=WHITE,
            bg_rgb=BLACK,
        )
        screen.blit(hint_surf, hint_surf.get_rect(centerx=SCREEN_WIDTH // 2, y=box_rect.bottom + 18))

        pygame.display.flip()


    return class_selection_screen(screen, name, assets)


def class_selection_screen(screen, name, assets):
    
    
    selection = create_surface_with_text(
        text=f"Welcome, {name}. Select your class:",
        font_size=40,
        text_rgb=WHITE,
        bg_rgb=BLACK,
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
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Shadow",
        action=Shadow(name, 100, 10, 10, 10, 10),
        subtitle="Large boost to dexterity",
        subsubtitle="Moderate boost to intelligence"
    )

    flame_btn = Button(
        center_position=positions_row_2[2],
        image=assets["FLAME_IMAGE"],
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Flame",
        action=Flame(name, 100, 10, 10, 10, 10),
        subtitle="Large boost to strength",
        subsubtitle="Moderate boost to dexterity"
    )

    blood_btn = Button(
        center_position=positions_row_2[0],
        image=assets["BLOOD_IMAGE"],
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Blood",
        action=Blood(name, 100, 10, 10, 10, 10),
        subtitle="Large boost to intelligence",
        subsubtitle="Moderate boost to dexterity"
    )
        

    memory_btn = Button(
        center_position=positions_row_1[3],
        image=assets["MEMORY_IMAGE"],
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Memory",
        action=Memory(name, 100, 10, 10, 10, 10),
        subtitle="Large boost to wisdom",
        subsubtitle="Moderate boost to intelligence"
    )

    stone_btn = Button(
        center_position=positions_row_1[2],
        image=assets["STONE_IMAGE"],
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Stone",
        action=Stone(name, 100, 10, 10, 10, 10),
        subtitle="Large boost to strength",
        subsubtitle="Moderate boost to wisdom"
    )

    tide_btn = Button(
        center_position=positions_row_1[1],
        image=assets["TIDE_IMAGE"],
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Tide",
        action=Tide(name, 100, 10, 10, 10, 10),
        subtitle="Large boost to intelligence",
        subsubtitle="Moderate boost to strength"
    )

    wind_btn = Button(
        center_position=positions_row_2[1],
        image=assets["WIND_IMAGE"],
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Wind",
        action=Wind(name, 100, 10, 10, 10, 10),
        subtitle="Large boost to dexterity",
        subsubtitle="Moderate boost to wisdom"
    )
    buttons = RenderUpdates(shadow_btn, flame_btn, blood_btn, memory_btn, stone_btn, tide_btn, wind_btn)
    player = game_loop(screen, buttons, extra_draw_callback=lambda surface: surface.blit(selection, selection_rect)).action
    
    return player