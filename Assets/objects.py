from .imports import Number, pygame, math
class Wall:
    def __init__(self,points: pygame.Rect):
        self.points = points
        self.rect = points

    def draw(self, screen):
        pygame.draw.rect(screen, pygame.Color("grey"), (self.rect.x, self.rect.y, self.rect.width, self.rect.height))