from UI_focus.buttons import *
from UI_focus.UI_functions import *
from playervariables.playertypes import *
from constants import *
from gamefunctions.screens import inventory_screen
from pygame.sprite import RenderUpdates





def play_level_1(screen, player, story):
    return_btn, inventory_btn = nav_buttons(screen, player)
    lines = [
        "The dungeon smells of rot and decay.",
        "The moans of the imprisoned and the clinking of chains create a cacophony of death.",
        "To be damned here is to suffer for eternity.",
        f"But you are far from damned {player.name}."
    ]

    continue_btn = Button(
        center_position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 * 2),
        font_size=20,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Go further into the dungeon",
        action=GameState.LEVEL_2,
        border_rgb=WHITE,
    )

    buttons = RenderUpdates(return_btn, inventory_btn, continue_btn)

    while True:
        result = game_loop(screen, buttons, extra_draw_callback=lambda surface: draw_lines(surface, lines))
        if result.action == GameState.INVENTORY:
            inventory_screen(screen, player)
        elif result.action == GameState.LEVEL_2:
            return GameState.LEVEL_2
        else:
            return GameState.TITLE
        
def play_level_2(screen, player, story):
    story.enter_scene("End of the Hallway")
    round = story.rounds("End of the Hallway")
    return_btn, inventory_btn = nav_buttons(screen, player)

    if round == 1:
        lines = [
        "Your steps echo through the abandoned hallway.",
        "Up ahead, you see a thin light flickering. A door, forgotten by time.",
        "As you press it open, you see an empty room, the furniture broken and decayed.",
        "On the left wall, another door stands, the flickering of torchlight coming from the other side."
        ]

    elif round == 2:
        lines = [
            "In the remains of the once ornate nighstand you find a note.",
            "It reads: 'The blade only serves itself.'",
            "The rest of the note is unreadable."
        ]
        story.make_choice("Found note in hallway")

    else:
        lines = [
            "The room is still empty and desolate."
        ]

    row = [(SCREEN_WIDTH // 3 * (i + 1), button_y(lines)) for i in range(2)]


    look_around_btn = Button(
        center_position=(row[0]),
        font_size=20,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Look around the room",
        action=GameState.REPEAT,
        border_rgb=WHITE,
    )
    leave_pos = (SCREEN_WIDTH // 2, button_y(lines)) if round >= 2 else row[1]
    Leave_btn = Button(
        center_position=(leave_pos),
        font_size=20,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Go through the door",
        action=GameState.LEVEL_3,
        border_rgb=WHITE,
    )
    Go_back_btn = Button(
        center_position=(SCREEN_WIDTH // 2, button_y(lines)),
        font_size=20,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Go back",
        action=GameState.REPEAT,
        border_rgb=WHITE,
    )
    buttons = RenderUpdates(return_btn, inventory_btn, look_around_btn, Leave_btn)
    if round == 2:
        buttons.add(Go_back_btn)
        buttons.remove(look_around_btn)
        buttons.remove(Leave_btn)
    if round == 3:
        buttons.remove(look_around_btn)
    while True:
        result = game_loop(screen, buttons, extra_draw_callback=lambda surface: draw_lines(surface, lines))
        if result.action == GameState.INVENTORY:
            inventory_screen(screen, player)
        elif result.action == GameState.REPEAT:
            return GameState.REPEAT
        elif result.action == GameState.LEVEL_3:
            return GameState.LEVEL_3
        else:
            return GameState.TITLE
        
def play_level_3(screen, player, story):
    monster = Player("Monster", 100, 20, 5, 5, 5)
    story.current_monster = monster
    story.enter_scene("The Castle Proper")
    return_btn, inventory_btn = nav_buttons(screen, player)
    round = story.rounds("The Castle Proper")
    
    if round == 1:
        lines = [
        "You enter an older section of the castle proper, the torches lit but the walls cracked and crumbling.",
        "Now, past the dungeon, the real danger awaits you.",
        "You must find the Hilt of the Shadows here. Only then can you set things right.",
        "The castle crawls with ancient beasts tamed by modern monsters. Be on your guard."
        ]

    elif round == 2:
        lines = [
            "You continue down the hallway, your footsteps echoing in the silence.",
            "It's a feeling before anything else. The hairs on the back of your neck stand up, and you know something is watching you.",
            "The air in front of you shivers and distorts, the shape monstrously huge.",
            "What do you do?"
        ]
    elif round == 3 and story.has_made_choice("Fight the monster in the hallway"):
        lines = [
            "You draw your weapon and prepare to fight.",
            "The monster materializes, a lizard-like beast with horns protruding from all over its body. It roars and lunges."
        ]
        
    
    elif round == 3 and story.has_made_choice("Sneak past the monster in the hallway"):
        lines = [
            "You try to sneak past the monster, holding your breath and moving as silently as possible.",
        ]
        sneaking = player.sneak(monster)
        if sneaking == True:
            lines.remove("You try to sneak past the monster, holding your breath and moving as silently as possible.")
            lines.append("You successfully sneak past the monster, moving with the shadows of the torchlight, and continue down the hallway.")
            story.make_choice("Successfully sneaked past the monster in the hallway")
        else: 
            lines.append("You fail to sneak past the monster and alert it to your presence. It roars and lunges.")
            story.make_choice("Failed to sneak past the monster in the hallway")
    elif round == 4: 
        pass
    else:
        lines = ["filler"]

    row = [(SCREEN_WIDTH // 3 * (i + 1), button_y(lines)) for i in range(2)]

    continue_btn = Button(
        center_position=(SCREEN_WIDTH // 2, button_y(lines)),
        font_size=20,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Walk down the hallway",
        action=GameState.REPEAT,
        border_rgb=WHITE,
    )
    draw_btn = Button(
        center_position=(row[0]),
        font_size=20,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Draw your weapon",
        action=GameState.REPEAT,
        border_rgb=WHITE,
        choice="Fight the monster in the hallway"
    )
    sneak_btn = Button(
        center_position=(row[1]),
        font_size=20,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Try to sneak past",
        action=GameState.REPEAT,
        border_rgb=WHITE,
        choice="Sneak past the monster in the hallway"
    )
    attack_btn = Button(
        center_position=(SCREEN_WIDTH // 2, button_y(lines)),
        font_size=20,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Attack",
        action=GameState.FIGHT,
        border_rgb=WHITE,
    )

    buttons = RenderUpdates(return_btn, inventory_btn, continue_btn)
    if round == 2:
        buttons.remove(continue_btn)
        buttons.add(draw_btn)
        buttons.add(sneak_btn)
    if round == 3:
        buttons.remove(continue_btn)
        buttons.remove(draw_btn)
        buttons.remove(sneak_btn)
    
    while True:
        result = game_loop(screen, buttons, extra_draw_callback=lambda surface: draw_lines(surface, lines))
        if result.action == GameState.INVENTORY:
            inventory_screen(screen, player)
        elif result.action == GameState.REPEAT:
            if result.choice == "Fight the monster in the hallway":
                story.make_choice("Fight the monster in the hallway")
            elif result.choice == "Sneak past the monster in the hallway":
                story.make_choice("Sneak past the monster in the hallway")
            return GameState.REPEAT
        elif result.action == GameState.LEVEL_4:
            return GameState.LEVEL_4
        else:
            return GameState.TITLE






    