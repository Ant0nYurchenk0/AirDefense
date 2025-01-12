import pygame as pg


class Factory(pg.sprite.Sprite):
  def __init__(self, pos, image):
    pg.sprite.Sprite.__init__(self)
    self.pos = pos
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.center = self.pos