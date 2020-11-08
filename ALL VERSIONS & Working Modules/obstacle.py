from graphics import *
import time

def bounceInWindow(star, dx, dy, xLow, xHigh):

    delay = .005
    while True:
        star.move(dx, dy)
        center = star.getAnchor()
        x = center.getX()
        if x < xLow:
            dx = -dx
        elif x > xHigh:
            dx = -dx
        time.sleep(delay)


def bounceStar():
    win = GraphWin('space', 500, 700)
    win.setBackground('Gray20')




    star = Image(Point(150, 150), "star.gif")
    star.draw(win)


    radius = 25
    xLow = radius
    xHigh = win.getWidth() - radius

    dx = 5
    dy = 0


    bounceInWindow(star, dx, dy, xLow, xHigh)
    win.close()

bounceStar()

    
