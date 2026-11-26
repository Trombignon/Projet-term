import pygame, csv
from Outils import SpriteSheet

class Tuile:
    
    def __init__(self, spritesheet, nom_image, position_x, position_y):
        
        pass
    
    
    def dessiner(self):
        pass
    
    

class Niveau:
    
    def __init__(self, nom_spritesheet, debut_x, debut_y):
        
        self.spritesheet = Spritesheet(nom_spritesheet)
        self.debut_x, self.debut_y = debut_x, debut_y