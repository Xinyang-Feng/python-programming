import sys
import pygame
from settings import Settings
from ship import ship

def run_game():
    # Initialize game, settings and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)

    # Set the background colour
    bg_color = (230, 230, 230)

    # Start the main loop for the game.
    While True:

        # Watch for keyboard and mouse event.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the window
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()






































