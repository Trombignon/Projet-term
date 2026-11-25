import pygame

class SceneJeu:
     
    def __init__(self, jeu):
        self.jeu = jeu
        self.perso = pygame.image.load("../images/PERSO-32.png")
        self.perso = pygame.transform.scale(self.perso, (128, 128))
        self.perso2 = pygame.image.load("../images/PERSO-24.png")
        self.perso2 = pygame.transform.scale(self.perso, (96, 96))
        
    
    def handle_events(self, event):
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.jeu.set_running(False)
                
    
    def update(self, dt):
        pass
    
    def dessiner(self, surface):
        surface.fill("blue")
        surface.blit(self.perso, (50, 50))
        surface.blit(self.perso2, (160, 50))