import pygame
import sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()
        self.level = Level()

        # Sound
        main_sound = pygame.mixer.Sound('audio/main.ogg')
        main_sound.set_volume(0.5)
        main_sound.play(loops=-1)

        # Font setup
        self.font = pygame.font.Font(None, 36)  # Define a font for button labels

        # Opening screen setup
        self.show_opening_screen()

    def show_opening_screen(self):
        play_button_width = 200
        play_button_height = 50
        button_spacing = 20  # Spacing between buttons

        # Calculate positions to center buttons vertically and horizontally
        total_button_height = play_button_height * 2 + button_spacing
        top_margin = (HEIGTH - total_button_height) // 2

        play_button_rect = pygame.Rect((WIDTH - play_button_width) // 2, top_margin, play_button_width, play_button_height)
        exit_button_rect = pygame.Rect((WIDTH - play_button_width) // 2, top_margin + play_button_height + button_spacing, play_button_width, play_button_height)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if play_button_rect.collidepoint(mouse_pos):
                        return  # Exit the opening screen loop and start the game
                    elif exit_button_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

            # Drawing the opening screen
            self.screen.fill(WATER_COLOR)
            # Draw play and exit buttons on the screen using pygame.draw.rect
            pygame.draw.rect(self.screen, (50, 150, 255), play_button_rect)  # Play button
            pygame.draw.rect(self.screen, (255, 50, 50), exit_button_rect)  # Exit button

            # Render text labels for buttons
            play_text = self.font.render("Play", True, (255, 255, 255))
            exit_text = self.font.render("Exit", True, (255, 255, 255))

            # Center the text inside the buttons
            play_text_rect = play_text.get_rect(center=play_button_rect.center)
            exit_text_rect = exit_text.get_rect(center=exit_button_rect.center)

            # Blit the text labels onto the buttons
            self.screen.blit(play_text, play_text_rect)
            self.screen.blit(exit_text, exit_text_rect)

            pygame.display.update()
            self.clock.tick(FPS)

    def run(self):
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
