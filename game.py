import pygame

from player import Player
from monster import Monster
from comet_event import CometFallEvent

#creer une seconde classe qui va representer notre jeu
class Game : 
    def __init__(self):
        # definir si notre jeu ea commencé ou non 
        self.is_playing = False
       #generer notre joueur
        self.all_players = pygame.sprite.Group() 
        self.player = Player(self)
        self.all_players.add(self.player)
        # générer l'événement
        self.comet_event = CometFallEvent(self)
        #groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
    
        
    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()
        
    def game_over(self):
        #remettre le jeu a neuf, retirer les monstres, remettre le joueur a 100 de vie, remettre le jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_percent()
        self.player.health = self.player.max_health
        self.is_playing = False
        
    def update(self, screen):
        #appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)
        
        #actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)
        #actualiser la barre d'événement du jeu
        self.comet_event.update_bar(screen)
        
        #actualiser l'animation du joueur
        self.player.update_animation()
        
        
        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()
        
        #récupérer les monstres de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()
        
        # récupérer les comètes de notre jeu 
        for comet in self.comet_event.all_comets:
            comet.fall()
        
        #appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)
        
        #appliquer l'ensemble des image de mon groupe de monstre
        self.all_monsters.draw(screen)
        
        #appliquer l'ensemnle des images de mon groupe comète
        
        self.comet_event.all_comets.draw(screen)
        
        #verifier si le joueur veut aller a gauche ou a droite 
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
    
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
        
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)