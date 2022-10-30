import pygame
from comet import Comet

# créer une classe pour gérer cet événement à interval régulier

class CometFallEvent:
    
    #lors du chargement -> créer un compteur 
    def __init__(self):
        self.percent = 0
        self.percent_speed = 33
        
    
        #definir un groupe de sprite pour stocker nos comètes
        self.all_comets = pygame.sprite.Group()
        
    
    def add_percent(self):
        self.percent += self.percent_speed / 100
    
    def is_full_loaded(self):
        return self.percent >= 100
    
    def reset_percent(self):
        self.percent = 0
        
    def meteor_fall(self):
        # faire apparaitre une première boule de feu
        self.all_comets.add(Comet())
        
    def attempt_fall(self):
        # la jauge d'évènement est totalement chargée 
        if self.is_full_loaded():
            print('pluie de comètes !! ')
            self.meteor_fall()
            self.reset_percent()
            
    
    def update_bar(self, surface):
        # ajouter du poucentage a la barre 
        self.add_percent()
        
        # appel de la méthode pour essayer de déclencher la pluei de comètes 
        self.attempt_fall()
        # barre noir (en arrière plan)
        pygame.draw.rect(surface, (0,0,0), [
		0, # l'axe des X 
		surface.get_height() -20 , # l'axe des y 
		surface.get_width(), # longueur de la fenêtre
		10 # épaisseur de la barre
		])
        #barre rouge (jauge d'event)
        pygame.draw.rect(surface, (187,11,11), [
		0, # l'axe des X 
		surface.get_height() -20, # l'axe des y 
		(surface.get_width() / 100) * self.percent, # longueur de la fenêtre
		10 # épaisseur de la barre
		])