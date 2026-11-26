import pygame
from Joueur import Joueur
from Niveau import Niveau


class SceneJeu:
    """
    Classe pour la scene de jeu.
    """
    def __init__(self, jeu):
        """
        Constructeur qui initialise les variable pour la scene.
        
        Parametre:
        Prends en parametre l'objet Jeu()
        """
        #assert isinstance(jeu, Jeu), "La variable mit en parametre n'est pas l'objet Jeu()"
        self.jeu = jeu
        self.image1 = pygame.image.load("../images/PERSO-32.png")
        self.image1 = pygame.transform.scale(self.image1, (128, 128))
        self.perso1 = Joueur(50, 50, self.image1)
        
        self.image2 = pygame.image.load("../images/PERSO-24.png")
        self.image2 = pygame.transform.scale(self.image2, (96, 96))
        self.perso2 = Joueur(160, 50, self.image2)
        
    
    def handle_events(self, event):
        """
        Méthode qui gère tout les evenements qui se passe dans la classe SceneJeu.
        
        Paramètre:
        event: prends un event en paramètre passer par la classe Jeu.
        """
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.jeu.set_running(False)
                
    
    def update(self, dt):
        """
        Méthode pour mettre a jour l'etat de la classe SceneJeu.
        """
        pass
    
    
    def dessiner(self, surface):
        """
        Méthode qui gere l'affichage de la classe.
        
        Paramètre:
        surface: prends une surface en paramètre tel que ecran
        """
        surface.fill("blue")
        self.perso1.dessiner(surface)
        self.perso2.dessiner(surface)