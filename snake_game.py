import pygame as py
py.init()
screen_width = 1000
screen_height = 1000
screen = py.display.set_mode((screen_width, screen_height))
running = True  # for running the screen continously
clock = py.time.Clock()  # no.of times the while loop runs in a second

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    # fills the screen into the color specified by RGB
    screen.fill((175, 215, 70))
    py.display.update()
    clock.tick(60)  # setting our fps to 60
