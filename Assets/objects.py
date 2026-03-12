from .imports import Number, termgame, math
class Wall:
    def __init__(self,points: termgame.Rect):
        self.points = points
        self.rect = points

    def draw(self, screen):
        termgame.draw.rect(screen, termgame.Color("grey"), (self.rect.x, self.rect.y, self.rect.width, self.rect.height))
