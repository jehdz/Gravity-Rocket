from graphics import *
import random
import math

#list of obstacles
#format:
#[
#   [x, y, xVel],
#   [x, y, xVel]
#]

def didCollide(x1,y1,r1,x2,y2,r2):
    if math.sqrt((x2-x1)**2 + (y2-y1)**2) <= r1 + r2:
        return True
    else:
        return False

def main():
    windowX = 400
    windowY = 600
    win = GraphWin('Space', windowX, windowY, autoflush=False)
    cameraX = 0
    cameraY = 0
    playerX = windowX/2
    playerY = windowY/2
    obstacles = [
        Circle(Point(0,0), 10),
        Circle(Point(0,-200), 10),
        Circle(Point(0,-400), 10),
        Circle(Point(0,-600), 10),
        Circle(Point(0,-800), 10),
        Circle(Point(0,-1000), 10)
    ]
    for i in range(len(obstacles)):
        obstacles[i].setFill(color_rgb(255,0,0))
        obstacles[i].draw(win)
    obstacleLocations = [
        [0,0],
        [0,-200],
        [0,-400],
        [0,-600],
        [0,-800],
        [0,-1000]

    ]
    obstacleSpeeds = [2,5,4,6,7,3]
 
    player = Circle(Point(playerX,playerY),20)
    player.setFill(color_rgb(80,218,214))
    player.draw(win)
    xVelocity = 0
    yVelocity = 0
    currentObstacleSpawn = -200
    while True:
        playerX, playerY = moveTo(player, playerX, playerY, xVelocity, yVelocity, playerX-cameraX+xVelocity, playerY-cameraY+yVelocity)
        for i in range(len(obstacles)-1,-1,-1):
            obstacleLocations[i][0], obstacleLocations[i][1] = moveTo(obstacles[i], obstacleLocations[i][0], obstacleLocations[i][1], obstacleSpeeds[i], 0, obstacleLocations[i][0]-cameraX+obstacleSpeeds[i], obstacleLocations[i][1]-cameraY)
            if obstacleLocations[i][0] < 0 or obstacleLocations[i][0] > windowX:
                obstacleSpeeds[i] *= -1
            if didCollide(playerX,playerY,20,obstacleLocations[i][0], obstacleLocations[i][1], 10) or playerY > cameraY + windowY:
                print("YOU LOSE")
            """
            if obstacleLocations[i][1] - windowY > cameraY:
                del obstacleLocations[i]
                del obstacleSpeeds[i]
                obstacles[i].undraw()
                del obstacles[i]
        if cameraY - 10 < currentObstacleSpawn:
            rSpeed = random.randrange(2,5)
            rX = random.randrange(10,windowX-10)
            obstacleLocations.append([rX, currentObstacleSpawn])
            obstacles.append(Circle(Point(rX, currentObstacleSpawn), 10))
            obstacleSpeeds.append(rSpeed)
            currentObstacleSpawn -= 200
            print(obstacles)
            """
                
        
        yVelocity +=2.5
        if win.checkKey() == 'space':
            yVelocity = -23 
        print(win.checkKey())
        update(60)
        if playerY < cameraY + windowY/2:
            cameraY = playerY - windowY/2

def moveTo(shape, shapeX, shapeY, dx, dy, x, y):
    shape.move(x-shape.getCenter().getX(), y-shape.getCenter().getY())
    return shapeX + dx, shapeY + dy
        
main()
