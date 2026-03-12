import pygame, math
from typing import Literal, Iterable
Number = int | float

def combineTuple(a: tuple[Number, ...],b: tuple[Number, ...], mode: Literal["sum", "subtract"]) -> tuple[Number, ...]:
    def subtract(a):
        return a[0]-a[1]
    if mode == "sum":
        return tuple(map(sum, zip(a, b)))
    elif mode == "subtract":
        return tuple(map(subtract, zip(a, b)))
    raise ValueError("Invalid mode. Valid modes: sum, subtract.")

def castRay(screen: pygame.Surface, start: tuple[Number,Number], direction: Number, collisionObjects: Iterable[pygame.Rect]) -> tuple[tuple[Number, Number], Number]:
    distance = 0
    testPoint = start
    while True:

        if any(o.collidepoint(testPoint) for o in collisionObjects):
            return (testPoint, distance)
        testPoint = combineTuple(testPoint, (math.cos(direction), math.sin(direction)), mode="sum")
        distance += 1
        if not screen.get_rect().collidepoint(testPoint):
            return (testPoint, distance)