import pygame
from load import load_image

class Sprite:
    def __init__(self, image, position):
        self.image=load_image(image)
        self.position=self.image.get_rect()
        self.position.topleft=position

    def get_rect(self):
        return self.position

    def flip(self, relative_rect):
        self.image=pygame.transform.flip(self.image, True, False)
        old_position=self.position
        self.position=self.image.get_rect()
        self.position.topleft=old_position.topleft

        dx=self.position.left-relative_rect.left
        self.position.right=relative_rect.right-dx

    def rotozoom(self, angle, scale):
        self.image=pygame.transform.rotozoom(self.image, angle, scale)

    def draw(self, screen):
        screen.blit(self.image, self.position)

class Bar:
    def __init__(self, image, position):
        self.image=load_image(image)
        self.position=self.image.get_rect()
        self.area=pygame.Rect(self.position)
        self.position.topleft=position
        self.flipped=False

    def get_rect(self):
        return self.position

    def flip(self, relative_rect):
        self.image=pygame.transform.flip(self.image, True, False)

        old_position=self.position
        self.position=self.image.get_rect()
        self.area=pygame.Rect(self.position)
        self.position.topleft=old_position.topleft

        dx=self.position.left-relative_rect.left
        self.position.right=relative_rect.right-dx

        self.flipped=not self.flipped

    def update(self, fraction):
        self.area.width=self.position.width*fraction

        if self.flipped:
            self.area.left=self.position.width-self.area.width

    def draw(self, screen):
        dest=pygame.Rect(self.position)
        if self.flipped:
            dest.left+=self.area.left
        screen.blit(self.image, dest, self.area)


class Hud:

    POSITIONS={"frame": (0, 0),
               "health": (62, 29),
               "mana": (70, 51),
               "icon": (-10, 10)}

    def __init__(self, images, position):
        self.frame=Sprite(images["frame"],
                         (position[0] + self.POSITIONS["frame"][0],
                          position[1] + self.POSITIONS["frame"][1]))
        self.health=Bar(images["health"],
                        (position[0] + self.POSITIONS["health"][0],
                         position[1] + self.POSITIONS["health"][1]))
        self.mana=Bar(images["mana"],
                      (position[0] + self.POSITIONS["mana"][0],
                       position[1] + self.POSITIONS["mana"][1]))
        self.icon=Sprite(images["icon"],
                       (position[0] + self.POSITIONS["icon"][0],
                        position[1] + self.POSITIONS["icon"][1]))
        self.icon.rotozoom(10, 0.7)

    def flip(self):
        bounding_rect=self.get_rect()
        self.frame.flip(bounding_rect)
        self.health.flip(bounding_rect)
        self.mana.flip(bounding_rect)
        self.icon.flip(bounding_rect)

    def get_rect(self):
        left=min(self.frame.get_rect().left,
                 self.health.get_rect().left,
                 self.mana.get_rect().left,
                 self.icon.get_rect().left)
        right=max(self.frame.get_rect().right,
                  self.health.get_rect().right,
                  self.mana.get_rect().right,
                  self.icon.get_rect().right)
        top=min(self.frame.get_rect().top,
                self.health.get_rect().top,
                self.mana.get_rect().top,
                self.icon.get_rect().top)
        bottom=max(self.frame.get_rect().bottom,
                   self.health.get_rect().bottom,
                   self.mana.get_rect().bottom,
                   self.icon.get_rect().bottom)
        return pygame.Rect(left, top, right-left, bottom-top)

    def update(self, health_fraction, mana_fraction):
        self.health.update(health_fraction)
        self.mana.update(mana_fraction)

    def draw(self, screen):
        self.frame.draw(screen)
        self.health.draw(screen)
        self.mana.draw(screen)
        self.icon.draw(screen)
