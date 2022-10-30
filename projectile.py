import pygame
from pyscreeze import center

# definir la classe qui va gérer le projectile de notre joueur

class Projectile(pygame.sprite.Sprite):
    
    #definir le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 2 
        self.player = player
        self.image = pygame.image.load('Assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0
        
    def rotate(self):
        #faire tourner le projectile en déplacement
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image,self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        
    def remove(self):
        self.player.all_projectiles.remove(self)    
        
    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        # verifier si le projectile touche un monstre
        
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # supprimer le projectile
            self.remove()
            #infliger des dégâts
            monster.damage(self.player.attack)
            
        
        #condition pour vérifier si notre projectile n'est plus présent sur l'écran
        
        if self.rect.x > 1080:
            #supprimer le projectile
            self.remove()
            
            

        
        
            
       