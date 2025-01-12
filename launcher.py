import pygame as pg
import math
from projectile import Projectile

class Launcher(pg.sprite.Sprite):
  def __init__(self, image, pos):
    pg.sprite.Sprite.__init__(self)
    self.image = image
    self.pos = pos
    self.rect = self.image.get_rect()
    self.range = 120
    self.cooldown = 1500
    self.rect.center = self.pos
    self.target = None
    self.last_shot = pg.time.get_ticks()

    self.range_image = pg.Surface((self.range*2, self.range*2))
    self.range_image.fill((0,0,0,))
    self.range_image.set_colorkey((0,0,0))
    pg.draw.circle(self.range_image, "white", (self.range, self.range), self.range)
    self.range_image.set_alpha(100)

    self.range_rect = self.range_image.get_rect()
    self.range_rect.center = self.rect.center


  def update(self, missile_group, projectile_group, projectile_image):
    if pg.time.get_ticks() - self.last_shot > self.cooldown:
      if self.target:
        self.shoot(projectile_group, projectile_image)
      else:
        self.pick_target(missile_group)

  def shoot(self, projectile_group, projectile_image):
    projectile = Projectile(self.pos, self.target, self, projectile_image)
    projectile_group.add(projectile)
    self.last_shot = pg.time.get_ticks()
    self.target = None

  def pick_target(self, missile_group):
    x_dist = 0
    y_dist = 0

    for missile in missile_group:
      x_dist = missile.pos[0] - self.pos[0]
      y_dist = missile.pos[1] - self.pos[1]
      dist = math.sqrt(x_dist**2 +y_dist**2)
      if dist < self.range:
        self.target = missile

  def draw(self, surface):
    surface.blit(self.range_image, self.range_rect)
    surface.blit(self.image, self.rect)