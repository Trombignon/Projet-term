import pygame, json, os

class SpriteSheet:
    """
    Classe pour gérer les spritesheets.
    """
    def __init__(self, nom_fichier):
        """
        Constructeur qui charge l'image mit en paramètre ainsi que le fichier json
        de cette image.
        """
        assert isinstance(nom_fichier, str), "Le fichier mit en parametre n'est pas une chaine de caractere"
        
        self.nom_fichier = os.path.join("..", "images", "spritesheets", nom_fichier)
        self.spritesheet =  pygame.image.load(self.nom_fichier).convert_alpha()
        self.meta_data = self.nom_fichier.replace(".png", ".json")
        with open(self.meta_data) as fichier:
            self.donnees = json.load(fichier)
        
    
    def get_image(self, position_x, position_y, width, height, scale):
        """
        Méthode pour charger une certaine image dans le spritesheet à partir
        de sa position et sa taille, et la tansforme à l'echelle requis.
        """
        assert isinstance(position_x, int), "Le premier argument n'est pas un entier"
        assert isinstance(position_y, int), "Le second argument n'est pas un entier"
        assert isinstance(width, int), "Le troisieme argument n'est pas un entier"
        assert isinstance(height, int), "Le quatrieme argument n'est pas un entier"
        assert isinstance(scale, int) or isinstance(scale, float), "Le dernier argument n'est pas un entier ni un float"
        
        image = pygame.surface((width, height), pygame.SRCALPHA)
        image.blit(self.spritesheet, (0,0), (x, y, w, h))
        image = pygame.transform.scale(image, (w * scale, h * scale))
        return image
    
    
    def parse(self, nom_image):
        pass