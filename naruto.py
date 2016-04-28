import pygame
from pygame.locals import *
from load import load_image

class Character:

    THROW_MANA=300
    SPECIAL_MANA=500

    def __init__(self, controls, images, position):
        self.stance=images["stance"]
        self.runright=images["runright"]
        self.runleft=images["runleft"]
        self.jump=images["jump"]
        self.attack=images["attack"]
        self.takedamage=images["takedamage"]
        self.throw=images["throw"]
        self.special=images["special"]
        self.block=images["block"]
        self.projectile_images={"throw": images["throw_projectile"],
                                "special": images["special_projectile"]}
        self.projectiles=[]
        self.ani_stance=Animation(self.stance, 10)
        self.ani_runright=Animation(self.runright, 7)
        self.ani_runleft=Animation(self.runleft, 7)
        self.ani_jump=Animation(self.jump, 13)
        self.ani_attack=Animation(self.attack, 7)
        self.ani_takedamage=Animation(self.takedamage, 10)
        self.ani_throw=Animation(self.throw, 7)
        self.ani_special=Animation(self.special, 7)
        self.ani_block=Animation(self.block, 10)
        self.state="stance"
        self.img=self.ani_stance.img
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
        self.replenish_mana()
        self.update_projectiles()

        if ((self.state!="jump" and self.state!="attack" and self.state!="takedamage" and
             self.state!="throw" and self.state!="special" and self.state!="block") or
            (self.ani_jump.done or self.ani_attack.done or self.ani_takedamage.done or
             self.ani_throw.done or self.ani_special.done or self.ani_block.done)):
            if self.state=="throw":
                if self.direction=="left":
                    self.projectiles.append(Projectile(self.rect.midleft,
                                                       (-7, 0),
                                                       100,
                                                       *self.projectile_images["throw"]))
                elif self.direction=="right":
                    self.projectiles.append(Projectile(self.rect.midright,
                                                       (+7, 0),
                                                       100,
                                                       *self.projectile_images["throw"]))
            elif self.state=="special":
                if self.direction=="left":
                    self.projectiles.append(Projectile(self.rect.midleft,
                                                       (-7, 0),
                                                       200,
                                                       *self.projectile_images["special"]))
                elif self.direction=="right":
                    self.projectiles.append(Projectile(self.rect.midright,
                                                       (+7, 0),
                                                       200,
                                                       *self.projectile_images["special"]))

            self.ani_jump.reset()
            self.ani_attack.reset()
            self.ani_takedamage.reset()
            self.ani_throw.reset()
            self.ani_special.reset()
            self.ani_block.reset()
            if keys_status[self.controls["jump"]]:
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

        if self.state=="runright":
            self.rect.x+=3
        elif self.state=="runleft":
            self.rect.x-=3
        elif self.state=="jump":
            if self.ani_jump.ani_pos < self.ani_jump.ani_max / 2:
                self.rect.y-=5
            else:
                self.rect.y+=5
            if keys_status[self.controls["right"]]:
                self.rect.x+=3
            elif keys_status[self.controls["left"]]:
                self.rect.x-=3
        elif self.state=="attack":
            if self.direction=="left":
                self.rect.x-=1
            elif self.direction=="right":
                self.rect.x+=1
        elif self.state=="takedamage" and self.state=="block":
            if self.direction=="left":
                self.rect.x+=1
            elif self.direction=="right":
                self.rect.x-=1

        if self.state=="stance":
            self.ani_stance.update()
            self.img=self.ani_stance.img
        elif self.state=="attack":
            self.ani_attack.update()
            self.img=self.ani_attack.img
        elif self.state=="runright":
            self.ani_runright.update()
            self.img=self.ani_runright.img
        elif self.state=="runleft":
            self.ani_runleft.update()
            self.img=self.ani_runleft.img
        elif self.state=="jump":
            self.ani_jump.update()
            self.img=self.ani_jump.img
        elif self.state=="takedamage":
            self.ani_takedamage.update()
            self.img=self.ani_takedamage.img
        elif self.state=="throw":
            self.ani_throw.update()
            self.img=self.ani_throw.img
        elif self.state=="special":
            self.ani_special.update()
            self.img=self.ani_special.img
        elif self.state=="block":
            self.ani_block.update()
            self.img=self.ani_block.img

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
        if self.state!="takedamage" and self.state!="block":
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
            if projectile.is_on_screen(800, 600):
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
