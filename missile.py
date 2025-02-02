import pygame as pg
from pygame.math import Vector2
import math 

class Missile(pg.sprite.Sprite):
  def __init__(self, waypoints, image):
    pg.sprite.Sprite.__init__(self)
    self.waypoints = waypoints
    self.original_pos = self.waypoints[0]
    self.pos = Vector2(self.original_pos)
    self.target_waypoint = 1
    self.speed = 2
    self.original_image = image
    self.angle = 0
    self.image = pg.transform.rotate(self.original_image, self.angle)
    self.rect = self.image.get_rect()
    self.rect.center = self.pos
  
  def update(self):
    self.move()
    self.rotate()

  def move(self):
    if self.target_waypoint < len(self.waypoints):
      self.target = Vector2(self.waypoints[self.target_waypoint])
      self.movement = self.target - self.pos
    else: 
      self.kill()

    dist = self.movement.length()
    if dist >= self.speed:
      self.pos += self.movement.normalize()*self.speed
    else:
      if dist != 0:
        self.pos += self.movement.normalize()*dist
      self.target_waypoint+=1


  def rotate(self):
    dist = self.target - self.pos
    self.angle = math.degrees(math.atan2(-dist[1], dist[0]))
    self.image = pg.transform.rotate(self.original_image, self.angle-90)
    self.rect = self.image.get_rect()
    self.rect.center = self.pos
