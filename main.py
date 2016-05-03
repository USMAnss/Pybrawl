import pygame, sys
from pygame.locals import *
from character import Character
from hud import Hud
from load import load_image
from settings import *
import dumbmenu as dm


def collide_projectiles(left, right):
    new_projectiles=[]
    for projectile in left.projectiles:
        if projectile.rect.colliderect(right.rect):
            right.take_damage(projectile.damage)
        else:
            new_projectiles.append(projectile)
    left.projectiles=new_projectiles

def collide(left, right):
    # check for player vs projectile collisions
    collide_projectiles(left, right)
    collide_projectiles(right, left)
    # continue with player vs player collision
    if not left.rect.colliderect(right.rect):
        return
    # deal damage
    if left.state=="attack":
        right.take_damage(left.damage)
    if right.state=="attack":
        left.take_damage(right.damage)
    # adjust position
    if left.rect.centerx>right.rect.centerx:
        left, right=right, left
    overlap=left.rect.right-right.rect.left
    if left.state=="stance":
        right.rect.centerx+=overlap
    elif right.state=="stance":
        left.rect.centerx-=overlap
    else:
        left.rect.centerx-=(overlap+1)//2
        right.rect.centerx+=(overlap+1)//2
    if left.state=="jump" and left.rect.left<0:
        left.rect.left=right.rect.right
    if right.state=="jump" and right.rect.right>WIDTH:
        right.rect.right=left.rect.left

def keep_inside(player):
    if player.rect.right>WIDTH:
        player.rect.right=WIDTH
    elif player.rect.left<0:
        player.rect.left=0

def playGame(character1, character2):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Sound/07 - The Raising Fighting Spirit.ogg")
    pygame.mixer.music.play(-1)
    displaysurf = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    player1=Character(PLAYER1_CONTROLS, IMAGES[character1], SOUNDS[character1], PLAYER1_POSITION)
    player2=Character(PLAYER2_CONTROLS, IMAGES[character2], SOUNDS[character2], PLAYER2_POSITION)
    HUD1_IMAGES=HUD_IMAGES.copy()
    HUD1_IMAGES["icon"]=IMAGES[character1]["icon"]
    HUD2_IMAGES=HUD_IMAGES.copy()
    HUD2_IMAGES["icon"]=IMAGES[character2]["icon"]
    player1_hud=Hud(HUD1_IMAGES, LEFT_HUD_POSITION)
    player2_hud=Hud(HUD2_IMAGES, RIGHT_HUD_POSITION)
    player2_hud.flip()
    background=load_image("Background/training_background.png")
    background=pygame.transform.scale(background, (WIDTH, HEIGHT))
    player1_wins=load_image("Background/player1wins.png")
    player2_wins=load_image("Background/player2wins.png")
    pygame.display.set_caption('Pybrawl')
    game_over=False
    while True: # main game loop
        displaysurf.blit(background, (0,0))
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_RETURN and game_over:
                return

        if player1.health==0:
            game_over=True
            displaysurf.blit(player2_wins, (172, 200))

        if player2.health==0:
            game_over=True
            displaysurf.blit(player1_wins, (172, 200))

        keys_status=pygame.key.get_pressed()
        if game_over:
            keys_status=[False for i in keys_status]

        player1.update(keys_status)
        player2.update(keys_status)

        collide(player1, player2)

        keep_inside(player1)
        keep_inside(player2)

        if player1.rect.centerx < player2.rect.centerx:
            player1.direction="right"
            player2.direction="left"
        else:
            player1.direction="left"
            player2.direction="right"

        player1_hud.update(player1.health/player1.max_health,
                           player1.mana/player1.max_mana)
        player2_hud.update(player2.health/player2.max_health,
                           player2.mana/player2.max_mana)

        player1.draw(displaysurf)
        player2.draw(displaysurf)
        player1_hud.draw(displaysurf)
        player2_hud.draw(displaysurf)
        pygame.display.update()

def menu():
    # colors
    white = 255,255,255
    black =   0,  0,  0
    orange = 255,165, 0
    ###http://www.discoveryplayground.com/computer-programming-for-kids/rgb-colors/

    size = width, height = WIDTH,HEIGHT
    pygame.display.set_caption('Pybrawl')

    while True:
        screen = pygame.display.set_mode(size)
        pygame.key.set_repeat(500,30)
        background = load_image("Background/main_menu.png")
        background=pygame.transform.scale(background, (WIDTH, HEIGHT))
        screen.blit(background, (0, 0))
        pygame.display.update()

        selection = dm.dumbmenu(screen, [
                                'Start Game',
                                'Help',
                                'Quit Game'], 325,375,None,32,1.4,white,white)

        if selection == 0:
            screen.blit(background, (0, 0))
            pygame.display.update()
            pygame.key.set_repeat(500,30)
            selectionTwo = dm.dumbmenu(screen, [
                            'Naruto',
                            'Sasuke',
                            'Suigetsu',
                            'Itachi',
                            'Jiraiya',
                            'To Main Menu'], 325,375,None,32,1.4,white,white)
            characters=["naruto", "sasuke", "suigetsu", "itachi", "jiraiya"]

            if selectionTwo==-1:
                print("You choose 'Quit'")
                pygame.quit()
                exit()

            if selectionTwo==5:
                continue

            screen.blit(background, (0, 0))
            pygame.display.update()
            pygame.key.set_repeat(500,30)
            selectionThree = dm.dumbmenu(screen, [
                            'Naruto',
                            'Sasuke',
                            'Suigetsu',
                            'Itachi',
                            'Jiraiya',
                            'To Main Menu'], 325,375,None,32,1.4,white,white)
            if selectionThree==-1:
                print("You choose 'Quit'")
                pygame.quit()
                exit()

            if selectionThree==5:
                continue

            playGame(characters[selectionTwo], characters[selectionThree])

        elif selection == 1:
            print('help')
        elif selection == 2 or selection == -1:
            print("You choose 'Quit'")
            pygame.quit()
            exit()

if __name__ == "__main__":
   menu()
