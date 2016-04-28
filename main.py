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

IMAGES = {
    "naruto": {"stance": ["Naruto/new_sprites/stance0.png",
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
                 "throw": ["Naruto/new_sprites/throw0.png",
                           "Naruto/new_sprites/throw1.png",
                           "Naruto/new_sprites/throw2.png",
                           "Naruto/new_sprites/throw3.png",
                           "Naruto/new_sprites/throw4.png"],
                 "special": ["Naruto/new_sprites/special0.png",
                             "Naruto/new_sprites/special1.png",
                             "Naruto/new_sprites/special2.png",
                             "Naruto/new_sprites/special3.png",
                             "Naruto/new_sprites/special4.png",
                             "Naruto/new_sprites/special5.png",
                             "Naruto/new_sprites/special6.png",
                             "Naruto/new_sprites/special7.png",
                             "Naruto/new_sprites/special8.png",
                             "Naruto/new_sprites/special9.png"],
                 "block": ["Naruto/new_sprites/block0.png"],
                 "throw_projectile": [["Naruto/new_sprites/rasengan0.png",
                                       "Naruto/new_sprites/rasengan1.png",
                                       "Naruto/new_sprites/rasengan2.png",
                                       "Naruto/new_sprites/rasengan3.png",
                                       "Naruto/new_sprites/rasengan4.png",
                                       "Naruto/new_sprites/rasengan5.png"],
                                      (4, 5)],
                 "special_projectile": [["Naruto/new_sprites/kyuubi0.png",
                                         "Naruto/new_sprites/kyuubi1.png",
                                         "Naruto/new_sprites/kyuubi2.png",
                                         # "Naruto/new_sprites/kyuubi3.png",
                                         # "Naruto/new_sprites/kyuubi4.png",
                                         "Naruto/new_sprites/kyuubi5.png"],
                                        (3, 3)],
                 "icon": "Hud/naruto_icon.png"},

    "sasuke": {"stance": ["Sasuke/new_sprites/stance0.gif",
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
                 "throw": ["Sasuke/new_sprites/throw0.png",
                           "Sasuke/new_sprites/throw1.png",
                           "Sasuke/new_sprites/throw2.png",
                           "Sasuke/new_sprites/throw3.png"],
                 "special": ["Sasuke/new_sprites/special0.png",
                             "Sasuke/new_sprites/special1.png",
                             "Sasuke/new_sprites/special2.png",
                             "Sasuke/new_sprites/special3.png",
                             "Sasuke/new_sprites/special4.png",
                             "Sasuke/new_sprites/special5.png"],
                 "block": ["Sasuke/new_sprites/block0.png"],
                 "throw_projectile": [["Sasuke/new_sprites/lightning0.png",
                                       "Sasuke/new_sprites/lightning1.png",
                                       "Sasuke/new_sprites/lightning2.png",
                                       "Sasuke/new_sprites/lightning3.png",
                                       "Sasuke/new_sprites/lightning4.png",
                                       "Sasuke/new_sprites/lightning5.png"],
                                      (4, 5)],
                 "special_projectile": [["Sasuke/new_sprites/katon0.png",
                                         "Sasuke/new_sprites/katon1.png",
                                         "Sasuke/new_sprites/katon2.png",
                                         "Sasuke/new_sprites/katon3.png",
                                         "Sasuke/new_sprites/katon4.png",
                                         "Sasuke/new_sprites/katon5.png"],
                                        (3, 5)],
                 "icon": "Hud/sasuke_icon.png"}
}

HUD_IMAGES = {"frame": "Hud/frame.png",
              "health": "Hud/health.png",
              "mana": "Hud/mana.png"}

LEFT_HUD_POSITION = (5, 0)
RIGHT_HUD_POSITION = (WIDTH-230, 0)

PLAYER1_CONTROLS = {"left": K_a,
                    "right": K_d,
                    "jump": K_w,
                    "attack": K_t,
                    "throw": K_y,
                    "special": K_u}

PLAYER2_CONTROLS = {"left": K_LEFT,
                    "right": K_RIGHT,
                    "jump": K_UP,
                    "attack": K_KP4,
                    "throw": K_KP5,
                    "special": K_KP6}

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
    if right.state=="jump" and right.rect.right>800:
        right.rect.right=left.rect.left

def keep_inside(player):
    if player.rect.right>800:
        player.rect.right=800
    elif player.rect.left<0:
        player.rect.left=0

def playGame(character1, character2):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Sound/07 - The Raising Fighting Spirit.ogg")
    pygame.mixer.music.play(-1)
    displaysurf = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    player1=Character(PLAYER1_CONTROLS, IMAGES[character1], (5, 545))
    player2=Character(PLAYER2_CONTROLS, IMAGES[character2], (740,545))
    HUD1_IMAGES=HUD_IMAGES.copy()
    HUD1_IMAGES["icon"]=IMAGES[character1]["icon"]
    HUD2_IMAGES=HUD_IMAGES.copy()
    HUD2_IMAGES["icon"]=IMAGES[character2]["icon"]
    player1_hud=Hud(HUD1_IMAGES, LEFT_HUD_POSITION)
    player2_hud=Hud(HUD2_IMAGES, RIGHT_HUD_POSITION)
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
    playGame("naruto", "sasuke")
