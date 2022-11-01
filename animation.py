import pygame


#définir une classe qui va s'occuper des animations 
class AnimateSprite(pygame.sprite.Sprite):
    
    #définir les choses a faire a la création de l'entité
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'Assets/{sprite_name}.png')
        self.current_image = 0 #commencer l'animation a l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False
      
    #définir une méthode pour démarrer l'animation
    def start_animation(self):
        self.animation = True
    def animate(self, loop=False):
        if self.animation:
            self.current_image +=1
            if self.current_image >= len(self.images):
                self.current_image=0
                #vérifier si l'animation n'est pas en mode couble
                if loop is False:
                #désactivetaion de l'animation
                    self.animation=False
            self.image = self.images[self.current_image]
        

    
            
    
    
    
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
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player')
}
        
        
 
        
    