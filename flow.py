from graphics import *
import time, random

class Car:

    def __init__(self, speed = 0, point = Point):
        self.speed = speed
        self.point = point

    def displayCar(self):
        print("Speed: %s Point: %s" % (self.speed ,self.point))

    def drawCar(self, win):
        disk = Circle(self.point, 5)
        disk.setOutline("red")
        disk.setFill("red")
        disk.draw(win)
        return disk

    def move(self,point = Point):
        self.disk.move(point)


def driveCar(car, xLow, xHigh, yLow, yHigh, win):

    delay = 0.05
    disk = car.drawCar(win)
    for i in range(6000):

        disk.move(5,0)
        car.point = disk.getCenter()
        car.displayCar()
        if car.point.x < xLow:
            car.point.x = xHigh
        elif car.point.x > xHigh:
            car.point.x = xLow
        if car.point.y < yLow:
            car.point.y = yHigh
        elif car.point.y > yHigh:
            car.point.y = yLow
        time.sleep(delay)


def flow():

    winWidth = 290
    winHeight = 290
    win = GraphWin('Flow', winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight)

    radius = 5
    xLow = radius  # center is separated from the wall by the radius at a bounce
    xHigh = winWidth - radius
    yLow = radius
    yHigh = winHeight - radius

    car = Car(10, Point(20,20))

    driveCar(car, xLow, xHigh, yLow, yHigh, win)

    win.close()

flow()






