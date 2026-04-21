import pygame
from UI_focus.buttons import GameState, Button
from UI_focus.font_render import create_surface_with_text
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, TEXT_START_Y, LINE_HEIGHT, BLACK, WHITE



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
                return button
            button.draw(screen)
        pygame.display.flip()

def nav_buttons(screen, player):
    return_btn = Button(
        center_position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 * 3.5),
        font_size=20,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Return to main menu",
        action=GameState.TITLE,
    )

    inventory_btn = Button(
        center_position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 * 3.25),
        font_size=20,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Inventory",
        action=GameState.INVENTORY,
    )
    return return_btn, inventory_btn

def draw_lines(surface, lines):
    y = TEXT_START_Y
    for line in lines:
        surf = create_surface_with_text(line, 20, WHITE, BLACK)
        surface.blit(surf, surf.get_rect(centerx=SCREEN_WIDTH // 2, y=y))
        y += LINE_HEIGHT

def text_end_y(lines):
    return TEXT_START_Y + len(lines) * LINE_HEIGHT

def button_y(lines):
    return text_end_y(lines) + LINE_HEIGHT