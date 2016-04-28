from pygame.locals import *

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
                 "icon": "Hud/sasuke_icon.png"},

    "suigetsu": {"introduction": ["Suigetsu/introduction0.png",
                                    "Suigetsu/introduction1.png",
                                    "Suigetsu/introduction2.png",
                                    "Suigetsu/introduction3.png",
                                    "Suigetsu/introduction4.png",
                                    "Suigetsu/introduction5.png"],
                   "stance": ["Suigetsu/stance0.png",
                              "Suigetsu/stance1.png",
                              "Suigetsu/stance2.png",
                              "Suigetsu/stance3.png"],
                   "runright": ["Suigetsu/move_right0.png",
                                "Suigetsu/move_right1.png",
                                "Suigetsu/move_right2.png",
                                "Suigetsu/move_right3.png",
                                "Suigetsu/move_right4.png",
                                "Suigetsu/move_right5.png"],
                   "runleft": ["Suigetsu/move_left0.png",
                               "Suigetsu/move_left1.png",
                               "Suigetsu/move_left2.png",
                               "Suigetsu/move_left3.png",
                               "Suigetsu/move_left4.png",
                               "Suigetsu/move_left5.png"],
                   "jump": ["Suigetsu/jump0.png",
                            "Suigetsu/jump1.png",
                            "Suigetsu/jump2.png",
                            "Suigetsu/jump4.png",
                            "Suigetsu/jump5.png",
                            "Suigetsu/jump6.png"],
                   "attack": ["Suigetsu/normal_attack0.png",
                              "Suigetsu/normal_attack1.png",
                              "Suigetsu/normal_attack2.png",
                              "Suigetsu/normal_attack3.png",
                              "Suigetsu/normal_attack4.png"],
                   "takedamage": ["Suigetsu/take_damage0.png",
                                  "Suigetsu/take_damage1.png",
                                  "Suigetsu/take_damage2.png"],
                   "throw": ["Suigetsu/throw0.png",
                             "Suigetsu/throw1.png",
                             "Suigetsu/throw2.png",
                             "Suigetsu/throw3.png",
                             "Suigetsu/throw4.png"],
                   "special": ["Suigetsu/special0.png",
                               "Suigetsu/special1.png",
                               "Suigetsu/special2.png",
                               "Suigetsu/special3.png",
                               "Suigetsu/special4.png"],
                   "block": ["Suigetsu/block0.png"],
                   "throw_projectile": [["Suigetsu/note0.png",
                                         "Suigetsu/note1.png",
                                         "Suigetsu/note2.png",
                                         "Suigetsu/note3.png"],
                                        (2, 3)],
                   "special_projectile": [["Suigetsu/sword0.png",
                                           "Suigetsu/sword1.png",
                                           "Suigetsu/sword2.png",
                                           "Suigetsu/sword3.png"],
                                          (0, 3)],
                   "icon": "Hud/suigetsu_icon.png"}
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

PLAYER1_POSITION = (5, 545)
PLAYER2_POSITION = (740,545)