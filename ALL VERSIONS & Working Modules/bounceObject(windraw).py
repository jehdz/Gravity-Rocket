from graphics import *
import time

def bounceInWindow(Object, dx, dy, xLow, xHigh):

    delay = .005
    while True:
        Object.move(dx, dy)
        center = Object.getCenter()
        x = center.getX()
        if x < xLow:
            dx = -dx
        elif x > xHigh:
            dx = -dx
        time.sleep(delay)

def bounceBall():
    win = GraphWin(1200, 400)
    win.setBackground('Gray20')
    win.yUp()

    ball = Circle(Point(100, 100), 20)
    ball.setFill('red3')
    ball.draw(win)

    radius = 20
    xLow = radius
    xHigh = win.getWidth() - radius

    dx = 5
    dy = 0


    bounceInWindow(ball, dx, dy, xLow, xHigh)
    win.close()

bounceBall()

    
