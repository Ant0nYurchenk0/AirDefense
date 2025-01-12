import pygame as pg
from pygame.math import Vector2
import math 

class Projectile(pg.sprite.Sprite):
  def __init__(self, pos, target, base, image):
    pg.sprite.Sprite.__init__(self)
    self.target = target
    self.pos = pos
    self.base=base
    self.waypoints = []
    self.speed = 3
    self.original_image = image
    self.angle = 0
    self.image = pg.transform.rotate(self.original_image, self.angle)
    self.rect = self.image.get_rect()
    self.rect.center = self.pos
  
  def update(self):
    self.move()
    self.rotate()

  def move(self):
    if not self.target:
      self.kill()

    self.movement = self.target.pos - self.pos
    
    dist_to_base = (Vector2(self.pos) - Vector2(self.base.pos)).length()
    if dist_to_base >= self.base.range:
      self.kill()

    dist_to_target = self.movement.length()
    if dist_to_target >= self.speed:
      self.pos += self.movement.normalize()*self.speed
      self.waypoints.append((self.pos[0], self.pos[1]))

    else:
      self.pos += self.movement.normalize()*dist_to_target
      self.target.kill()
      self.kill()


  def draw(self, surface):
    if len(self.waypoints) >= 2:
      pg.draw.lines(surface, "orange", False, self.waypoints)
    surface.blit(self.image, self.rect)

  def rotate(self):
    dist = self.target.pos - self.pos
    self.angle = math.degrees(math.atan2(-dist[1], dist[0]))
    self.image = pg.transform.rotate(self.original_image, self.angle-90)
    self.rect = self.image.get_rect()
    self.rect.center = self.pos
