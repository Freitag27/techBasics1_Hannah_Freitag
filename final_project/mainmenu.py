import pygame
import sys
import os
import tremblingtunnels
import achievements

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)

PLAY_LIGHT = (38, 40, 35)
PLAY_DARK = (2, 4, 3)

QUIT_LIGHT = (31, 17, 17)
QUIT_DARK = (2, 4, 3)

ACH_LIGHT = (71, 72, 63)
ACH_DARK = (2, 4, 3)

script_dir = os.path.dirname(os.path.abspath(__file__))
Background_path = os.path.join(script_dir, "assets", "backgrounds", "cave_main_menu.jpg")

font = pygame.font.SysFont("Poor Richard", 40)
logo_font = pygame.font.SysFont("Poor Richard", 80)

background = pygame.image.load(Background_path)
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

def start_menu(screen):
    while True:
        mouse = pygame.mouse.get_pos()

        screen.blit(background, (0, 0))
        logo_text = logo_font.render("Trembling Tunnels", True, WHITE)
        logo_rect = logo_text.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(logo_text, logo_rect)

        # --- DYNAMICALLY CENTERED BUTTONS ---
        play_width, play_height = 140, 50
        play_button = pygame.Rect((SCREEN_WIDTH // 2) - (play_width // 2), 200, play_width, play_height)

        quit_width, quit_height = 140, 50
        quit_button = pygame.Rect((SCREEN_WIDTH // 2) - (quit_width // 2), 300, quit_width, quit_height)

        ach_width, ach_height = 300, 50
        achievements_button = pygame.Rect((SCREEN_WIDTH // 2) - (ach_width // 2), 400, ach_width, ach_height)

        # Draw Buttons
        pygame.draw.rect(screen, PLAY_LIGHT if play_button.collidepoint(mouse) else PLAY_DARK, play_button)
        pygame.draw.rect(screen, QUIT_LIGHT if quit_button.collidepoint(mouse) else QUIT_DARK, quit_button)
        pygame.draw.rect(screen, ACH_LIGHT if achievements_button.collidepoint(mouse) else ACH_DARK, achievements_button)

        # Render Text
        play_text = font.render("Play", True, WHITE)
        quit_text = font.render("Quit", True, WHITE)
        achievements_text = font.render("Achievements", True, WHITE)

        # --- CENTER TEXT INSIDE BUTTONS ---
        play_text_rect = play_text.get_rect(center=play_button.center)
        quit_text_rect = quit_text.get_rect(center=quit_button.center)
        achievements_text_rect = achievements_text.get_rect(center=achievements_button.center)

        # Draw Text
        screen.blit(play_text, play_text_rect)
        screen.blit(quit_text, quit_text_rect)
        screen.blit(achievements_text, achievements_text_rect)

        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(mouse):
                    tremblingtunnels.run_game(screen)

                if achievements_button.collidepoint(mouse):
                    achievements.show_achievements(screen)

                if quit_button.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()