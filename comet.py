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
        
        #verifier si le nombre de comète est de zero 
        if len(self.comet_event.all_comets) == 0:
            # remettre la barre à 0 
            self.comet_event.reset_percent()
            #apparaitre a nouveau les deux premier monstre 
            self.comet_event.game.start()
           

    def fall(self):
        self.rect.y += self.velocity
        
        # ne tombe pas sur le sol
        if self.rect.y >= 500:
            # retirer la boule de feu
            self.remove()
            
            # s'il n'y a plus de boule de feu sur le jeu
            if len(self.comet_event.all_comets) == 0:
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False
        
        # verifier si la boule de feu touche le joueur 
        if self.comet_event.game.check_collision( 
        	self,self.comet_event.game.all_players):
            # retirer la boule de feu
            self.remove()
            #subir 20 point de dégats
            self.comet_event.game.player.damage(20)