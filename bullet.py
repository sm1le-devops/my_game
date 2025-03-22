import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gan):

        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 20)

        self.color = 139, 195, 74
        self.speed = 9
        self.rect.centerx = gan.rect.centerx
        self.rect.top = gan.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):

        pygame.draw.rect(self.screen, self.color, self.rect)





