import pygame
import froggerlib


class Frogger:

    def __init__(self, width, height, lane_size):
        self.mWidth = width
        self.mHeight = height
        self.mBackGroundColor = (255, 255, 255)
        self.mFrogColor = (0, 255, 0)
        self.mStageColor = (255, 0, 255)
        self.mRoadColor = (0, 0, 0)
        self.mWaterColor = (0, 0, 255)
        self.mCarColor = (0, 255, 255)
        self.mTruckColor = (125, 125, 125)
        self.mRaceCarColor = (255, 0, 205)
        self.mDozerColor = (0, 25, 255)
        self.mGrassColor = (100, 205, 100)

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


    def evolve(self, dt):
        if self.mFrogDead:
            return

        self.moveCars()
        self.mFrog.move()
        self.checkLanesHitFrog()
        self.checkCarsHitFrog()
        if self.mFrog.outOfBounds(self.mWidth, self.mHeight):
            self.mFrogDead = True
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
        self.drawFrog(surface)

        return



# Check frog if it is out of balance.