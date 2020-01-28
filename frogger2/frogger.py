import pygame
import froggerlib


class Frogger:

    def __init__(self, width, height, lane_size):
        self.mWidth = width
        self.mHeight = height
        self.mBackGroundColor = (255, 255, 255)
        self.mFrogColor = (0, 255, 0)
        self.mStageColor = (134, 65, 244)
        self.mRoadColor = (0, 0, 0)
        self.mWaterColor = (0, 0, 255)
        self.mCarColor = (0, 255, 255)
        self.mTruckColor = (125, 125, 125)
        self.mRaceCarColor = (244, 66, 179)
        self.mDozerColor = (151, 244, 65)
        self.mGrassColor = (100, 205, 100)
        self.mHomeColor = (66, 244, 235)
        self.mLogColor = (244, 65, 100)
        self.mTurtleColor = (65, 244, 146)

        #
        self.mLaneSize = lane_size
        self.mObjectSize = int(self.mLaneSize * 0.8)
        self.mObjectGap = int((self.mLaneSize - self.mObjectSize) / 2)
        self.mFrogDead = False

        # Frog
        w = self.mObjectSize
        h = self.mObjectSize
        x = int(self.mWidth / 2 - w / 2)
        y = 10 * self.mLaneSize + self.mObjectGap
        speed = 8
        horizontal_gap = self.mLaneSize
        vertical_gap = self.mLaneSize
        self.mFrog = froggerlib.Frog(x, y, w, h, x, y, speed, horizontal_gap, vertical_gap)

        # Lanes
        self.mLanes = []
        self.mLanes.append(froggerlib.Stage(0, 10 * self.mLaneSize, self.mWidth, self.mLaneSize))
        self.mLanes.append(froggerlib.Road(0, 9 * self.mLaneSize, self.mWidth, self.mLaneSize))
        self.mLanes.append(froggerlib.Road(0, 8 * self.mLaneSize, self.mWidth, self.mLaneSize))
        self.mLanes.append(froggerlib.Road(0, 7 * self.mLaneSize, self.mWidth, self.mLaneSize))
        self.mLanes.append(froggerlib.Road(0, 6 * self.mLaneSize, self.mWidth, self.mLaneSize))
        self.mLanes.append(froggerlib.Stage(0, 5 * self.mLaneSize, self.mWidth, self.mLaneSize))
        self.mLanes.append(froggerlib.Water(0, 4 * self.mLaneSize, self.mWidth, self.mLaneSize))
        self.mLanes.append(froggerlib.Water(0, 3 * self.mLaneSize, self.mWidth, self.mLaneSize))
        self.mLanes.append(froggerlib.Water(0, 2 * self.mLaneSize, self.mWidth, self.mLaneSize))
        self.mLanes.append(froggerlib.Water(0, 1 * self.mLaneSize, self.mWidth, self.mLaneSize))
        self.mLanes.append(froggerlib.Grass(0, 0 * self.mLaneSize, self.mWidth, self.mLaneSize))

        # Home spots
        self.mLanes.append(froggerlib.Home(80, 0 * self.mLaneSize, 70, self.mLaneSize))
        self.mLanes.append(froggerlib.Home(230, 0 * self.mLaneSize, 70, self.mLaneSize))
        self.mLanes.append(froggerlib.Home(380, 0 * self.mLaneSize, 70, self.mLaneSize))
        self.mLanes.append(froggerlib.Home(530, 0 * self.mLaneSize, 70, self.mLaneSize))

        # Logs
        self.mLogs = []
        x = self.mWidth
        y = 4*self.mLaneSize + self.mObjectGap
        w = self.mObjectSize + 80
        h = self.mObjectSize
        dx = 0 - w
        dy = y
        speed = 6
        speed1 = 5
        y1 = 1 * self.mLaneSize + self.mObjectGap
        dy1 = y1
        self.mLogs.append(froggerlib.Log(x, y, w, h, dx, dy, speed))
        self.mLogs.append(froggerlib.Log(x, y1, w, h, dx, dy1, speed1))



        #Turtles
        self.mTurtles = []
        x = self.mWidth
        y = 3*self.mLaneSize + self.mObjectGap
        w = self.mObjectSize + 80
        h = self.mObjectSize
        dx = self.mWidth
        dy = y
        speed = 5

        speed1 = 8
        y1 = 2 * self.mLaneSize + self.mObjectGap
        dy1 = y1
        self.mTurtles.append(froggerlib.Turtle(x, y, w, h, dx, dy, speed))
        self.mTurtles.append(froggerlib.Turtle(x, y1, w, h, dx, dy1, speed1))




        self.mCars = [ ]
        x = self.mWidth
        y = 9*self.mLaneSize + self.mObjectGap
        w = self.mObjectSize
        h = self.mObjectSize
        dx = 0 - w
        dy = y
        speed = 10

        #Truck
        y1 = 8*self.mLaneSize + self.mObjectGap
        speed1 = 7
        dy1 = y1
        x1 = 0
        dx1 = self.mWidth
        if dx1 < 0 + self.mWidth:
            dx1 = 0

        #Dozer
        y2 = 7*self.mLaneSize + self.mObjectGap
        speed2 = 2
        dy2 = y2
        x2 = 0
        dx2 = self.mWidth

        #RaceCar
        y3 = 6*self.mLaneSize + self.mObjectGap
        dy3 = y3
        self.mins = 5
        self.maxs = 20


        self.mCars.append(froggerlib.Car( x, y, w, h, dx, dy, speed ))
        self.mCars.append(froggerlib.Truck( x1, y1, w, h, dx1, dy1, speed1))
        self.mCars.append(froggerlib.Dozer( x2,y2,w,h,dx2,dy2,speed2))
        self.mCars.append(froggerlib.RaceCar( x,y3,w,h,dx,dy3,self.mins,self.maxs))


    #Moving Keys
    # ===================================================
    def actOnHoldRight( self ):
        self.mFrog.right()
        return

    def actOnHoldUP( self ):
        self.mFrog.up()
        return

    def actOnHoldDown(self):
        self.mFrog.down()
        return

    def actOnHoldLeft(self):
        self.mFrog.left()
        return


    def checkLanesHitFrom(self):
        for lane in self.mLanes:
            if lane.hits( self.mFrog ):
                self.mFrogDead = True
        return

    def checkLanesHitFrog(self):
        for lane in self.mLanes:
            if lane.hits(self.mFrog):
                self.mFrogDead = True
        return

    def checkCarsHitFrog(self):
        for car in self.mCars:
            if car.hits(self.mFrog):
                self.mFrogDead = True

    def moveCars(self):
        for car in self.mCars:
            car.move()
            if car.atDesiredLocation():
                if car.getDesiredX() == self.mWidth:
                    car.setX(0)
                else:
                    car.setX(self.mWidth)
        return

    def moveLogs(self):
        for log in self.mLogs:
            log.move()
            if log.atDesiredLocation():
                if log.getDesiredX() == self.mWidth:
                    log.setX(0)
                else:
                    log.setX(self.mWidth)


    def moveTurtles(self):
        for turtle in self.mTurtles:
            turtle.move()
            if turtle.atDesiredLocation():
                if turtle.getDesiredX() == self.mWidth:
                    turtle.setX(0)
                else:
                    turtle.setX(self.mWidth)


    #=============================================================
    def evolve(self, dt):
        if self.mFrogDead:
            return
        self.moveCars()
        self.moveLogs()
        self.moveTurtles()
        self.mFrog.move()
        self.checkLanesHitFrog()
        self.checkCarsHitFrog()

        for log in self.mLogs:
            log.supports(self.mFrog)
        if self.mFrog.outOfBounds(self.mWidth, self.mHeight):
            self.mFrogDead = True

        for turtle in self.mTurtles:
            turtle.supports(self.mFrog)
        if self.mFrog.outOfBounds(self.mWidth, self.mHeight):
            self.mFrogDead = True
        return

    # Draw Logs and Turtles
    def drawLogs(self, surface):
        for log in self.mLogs:
            color = self.mLogColor
            rect = pygame.Rect(int(log.getX()), int(log.getY()), int(log.getWidth()), int(log.getHeight()))
            pygame.draw.rect(surface,color, rect,0)
        return

    def drawTurtles(self, surface):
        for turtle in self.mTurtles:
            color = self.mTurtleColor
            rect = pygame.Rect(int(turtle.getX()), int(turtle.getY()), int(turtle.getWidth()), int(turtle.getHeight()))
            pygame.draw.rect(surface,color, rect,0)
        return



    # draw Frog
    # ===================================================
    def drawFrog( self, surface ):
        rect = pygame.Rect( int ( self.mFrog.getX( ) ), int ( self.mFrog.getY( ) ), int ( self.mFrog.getWidth( ) ), int ( self.mFrog.getHeight( ) ) )
        pygame.draw.rect( surface, self.mFrogColor, rect, 0 )
        return

    # draw Lanes
    # ===================================================
    def drawLanes(self, surface):
        for lane in self.mLanes:
            if isinstance(lane, froggerlib.Road):
                color = self.mRoadColor
            elif isinstance(lane, froggerlib.Grass):
                color = self.mGrassColor
            elif isinstance(lane, froggerlib.Stage):
                color = self.mStageColor
            elif isinstance(lane, froggerlib.Water):
                color = self.mWaterColor
            elif isinstance(lane, froggerlib.Home):
                color = self.mHomeColor

            rect = pygame.Rect(int(lane.getX()), int(lane.getY()), int(lane.getWidth()), int(lane.getHeight()))
            pygame.draw.rect(surface, color, rect, 0)

        return

    # draw Car
    # ===================================================
    def drawCars(self, surface):
        for car in self.mCars:
            if isinstance(car, froggerlib.Car):
                color = self.mCarColor
            elif isinstance(car, froggerlib.Truck):
                color = self.mTruckColor
            elif isinstance(car, froggerlib.Dozer):
                color = self.mDozerColor
            elif isinstance(car, froggerlib.RaceCar):
                color = self.mRaceCarColor

            rect = pygame.Rect(int(car.getX()), int(car.getY()), int(car.getWidth()), int(car.getHeight()))
            pygame.draw.rect(surface, color, rect, 0)

        return






    # draws the current state of the system
    # ===================================================

    def draw( self, surface ):
        # rectangle to fill the background
        rect = pygame.Rect( int ( 0 ), int ( 0 ), int ( self.mWidth ), int ( self.mHeight ) )
        pygame.draw.rect( surface, self.mBackGroundColor, rect, 0 )

        self.drawLanes(surface)
        self.drawCars(surface)
        self.drawLogs(surface)
        self.drawTurtles(surface)
        self.drawFrog(surface)
        return


# Call support on every log and turtle and see if they support frog object. Other would be an Frog and self is (turtle and log)
#