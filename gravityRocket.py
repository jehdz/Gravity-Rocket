from graphics import *
import random
import math
import graphics 



def didCollide(x1,y1,r1,x2,y2,r2):
    if math.sqrt((x2-x1)**2 + (y2-y1)**2) <= r1 + r2:
        return True
    else:
        return False


def main():
    windowX = 400
    windowY = 600
    win = GraphWin('Space', windowX, windowY, autoflush=False)
    win.setBackground('Gray20')

    currentScore = 0
    scoreText = Text(Point(200,20), str(currentScore))
    scoreText.draw(win)
    scoreText.setTextColor('Gray20')

    gameOver = Text(Point(win.getWidth()/2, 200), 'GAME OVER')
    gameOver.setTextColor('Green')
    gameOver.setStyle('bold')
    gameOver.setSize(36)
    gameOver.setFace('courier')
    
    highScore = Text(Point(win.getWidth()/2, 400), 'FINAL SCORE')
    highScore.setTextColor('Yellow')
    highScore.setStyle('italic')
    highScore.setSize(28)
    highScore.setFace('helvetica')

    scoreText = Text(Point(win.getWidth()/2,450), str(currentScore))
    scoreText.setFill('white')
    scoreText.setStyle('bold')
    scoreText.setStyle('italic')
    scoreText.setSize(24)
    scoreText.setFace('helvetica')
    
    stars = []
    for i in range(500):                      # make a list of 500 random points

        x = random.randint(0, 500)
        y = random.randint(0, 700)
        p = graphics.Point(x, y)
        

        p.setFill("yellow")
        p.draw(win)

        stars.append(p)
    

    
    cameraX = 0
    cameraY = 0
    playerX = windowX/2
    playerY = windowY/2
    obstacles = []
    y = 0
    for i in range(100):
        x = 0
        y = y -200
        circle = Circle(Point(x, y), 10)
        obstacles.append(circle)
    

    for i in range(len(obstacles)):
        obstacles[i].setFill(color_rgb(255,0,0))
        obstacles[i].draw(win)


    obstacleLocations = []
    y = 0
    for i in range(100):
        x = 0
        y = y - 200
        location = [x, y]
        obstacleLocations.append(location)

        
    obstacleSpeeds = []
    for i in range(100):
        speed = random.randint(10, 20)
        obstacleSpeeds.append(speed)
 
    player = Circle(Point(playerX,playerY),20)
    player.setFill(color_rgb(80,218,214))
    player.draw(win)
    xVelocity = 0
    yVelocity = 0
    currentObstacleSpawn = -200
    while True:
        if -playerY > currentScore:
            currentScore = -playerY
            scoreText.setText(str(currentScore))
        for s in stars:
            s.move(0, 10)                          # move it down 2 pixels

            if s.getY() > 699:           # if it's out of bounds, move it back to 0
                s.move(0, -700)

        
        playerX, playerY = moveTo(player, playerX, playerY, xVelocity, yVelocity, playerX-cameraX+xVelocity, playerY-cameraY+yVelocity)
        for i in range(len(obstacles)-1,-1,-1):
            obstacleLocations[i][0], obstacleLocations[i][1] = moveTo(obstacles[i], obstacleLocations[i][0], obstacleLocations[i][1], obstacleSpeeds[i], 0, obstacleLocations[i][0]-cameraX+obstacleSpeeds[i], obstacleLocations[i][1]-cameraY)
            if obstacleLocations[i][0] < 0 or obstacleLocations[i][0] > windowX:
                obstacleSpeeds[i] *= -1
            if didCollide(playerX,playerY,20,obstacleLocations[i][0], obstacleLocations[i][1], 10) or playerY > cameraY + windowY:
                win.setBackground('black')
                gameOver.draw(win)
                highScore.draw(win)
                scoreText.draw(win)
                win.getMouse()
                win.close()
                
            
                
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
