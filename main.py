import pygame, sys
from pygame.locals import *
from naruto import Character
from hud import Hud
from load import load_image

           #R    G    B
BLUE =     (0,   0,   255)
GREEN =    (0,   128, 0)
PURPLE =   (128, 0,   128)
RED =      (255, 0,   0)
YELLOW =   (255, 255, 0)
NAVYBLUE = (0,   0,   128)
WHITE =    (255, 255, 255)
BLACK =    (0,   0,   0)

WIDTH=800
HEIGHT=600
FPS=60

NARUTO_IMAGES = {"stance": ["Naruto/new_sprites/stance0.png",
                            "Naruto/new_sprites/stance1.png",
                            "Naruto/new_sprites/stance2.png",
                            "Naruto/new_sprites/stance3.png"],
                 "runright": ["Naruto/new_sprites/move_right0.png",
                              "Naruto/new_sprites/move_right1.png",
                              "Naruto/new_sprites/move_right2.png",
                              "Naruto/new_sprites/move_right3.png",
                              "Naruto/new_sprites/move_right4.png",
                              "Naruto/new_sprites/move_right5.png"],
                 "runleft": ["Naruto/new_sprites/move_left0.png",
                             "Naruto/new_sprites/move_left1.png",
                             "Naruto/new_sprites/move_left2.png",
                             "Naruto/new_sprites/move_left3.png",
                             "Naruto/new_sprites/move_left4.png",
                             "Naruto/new_sprites/move_left5.png"],
                 "jump": ["Naruto/new_sprites/jump0.png",
                          "Naruto/new_sprites/jump1.png",
                          "Naruto/new_sprites/jump2.png",
                          "Naruto/new_sprites/jump4.png",
                          "Naruto/new_sprites/jump5.png",
                          "Naruto/new_sprites/jump6.png"],
                 "attack": ["Naruto/new_sprites/normal_attack0.png",
                            "Naruto/new_sprites/normal_attack1.png",
                            "Naruto/new_sprites/normal_attack2.png"],
                 "takedamage": ["Naruto/new_sprites/take_damage0.png",
                                "Naruto/new_sprites/take_damage1.png"],
                 "icon": "Hud/naruto_icon.png"}

SASUKE_IMAGES = {"stance": ["Sasuke/new_sprites/stance0.gif",
                            "Sasuke/new_sprites/stance1.gif",
                            "Sasuke/new_sprites/stance2.gif",
                            "Sasuke/new_sprites/stance3.gif",
                            "Sasuke/new_sprites/stance4.gif",
                            "Sasuke/new_sprites/stance5.gif"],
                 "runright": ["Sasuke/new_sprites/move_right0.gif",
                              "Sasuke/new_sprites/move_right1.gif",
                              "Sasuke/new_sprites/move_right2.gif",
                              "Sasuke/new_sprites/move_right3.gif",
                              "Sasuke/new_sprites/move_right4.gif",
                              "Sasuke/new_sprites/move_right5.gif"],
                 "runleft": ["Sasuke/new_sprites/move_left0.gif",
                             "Sasuke/new_sprites/move_left1.gif",
                             "Sasuke/new_sprites/move_left2.gif",
                             "Sasuke/new_sprites/move_left3.gif",
                             "Sasuke/new_sprites/move_left4.gif",
                             "Sasuke/new_sprites/move_left5.gif"],
                 "jump": ["Sasuke/new_sprites/jump0.gif",
                          "Sasuke/new_sprites/jump1.gif",
                          "Sasuke/new_sprites/jump2.gif",
                          "Sasuke/new_sprites/jump4.gif",
                          "Sasuke/new_sprites/jump5.gif",
                          "Sasuke/new_sprites/jump6.gif"],
                 "attack": ["Sasuke/new_sprites/normal_attack0.png",
                            "Sasuke/new_sprites/normal_attack1.png",
                            "Sasuke/new_sprites/normal_attack2.png",
                            "Sasuke/new_sprites/normal_attack3.png"],
                 "takedamage": ["Sasuke/new_sprites/take_damage0.png",
                                "Sasuke/new_sprites/take_damage1.png",
                                "Sasuke/new_sprites/take_damage2.png"],
                 "icon": "Hud/sasuke_icon.png"}

HUD_IMAGES = {"frame": "Hud/frame.png",
              "health": "Hud/health.png",
              "mana": "Hud/mana.png"}

LEFT_HUD_POSITION = (5, 0)
RIGHT_HUD_POSITION = (WIDTH-230, 0)

PLAYER1_CONTROLS = {"left": K_a,
                    "right": K_d,
                    "jump": K_w,
                    "attack": K_t}

PLAYER2_CONTROLS = {"left": K_LEFT,
                    "right": K_RIGHT,
                    "jump": K_UP,
                    "attack": K_KP4}

def collide(left, right):
    if not left.rect.colliderect(right.rect):
        return
    #deal damage
    if left.state=="attack":
        right.take_damage(left.damage)
    if right.state=="attack":
        left.take_damage(right.damage)
    #adjust position
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
    if right.state=="jump" and right.rect.right>800:
        right.rect.right=left.rect.left

def keep_inside(player):
    if player.rect.right>800:
        player.rect.right=800
    elif player.rect.left<0:
        player.rect.left=0

def playGame():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Sound/07 - The Raising Fighting Spirit.ogg")
    pygame.mixer.music.play(-1)
    displaysurf = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    player1=Character(PLAYER1_CONTROLS, NARUTO_IMAGES, (5, 545))
    player2=Character(PLAYER2_CONTROLS, SASUKE_IMAGES, (740,545))
    player1_hud=Hud({**HUD_IMAGES, "icon": NARUTO_IMAGES["icon"]},
                    LEFT_HUD_POSITION)
    player2_hud=Hud({**HUD_IMAGES, "icon": SASUKE_IMAGES["icon"]},
                    RIGHT_HUD_POSITION)
    player2_hud.flip()
    background=load_image("Background/training_background.png")
    background=pygame.transform.scale(background, (WIDTH, HEIGHT))
    pygame.display.set_caption('Pygame')
    while True: # main game loop
        displaysurf.blit(background, (0,0))
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        player1.update(pygame.key.get_pressed())
        player2.update(pygame.key.get_pressed())

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

if __name__ == "__main__":
    playGame()
