
from turtle import width
from typing_extensions import Self
import pygame
import math
pygame.init()
from player import Player
from game import Game

       

#générer une fenêtre au jeu

pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080,720))

background = pygame.image.load('Assets/bg.jpg')

# charger notre jeu 
game = Game()

#charger notre joueur
player = Player(Self)

running = True

# boucle tant que cette condition est vrai
while running:
    
    #appliquer l'arrière plan du jeu
    screen.blit(background,(0,-200))
    #importer notre bannière
    banner = pygame.image.load('Assets/banner.png')
    banner = pygame.transform.scale(banner, (500,500))
    banner_rect = banner.get_rect()
    banner_rect.x = math.ceil(screen.get_width() / 4)
    
    #import/charger le bouton pour lancer la partie
    play_button = pygame.image.load('Assets/button.png')
    play_button = pygame.transform.scale(play_button, (400, 150))
    play_button_rect = play_button.get_rect()
    play_button_rect.x = math.ceil(screen.get_width() / 3.33)
    play_button_rect.y = math.ceil(screen.get_height() / 2)
    
    #verifier si notre jeu a commencer ou non 
    if game.is_playing:
        #déclencer les instructions de la partie
        game.update(screen)
        #verifier si notre jeu n'a pas commencé
    else:
        #ajouter écran de bienvenu
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)
        
        
    
    #mettre a jour l'écran
    pygame.display.flip()
    
    #si le joueur ferme cette fenêtre
    for event  in pygame.event.get():
        # que l'evenement est fermeture de fenêtre 
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            
            #detectert si la touche espace est enclecnhé pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verification pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode 'lancé' 
                game.start()
            
    
            