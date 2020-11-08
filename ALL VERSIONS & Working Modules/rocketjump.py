from graphics import *

def moveAll(rocket, dx, dy):
    '''Move that ball'''
    for Cir1 in Cir1:
        Cir1.move(dx, dy)

def main():
    win = GraphWin('Space', 600, 300)
    win.yUp()

    rocket1 = Circle(Point(200,100), 20) # set center and radius
    rocket1.setFill("red")
    rocket1.draw(win)

    win.getMouse()

    rocket2 = Circle(Point(200, 200), 20)
    rocket2.setFill('red')
    rocket2.draw(win)

    rocket1.undraw()

    win.getMouse()

    rocket3 = Circle(Point(200, 100), 20) # set endpoints
    rocket3.setFill('red')
    rocket3.draw(win)

    rocket2.undraw()

    message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    message .draw(win)
    win.getMouse()
    win.close()

def rocket():
    win = GraphWin('Space', 600, 200)
    win.yUp()

    rocket = Circle(Point(100,100), 20) # set center and radius
    rocket.setFill("red")
    rocket.draw(win)

    win.getMouse()
    
    v=25
    for i in range (100):
        moveAll(Cir1, 0, V)
        time.sleep(0.0167)
        v=v-1

    win.promptClose(win.getWidth()/2, 20)
    
main()


