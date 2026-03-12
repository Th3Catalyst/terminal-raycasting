from Assets import pygame, Number, math, combineTuple, Player, Wall


def main() -> None:
    fov = int(input("Enter fov: "))

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    player = Player((screen.get_width()/2 + 10, screen.get_height()/2),0)

    walls = [
        Wall(pygame.Rect(0,0,20,720)),
        Wall(pygame.Rect(0, 700, 1280, 20)),
        Wall(pygame.Rect(1260, 0, 20, 720)),
        Wall(pygame.Rect(0, 0, 1280, 20)),
    ]
    for i in range(16):
        for j in range(9):
            walls.append(Wall(pygame.Rect(i*80,j*80,40,40)))
    debug = False
    oldMousePos = pygame.mouse.get_pos()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.move(screen, pygame.key.get_pressed(), list(map(lambda i: i.rect, walls)))
        player.angle -= (oldMousePos[0] - pygame.mouse.get_pos()[0]) / 100
        player.pitch += (oldMousePos[1] - pygame.mouse.get_pos()[1]) * 10
        oldMousePos = pygame.mouse.get_pos()

        screen.fill("#000000")

        player.rayCast(screen, fov, list(map(lambda i: i.rect, walls)))
        if debug:
            player.draw(screen)
            for wall in walls:
                wall.draw(screen)


        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()