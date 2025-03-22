import pygame, controls
from gan import Gun #забираем оттуда с папки gan код
from pygame.sprite import Group
from stats import Stats
from scores import Scores





def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 650))
    pygame.display.set_caption("Космические защитники")
    bg_color = (0, 0, 0)
    gan = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)



    while True:
        controls.events(screen, gan, bullets)
        if stats.run_game:
            gan.update_gan()
            controls.update(bg_color, screen, stats, sc, gan, inos, bullets)
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, sc,  gan, inos, bullets)

run()
