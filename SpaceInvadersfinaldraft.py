#Sarah Graff 5/22/17
#"Space Invaders" - instructions are included in the game when played
#I hereby certify that this program is solely the result of my own work and is in compliance with the Academic Integrity policy of the course syllabus.
import Draw
import sys
Draw.setCanvasSize(500, 500)
Draw.setColor(Draw.BLACK)
Draw.setBackground(Draw.BLACK)
aliens = [(10, 50), (70, 50), (130, 50), (190, 50), (250, 50), (310, 50), (370, 50)] #each item in the list is the set of coordinates where the future aliens will be drawn 
def drawAliens(a):  #draws the aliens at the location of the coordinates in the list
    for i in range(len(a)): #for each item in the list 'a' 
        (x, y) = a[i] #the item equals the coordinates x and y
        Draw.picture("C:/CodeAssignments/alieninvader2.gif", x, y) #draws the alien picture at a[i]'s coordinate
    Draw.show()
def moveAliens(a, dx, dy): #increases or decreases the value of the x and y coordinates of the items in list 'a' by dx and dy
    for i in range(len(a)): #for each item in list 'a' 
        (x, y) = a[i] #the item equals the coordinates x and y
        a[i] = (x+dx, y+dy) #add the values of dx and dy to the existing x and y coordinates
        if y >= 465: #if the aliens have moved past the position of the spaceship
            Draw.setFontSize(50)
            Draw.setColor(Draw.CYAN)
            Draw.setFontFamily("OCR A Extended")
            Draw.setFontBold(True)
            Draw.string('GAME OVER', 90, 200) #the game ends  
def drawSpaceship(xOffset): #draws the spaceship object with a variable as its x coordinate so it can be moved along the x-axis
        Draw.setColor(Draw.GREEN)
        Draw.filledRect(xOffset, 485, 50, 26) 
        Draw.filledOval(xOffset + 24, 470, 5, 15)   
def scoreTally(score): #increments the score based on the number of aliens left in the list 
        Draw.setFontSize(25)
        Draw.setColor(Draw.CYAN)
        Draw.setFontFamily("OCR A Extended")
        Draw.setFontBold(True)
        Draw.string(str(score), 10, 10) #draws the string of the score           
def laser(laserX, laserY): #draws the laser at the given x and y coordinates
    Draw.setColor(Draw.GREEN)
    Draw.filledRect(laserX, laserY, 9, 17) #draws the laser shape at the given x and y coordinates
def hitAliens(a, lx, ly): #takes list of aliens and position of laser and determines if the alien has been hit
    if ly != None: #if the laser has been fired
        for i in range(len(a)): #for each item in the list 'a'
            (x, y) = a[i] #the item equals the coordinates x and y
            if x <= lx <= x + 60 and y < ly <= y + 30: #if the x coordinate of the laser is greater than or equal to the value of the x coordinate of the alien and less than or equal to the value of the x coordinate plus 60 (which is the width of the alien) or if the y coordinate of the laser is greater than the y coordinate of the alien and less than or equal to the y coordinate plus 30, with is the height of the alien
                del a[i] #delete that alien from the list
                return a #return the modified list             
        return -1 #if nothing was hit, return -1 and the loop continues
def winGame(a): #takes list of aliens, determines if the game is won
    if len(a) == 0: #if the length of the list of aliens is 0, then the game is won
        Draw.setFontSize(50)
        Draw.setColor(Draw.MAGENTA)
        Draw.setFontFamily("OCR A Extended")
        Draw.setFontBold(True)
        Draw.string('YOU WON!', 90, 200)            
def play1():  #the main function that 'plays' the game
    xOffset = 225 #the default xOffset for the spaceship before anything has changed in the gameplay
    laserX = xOffset+24 #default xcoordinate for the laser that equals the x coordinate of the middle of the spaceship
    laserY = None #the laser does not exist yet
    numSteps = 0 #keeps track of the number of times that aliens have moved across the canvas, at this point initially 0
    direction = 1 #the default, 'positive' direction for the aliens to move
    while True: #until the game has ended:          
        if Draw.hasNextKeyTyped(): #wait for a key to be typed            
            newKey = Draw.nextKeyTyped()
            if newKey == "Right": #if the key typed is the right arrow:
                xOffset += 20 #the spaceship moves 20 pixels to the right along the x axis
            elif newKey == "Left": #if the key typed is the left arrow:
                xOffset -= 20 #the spaceship moves 20 pixels to the left along the x axis
            elif newKey == "Up": #if the key typed is the up arrow:
                laserX = xOffset + 24 #the laserX is at the position of the xOffset plus 24 pixels
                laserY = 500 #the laserY is at the y coordinate of the bottom of the spaceship, it is no longer None, and now exists in the gameplay
        Draw.clear() #clears the canvas
        drawSpaceship(xOffset) #draws the spaceship at its new position
        drawAliens(aliens) #draws the list of aliens on the canvas
        if laserY != None: #if the laser has been entered into gameplay
            sys.stdout.flush() #inserted by the professor to make the loop that moves the laser work correctly
            laserY -= 40 #have it move down the y axis 40 pixels at a time
            laser(laserX, laserY) #draw the laser at its new position everytime through the loop    
        if numSteps == 10: #takes 10 steps for the aliens to move across the screen
            moveAliens(aliens, 0, +20) #move the aliens down the y-axis 20 
            direction = -direction #direction changes after 10 steps have happened
            numSteps = 0 #resets the number of steps
        if direction == 1: #if the direction is positive:
            moveAliens(aliens, +7, 0) #moves aliens across the x axis in the positive direction
        else: #if the direction is negative
            moveAliens(aliens, -7, 0) #move the aliens in the negative direction on the x axis
        numSteps += 1  #everytime the aliens move across the x axis, the list of numSteps increases by 1
        hitAliens(aliens, laserX, laserY) #determine if any aliens have been hit by the laser
        scoreTally((7 - (len(aliens)))*100) #multiply the score by the number of aliens that have been hit by the laser and removed from the list
        winGame(aliens) #determine if the game has been won
        Draw.show(150) #display the game       
while True: #until the mouse has been clicked, display the instructions for the game
    Draw.setColor(Draw.YELLOW) 
    Draw.setFontSize(15)
    Draw.setFontFamily("OCR A Extended")
    Draw.setFontBold(True)    
    Draw.string("Welcome to Space Invaders:", 90, 30) 
    Draw.setColor(Draw.CYAN)
    Draw.setFontSize(20)
    Draw.string("Use the arrow key to", 80, 70)
    Draw.string("move the spaceship", 90, 90) 
    Draw.string("back and forth", 100, 110)
    Draw.setColor(Draw.GREEN)
    Draw.string("Press the up key to fire", 70, 140)
    Draw.setColor(Draw.MAGENTA)
    Draw.string("Shoot all the aliens before", 30, 190)
    Draw.string("they reach the spaceship", 60, 210)
    Draw.setColor(Draw.ORANGE)
    Draw.string("Click anywhere to begin", 80, 300)
    if Draw.mousePressed(): #if the mouse has been clicked:
        Draw.clear() #remove the instructions from the canvas
        play1() #initiate gameplay
        




