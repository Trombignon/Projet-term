import pygame
from scenes import SceneJeu

pygame.init()

Native_resolution = (320, 180)
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()

class Jeu:
    """
    Classe qui gère la boucle principale du jeu.
    """
    def __init__(self):
        """
        Constructeur qui initialise la variable pour faire tourner la boucle principale,
        une surface sur laquelle tout est dessiner et la premiere scene.
        
        Paramètres:
        Ne prends aucun paramètres.
        """
        self.running = True
        self.surface = pygame.Surface(Native_resolution, pygame.SRCALPHA)
        self.scene = SceneJeu(self)
        
        
    def set_running(self, run):
        """
        Méthode pour changer la valeur de self.running.
        """
        assert isinstance(run, bool), "La variable mit en paramètre n'est un booléen"
        
        self.running = run
        
    
    def set_scene(self, new_scene):
        """
        Méthode pour changer la scene a une nouvelle scene.
        
        Parmètre:
        Prends un object en paramètre
        """
        assert isinstance(new_scene, SceneJeu), "La variable mit en paramètre n'est pas un object Scene"
        self.scene = new_scene
        
    
    def update(self, dt):
        """
        Méthode qui met à jour le status du jeu grace a dt.
        
        Paramètre:
        dt (float): une variable de type float
        """
        assert isinstance(dt, float), "dt n'est pas correct"
        self.scene.update(dt)
        
    
    def dessiner(self):
        """
        Méthode qui dessine le status
        """
        self.scene.dessiner(screen)
        
    
    def lancer_boucle(self):
        """
        Méthode qui lance la boucle principale du jeu.
        """
        while self.running:
            
            dt = clock.tick(60) / 1000
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    self.set_running(False)
                
                self.scene.handle_events(event)
            
            self.update(dt)
            self.dessiner()
            
            pygame.display.flip()
        
        pygame.quit()
        
    

jeu = Jeu()
jeu.lancer_boucle()