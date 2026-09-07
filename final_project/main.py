import pygame
import sys

pygame.init()
pygame.mixer.init()
# Screen dimensions



SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Trembling Tunnels")

# Import AFTER pygame.init()
import mainmenu

# Start the menu
mainmenu.start_menu(screen)

pygame.quit()
sys.exit()