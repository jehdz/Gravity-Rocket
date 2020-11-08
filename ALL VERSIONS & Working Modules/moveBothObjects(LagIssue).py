from graphics import *
import time

def moveBoth(player, star, win):

    xVelocity = 0
    yVelocity = 0
    radius = 25
    xLow = radius
    xHigh = win.getWidth() - radius

    dx = 5
    dy = 2
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

        player.move(xVelocity, yVelocity)
        yVelocity +=2.5
        if win.checkKey() == 'space': 
            yVelocity = -23

    

def main():
    windowX = 500
    windowY = 700
    win = GraphWin('Space', windowX, windowY)
    win.setBackground('Gray20')

    #rocket
    player = Image(Point(windowX/2,windowY/2),"rocket.gif")
    player.draw(win)



    #star
    star = Image(Point(150, 150), "star.gif")
    star.draw(win)

    moveBoth(player, star, win)
main()

