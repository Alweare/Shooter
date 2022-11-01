import pygame


#définir une classe qui va s'occuper des animations 
class AnimateSprite(pygame.sprite.Sprite):
    
    #définir les choses a faire a la création de l'entité
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'Assets/{sprite_name}.png')
        self.current_image = 0 #commencer l'animation a l'image 0
        self.images = animations.get(sprite_name)
        
    # définir une méthode pour animer le sprite
    def animate(self):
        
        #passer a l'image suivante
        self.current_image += 1
        
        #vérifier si on a atteint la fin de l'animation
        
        if self.current_image >= len(self.images):
            #remettre l'animation au départ
            self.current_image = 0
        
        #modifier l'image de l'animation précédente par la suivante
        self.image  = self.images[self.current_image]
    
    
    
    
#définir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    #charger les 24 images de ce sprite dans le dossier correspondant
    images = []
    #récupérer le chemin du dossier pour ce sprite
    path  = f"Assets/{sprite_name}/{sprite_name}"
    
    #boucler sur chaque image dans ce dossier 
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
    
    # renvoyer le contenu de la liste d'image
    return images

# définir un dictionnaire qui va contenir les images charger de chaque sprite
# mummy -> [...mummy1.png,...]

animations = {
	'mummy': load_animation_images('mummy')
}
        
        
 
        
    