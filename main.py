import pygame as pg
import constants as c
from missile import Missile 
from factory import Factory
from launcher import Launcher

if __name__=="__main__":

  pg.init()

  clock = pg.time.Clock()


  screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
  pg.display.set_caption("AirDefense")

  factory_image = pg.image.load('assets/images/entities/factory.png')
  factory_image = pg.transform.scale(factory_image, c.DEFAULT_ENTITY_IMAGE_SIZE)
  factory_group = pg.sprite.Group()

  factory = Factory((500, 500), factory_image)
  factory_group.add(factory)

  missile_image = pg.image.load('assets/images/entities/missile.png').convert_alpha()
  missile_image = pg.transform.scale(missile_image, c.DEFAULT_ENTITY_IMAGE_SIZE)
  missile_group = pg.sprite.Group()
  
  launcher_image = pg.image.load('assets/images/entities/launcher.png').convert_alpha()
  launcher_image = pg.transform.scale(launcher_image, c.DEFAULT_ENTITY_IMAGE_SIZE)
  launcher_group = pg.sprite.Group()
  
  projectile_image = pg.image.load('assets/images/entities/projectile.png').convert_alpha()
  projectile_image = pg.transform.scale(projectile_image, c.DEFAULT_ENTITY_IMAGE_SIZE)
  projectile_group = pg.sprite.Group()
  

  run = True
  while run:
    clock.tick(c.FPS)
    screen.fill((0,0,0))
    
    for missile in missile_group:
      pg.draw.lines(screen, "white", False, [missile.pos, missile.original_pos])
    
    missile_group.update()
    missile_group.draw(screen)

    factory_group.update()
    factory_group.draw(screen)

    projectile_group.update()
    for projectile in projectile_group:
      projectile.draw(screen)

    launcher_group.update(missile_group, projectile_group, projectile_image)
    for launcher in launcher_group:
      launcher.draw(screen)


    for event in pg.event.get():
      if event.type == pg.QUIT: 
        run = False

      if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
        pos = pg.mouse.get_pos()
        missile = Missile([pos, factory.pos], missile_image)
        missile_group.add(missile)

      if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
        pos = pg.mouse.get_pos()
        if pos[0] < c.SCREEN_WIDTH and pos[1] < c.SCREEN_HEIGHT:
          launcher = Launcher(launcher_image, pos)
          launcher_group.add(launcher)

    pg.display.update()

  pg.quit()
