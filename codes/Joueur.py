import pygame

class Joueur:
    
    def __init__(self, position_x, position_y, image):
        self.position_x = position_x
        self.position_y = position_y
        self.image = image

    def update(self, dt):
        pass
    
    
    def dessiner(self, surface):
        surface.blit(self.image, (self.position_x, self.position_y))