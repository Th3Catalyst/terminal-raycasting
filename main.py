from Assets import Number, math, combineTuple, Player, Wall


def main() -> None:
    fov = int(input("Enter fov: "))

    termgame.init()
    screen = termgame.display.set_mode((1280, 720))
    clock = termgame.time.Clock()

    player = Player((screen.get_width()/2 + 10, screen.get_height()/2),0)

    walls = [
        Wall(termgame.Rect(0,0,20,720)),
        Wall(termgame.Rect(0, 700, 1280, 20)),
        Wall(termgame.Rect(1260, 0, 20, 720)),
        Wall(termgame.Rect(0, 0, 1280, 20)),
    ]
    for i in range(16):
        for j in range(9):
            walls.append(Wall(termgame.Rect(i*80,j*80,40,40)))
    debug = False
    oldMousePos = termgame.mouse.get_pos()
    running = True
    while running:
        for event in termgame.event.get():
            if event.type == termgame.QUIT:
                running = False

        player.move(screen, termgame.key.get_pressed(), list(map(lambda i: i.rect, walls)))
        player.angle -= (oldMousePos[0] - termgame.mouse.get_pos()[0]) / 100
        player.pitch += (oldMousePos[1] - termgame.mouse.get_pos()[1]) * 10
        oldMousePos = termgame.mouse.get_pos()

        screen.fill("#000000")

        player.rayCast(screen, fov, list(map(lambda i: i.rect, walls)))
        if debug:
            player.draw(screen)
            for wall in walls:
                wall.draw(screen)


        termgame.display.flip()

        clock.tick(60)

    termgame.quit()


if __name__ == "__main__":
    main()
