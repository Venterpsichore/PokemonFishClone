import pygame
import config

class Player:
    def __init__(self, x_position, y_position):
        print("player created")
        self.position = (x_position, y_position)
        self.image = pygame.image.load("Spillycup/!$PianoKid.png")
        self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        self.rect = pygame.Rect(pygame.draw.rect(screen, config.WHITE, (self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, config.SCALE), 4)
)

        def update(self):
            print("player updated")

        def update_position(self, x_change, y_change):
            self.position[0] += x_change
            self.position[0] += y_change
            self.rect = pygame.draw.rect(screen, config.WHITE, (self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, config.SCALE), 4)



        def render(self,screen):
            screen.blit(self.image, self.rect)