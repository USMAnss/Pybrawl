import pygame
from pygame.locals import *
from load import *
from settings import *

class Character:

    THROW_MANA=300
    SPECIAL_MANA=500

    def __init__(self, controls, images, sounds, position):
        self.projectile_images={"throw": images["throw_projectile"],
                                "special": images["special_projectile"]}
        self.projectiles=[]
        self.animations={
            "stance": Animation(images["stance"], 10),
            "runright": Animation(images["runright"], 7),
            "runleft": Animation(images["runleft"], 7),
            "jump": Animation(images["jump"], 10),
            "attack": Animation(images["attack"], 7),
            "takedamage": Animation(images["takedamage"], 10),
            "throw": Animation(images["throw"], 7),
            "special": Animation(images["special"], 7),
            "block": Animation(images["block"], 10),
            "introduction": Animation(images["introduction"], 10),
            "death": Animation(images["death"], 10, (len(images["death"]) - 1,
                                                     len(images["death"]) - 1))
        }
        self.sounds={key: load_sound(value) for key, value in sounds.items()}
        self.state="introduction"
        self.img=self.animations["stance"].img
        self.rect=self.img.get_rect()
        self.rect.topleft=position
        self.direction="right"
        self.controls=controls
        self.health=1000
        self.max_health=1000
        self.mana=1000
        self.max_mana=1000
        self.damage=100

    def update(self, keys_status):
        self.update_projectiles()

        if self.state!="death":
            self.replenish_mana()
            self.update_state(keys_status)
            self.update_position(keys_status)

        self.update_animation()
        self.update_image_direction()

    def update_state(self, keys_status):
        if (self.state not in ["jump", "attack", "takedamage", "throw", "special", "block", "introduction"] or
            self.animations[self.state].done):
            if self.state=="throw":
                if self.direction=="left":
                    self.projectiles.append(Projectile(self.rect.midleft,
                                                       (-10, 0),
                                                       100,
                                                       *self.projectile_images["throw"]))
                elif self.direction=="right":
                    self.projectiles.append(Projectile(self.rect.midright,
                                                       (+10, 0),
                                                       100,
                                                       *self.projectile_images["throw"]))
            elif self.state=="special":
                if self.direction=="left":
                    self.projectiles.append(Projectile(self.rect.midleft,
                                                       (-9, 0),
                                                       200,
                                                       *self.projectile_images["special"]))
                elif self.direction=="right":
                    self.projectiles.append(Projectile(self.rect.midright,
                                                       (+9, 0),
                                                       200,
                                                       *self.projectile_images["special"]))

            if self.state in ["jump", "attack", "takedamage", "throw", "special", "block", "introduction"]:
                self.animations[self.state].reset()

            if self.state=="takedamage" and self.health==0:
                self.state="death"
            elif keys_status[self.controls["jump"]]:
                self.state="jump"
            elif keys_status[self.controls["special"]] and self.mana>=self.SPECIAL_MANA:
                self.state="special"
                self.mana-=self.SPECIAL_MANA
            elif keys_status[self.controls["attack"]]:
                self.state="attack"
            elif keys_status[self.controls["throw"]] and self.mana>=self.THROW_MANA:
                self.state="throw"
                self.mana-=self.THROW_MANA
            elif keys_status[self.controls["right"]] and keys_status[self.controls["left"]]:
                self.state="stance"
            elif keys_status[self.controls["right"]]:
                self.state="runright"
            elif keys_status[self.controls["left"]]:
                self.state="runleft"
            else:
                self.state="stance"

            if self.state in self.sounds:
                self.sounds[self.state].play()

    def update_position(self, keys_status):
        if self.state=="runright":
            self.rect.x+=4
        elif self.state=="runleft":
            self.rect.x-=4
        elif self.state=="jump":
            if self.animations["jump"].ani_pos < self.animations["jump"].ani_max / 2:
                self.rect.y-=7
            else:
                self.rect.y+=7
            if keys_status[self.controls["right"]]:
                self.rect.x+=4
            elif keys_status[self.controls["left"]]:
                self.rect.x-=4
        elif self.state=="attack":
            if self.direction=="left":
                self.rect.x-=2
            elif self.direction=="right":
                self.rect.x+=2
        elif self.state=="takedamage" and self.state=="block":
            if self.direction=="left":
                self.rect.x+=1
            elif self.direction=="right":
                self.rect.x-=1

    def update_animation(self):
        self.animations[self.state].update()
        self.img=self.animations[self.state].img

    def update_image_direction(self):
        self.old_rect=self.rect
        self.rect=self.img.get_rect()
        self.rect.topleft=self.old_rect.topleft

        if self.direction=="left" and not self.state in ["runright", "runleft"]:
            self.img=pygame.transform.flip(self.img, True, False)

    def draw(self, screen):
        self.adjust_height(screen)
        screen.blit(self.img, self.rect.topleft)

        for projectile in self.projectiles:
            projectile.draw(screen)

    def adjust_height(self, screen):
        if self.state!="jump":
            self.rect.bottom=screen.get_height()

    def take_damage(self, damage):
        if self.state not in ["death", "takedamage", "block"]:
            if (self.direction=="left" and self.state=="runright" or
                self.direction=="right" and self.state=="runleft"):
                self.state="block"
            else:
                self.health=max(0, self.health-damage)
                self.state="takedamage"

    def replenish_mana(self):
        self.mana=min(self.max_mana, self.mana+1)

    def update_projectiles(self):
        new_projectiles=[]
        for projectile in self.projectiles:
            if projectile.is_on_screen(WIDTH, HEIGHT):
                projectile.update()
                new_projectiles.append(projectile)
        self.projectiles=new_projectiles



class Animation:
    def __init__(self, pictures, speed, loop=None):
        self.ani_speed_init=speed
        self.ani_speed=self.ani_speed_init
        self.ani=[load_image(picture) for picture in pictures]
        self.ani_pos=0
        self.ani_max=len(self.ani)-1
        self.img=self.ani[0]
        self.loop=loop if loop is not None else (0, self.ani_max)
        self.done=False

    def update(self):
        # if not self.done:
        self.ani_speed-=1
        if self.ani_speed==0:
            if self.ani_pos==self.loop[1]:
                self.ani_pos=self.loop[0]
            else:
                self.ani_pos=(self.ani_pos+1)%len(self.ani)
            if self.ani_pos==0:
                self.done=True
            self.img=self.ani[self.ani_pos]
            self.ani_speed=self.ani_speed_init

    def reset(self):
        self.ani_speed=self.ani_speed_init
        self.ani_pos=0
        self.img=self.ani[0]
        self.done=False

    def stop(self):
        self.done=True

class Projectile:
    def __init__(self, position, velocity, damage, images, loop):
        self.ani=Animation(images, 7, loop)
        self.rect=self.ani.img.get_rect()
        self.rect.center=position
        self.velocity=velocity
        self.damage=damage

    def draw(self, screen):
        if self.velocity[0] < 0:
            screen.blit(pygame.transform.flip(self.ani.img, True, False), self.rect)
        else:
            screen.blit(self.ani.img, self.rect)

    def update(self):
        self.rect.x+=self.velocity[0]
        self.rect.y+=self.velocity[1]

        old_rect=self.rect
        self.ani.update()
        self.rect=self.ani.img.get_rect()
        self.rect.center=old_rect.center

    def is_on_screen(self, screen_width, screen_height):
        return (self.rect.left < screen_width and
                self.rect.right > 0 and
                self.rect.bottom > 0 and
                self.rect.top < screen_height)
