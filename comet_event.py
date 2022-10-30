import pygame

# créer une classe pour gérer cet événement à interval régulier

class CometFallEvent:
    
    #lors du chargement -> créer un compteur 
    def __init__(self):
        self.percent = 0
        self.percent_speed = 5
        
    
    def add_percent(self):
        self.percent += self.percent_speed / 100
    
    def update_bar(self, surface):
        # ajouter du poucentage a la barre 
        self.add_percent()
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