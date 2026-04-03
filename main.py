import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def main():
    pygame.init()
    pygame.display.set_caption("Seven Shadows of the Shattered Blade")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font("elvencommonspeak2.ttf", 36)
    text_surface = font.render("Seven Shadows of the Shattered Blade", True, (255, 255, 255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, SCREEN_HEIGHT // 2 - text_surface.get_height() // 2))
        pygame.display.flip()
    
    


if __name__ == "__main__":
    main()
