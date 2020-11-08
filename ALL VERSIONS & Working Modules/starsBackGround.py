
from graphics import *
import random



def backGround():
    windowX = 400
    windowY = 600
    win = GraphWin('Space', windowX, windowY)
    win.setBackground('Gray20')

    stars = []
    for i in range(500):                      # make a list of 500 random points

        x = random.randint(0, 500)
        y = random.randint(0, 700)
        p = graphics.Point(x, y)
        

        p.setFill("yellow")
        p.draw(win)

        stars.append(p)


    while True:                              # keep looping forever
      for s in stars:
        s.move(0, 10)                          # move it down 2 pixels

        if s.getY() > 699:           # if it's out of bounds, move it back to 0
            s.move(0, -700)


def main():
    backGround()

    ball = Circle(Point(200, 200), 50)
    ball.setFill('red')
    ball.draw(win)

main()
