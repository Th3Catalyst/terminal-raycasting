from termgame.key import ScancodeWrapper

from .imports import Number, termgame, math, combineTuple, castRay, Iterable
class Player:
    def __init__(self, pos: tuple[Number,Number], angle: Number, pitch: Number = 0) -> None:
        self.pos = pos
        self.angle = angle
        self.pitch = pitch

    def draw(self, screen) -> None:
        frontPoint = (self.pos[0] + 20*math.cos(self.angle), self.pos[1] + 20*math.sin(self.angle))
        leftPoint = (self.pos[0] + 5*math.cos(self.angle + 2*math.pi/3), self.pos[1] + 5*math.sin(self.angle + 2*math.pi/3))
        rightPoint = (self.pos[0] + 5*math.cos(self.angle - 2*math.pi/3), self.pos[1] + 5*math.sin(self.angle - 2*math.pi/3))
        termgame.draw.polygon(screen, "yellow", (frontPoint, leftPoint, rightPoint))

    def rayCast(self, screen: termgame.Surface, fov: int, collisionObjects: Iterable[termgame.Rect]) -> None:
        fovRad = fov/180*math.pi
        detail = 3
        for i in range(math.floor(detail*(fov+1))):
            endPoint = castRay(screen, self.pos, self.angle-fovRad/2+i/(180*detail)*math.pi, collisionObjects)
            if endPoint[1] == 0: endPoint = (endPoint[0], endPoint[1]+0.001)
            termgame.draw.line(screen, (int(255/math.exp(0.005*endPoint[1])),int(255/math.exp(0.005*endPoint[1])),int(255/math.exp(0.005*endPoint[1]))), (screen.get_width()*i/(fov*detail),screen.get_height()/2-20000/endPoint[1]+self.pitch), (screen.get_width()*i/(fov*detail),screen.get_height()/2+7000/endPoint[1]+self.pitch), math.ceil(20/detail))
            #termgame.draw.line(screen, "blue", self.pos, endPoint[0])
    
    def move(self, screen, keys: ScancodeWrapper, collisionObjects: Iterable[termgame.Rect]) -> None:
        speed= 2
        if keys[termgame.K_w] and castRay(screen, self.pos, self.angle, collisionObjects)[1] > speed:
            self.pos = combineTuple(self.pos, (speed*math.cos(self.angle),speed*math.sin(self.angle)), mode="sum")
        if keys[termgame.K_s] and castRay(screen, self.pos, self.angle + math.pi, collisionObjects)[1] > speed:
            self.pos = combineTuple(self.pos, (speed*math.cos(self.angle),speed*math.sin(self.angle)), mode="subtract")
        if keys[termgame.K_a] and castRay(screen, self.pos, self.angle-math.pi/2, collisionObjects)[1] > speed:
            self.pos = combineTuple(self.pos, (speed*math.cos(self.angle-math.pi/2),speed*math.sin(self.angle-math.pi/2)), mode="sum")
        if keys[termgame.K_d] and castRay(screen, self.pos, self.angle+math.pi/2, collisionObjects)[1] > speed:
            self.pos = combineTuple(self.pos, (speed*math.cos(self.angle-math.pi/2),speed*math.sin(self.angle-math.pi/2)), mode="subtract")

