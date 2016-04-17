import pygame
from pygame.locals import *
from load import load_image

class Character:
    def __init__(self, controls, images, position):
        self.stance=images["stance"]
        self.runright=images["runright"]
        self.runleft=images["runleft"]
        self.jump=images["jump"]
        self.attack=images["attack"]
        self.ani_stance=Animation(self.stance, 10)
        self.ani_runright=Animation(self.runright, 7)
        self.ani_runleft=Animation(self.runleft, 7)
        self.ani_jump=Animation(self.jump, 13)
        self.ani_attack=Animation(self.attack, 7)
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
        if (self.state!="jump" and self.state!="attack") or (self.ani_jump.done or self.ani_attack.done):
            self.ani_jump.reset()
            self.ani_attack.reset()
            if keys_status[self.controls["jump"]]:
                self.state="jump"
            elif keys_status[self.controls["right"]] and keys_status[self.controls["left"]]:
                self.state="stance"
            elif keys_status[self.controls["attack"]]:
                self.state="attack"
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

        self.old_rect=self.rect
        self.rect=self.img.get_rect()
        self.rect.topleft=self.old_rect.topleft

        if self.direction=="left" and not self.state in ["runright", "runleft"]:
            self.img=pygame.transform.flip(self.img, True, False)
        

    def draw(self, screen):
        self.adjust_height(screen)
        screen.blit(self.img, self.rect.topleft)

    def adjust_height(self, screen):
        if self.state!="jump":
            self.rect.bottom=screen.get_height()
            
                
class Animation:
    def __init__(self, pictures, speed):
        self.ani_speed_init=speed
        self.ani_speed=self.ani_speed_init
        self.ani=[load_image(picture) for picture in pictures]
        self.ani_pos=0
        self.ani_max=len(self.ani)-1
        self.img=self.ani[0]
        self.done=False
        
    def update(self):
        self.ani_speed-=1
        if self.ani_speed==0:
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
        
