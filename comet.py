import pygame
import random


#créer une classe pour gérer cette comète

class Comet(pygame.sprite.Sprite):
    
    def __init__(self, comet_event):
        super().__init__()
        # définir l'image de la comète
        self.image = pygame.image.load('Assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20,800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event
    
    def remove(self):
        self.comet_event.all_comets.remove(self)

    def fall(self):
        self.rect.y += self.velocity
        
        # ne tombe pas sur le sol
        if self.rect.y >= 500:
            print('sol')
            # retirer la boule de feu
            self.remove()
        
        # verifier si la boule de feu touche le joueur 
        if self.comet_event.game.check_collision( 
        	self,self.comet_event.game.all_players):
            print('joueur touché')
            # retirer la boule de feu
            self.remove()
            #subir 20 point de dégats
            self.comet_event.game.player.damage(20)