from tkinter import *
import time
import numpy
import random


class Car:
    def getDirection(self, topX):
        if topX < 250:
            return "right"
        if topX > 250:
            return "left"

    def __init__(self, canvas, colour, topX, topY, bottomX, bottomY, turnDirection):
        self.canvas = canvas
        self.direction = Car.getDirection(self, topX)
        self.turnDirection = turnDirection
        self.location = self.canvas.create_rectangle(topX, topY, bottomX, bottomY, fill=colour)

    def turn(self, distanceY, x):
        topXOld, topYOld, bottomXOld, bottomYOld = self.canvas.coords(self.location)
        self.canvas.coords(self.location, topXOld + 5, topYOld - 10, bottomXOld - 5, bottomYOld + 10)
        self.canvas.update()
        self.canvas.move(self.location, distanceY, x)
        self.canvas.update()

    def move(self, distanceX, distanceY):
        topXOld, topYOld, bottomXOld, bottomYOld = self.canvas.coords(self.location)
        averageX = [topXOld, bottomXOld]
        centre_x = numpy.mean(averageX)
        averageY = [topYOld, bottomYOld]
        centre_y = numpy.mean(averageY)
        x = 0
        name = self.location

        if (self.direction == "left"):
            x = distanceX * -1
        if (self.direction == "right"):
            x = distanceX
        if (self.turnDirection == "left"):
            bla = ""
        if (self.direction == "right" and self.turnDirection == "right"):
            if (centre_x < 215):
                self.canvas.move(self.location, x, distanceY)
            if (centre_x == 215 and centre_y == 135):
                Car.turn(self, distanceY, x)
            if (centre_y > 135):
                self.canvas.move(self.location, distanceY, x)
        if (self.direction == "left" and self.turnDirection == "right"):
            if (centre_x > 235):
                self.canvas.move(self.location, x, distanceY)
            if (centre_x == 235 and centre_y == 115):
                # Turn
                Car.turn(self, distanceY, x)
            if (centre_y < 115):
                self.canvas.move(self.location, distanceY, x)
        if (self.direction == "right" or "left") and self.turnDirection == "straight":
            self.canvas.move(self.location, x, distanceY)


class RouteController:
    def __init__(self, canvas):
        self.canvas = canvas
        self.cars = []

    def createCars(self):
        colours = ["blue", "green", "red", "yellow", "black", "white", "purple", "pink"]
        turns = ["right", "straight"]
        top = [[0, 125], [420, 105], [-60, 125], [500, 105], [-130, 125], [-170, 125], [550, 105], [-210, 125],
               [590, 105], [650, 105]]
        colour = []
        turn = []
        for i in range(10):
            colour.append(random.choice(colours))
            turn.append(random.choice(turns))

        car1 = Car(self.canvas, colour[0], top[0][0], top[0][1], top[0][0] + 30, top[0][1] + 20, turn[0])
        car2 = Car(self.canvas, colour[1], top[1][0], top[1][1], top[1][0] + 30, top[1][1] + 20, turn[1])
        car3 = Car(self.canvas, colour[2], top[2][0], top[2][1], top[2][0] + 30, top[2][1] + 20, turn[2])
        car4 = Car(self.canvas, colour[3], top[3][0], top[3][1], top[3][0] + 30, top[3][1] + 20, turn[3])
        car5 = Car(self.canvas, colour[4], top[4][0], top[4][1], top[4][0] + 30, top[4][1] + 20, turn[4])
        car6 = Car(self.canvas, colour[5], top[5][0], top[5][1], top[5][0] + 30, top[5][1] + 20, turn[5])
        car7 = Car(self.canvas, colour[6], top[6][0], top[6][1], top[6][0] + 30, top[6][1] + 20, turn[6])
        car8 = Car(self.canvas, colour[7], top[7][0], top[7][1], top[7][0] + 30, top[7][1] + 20, turn[7])
        car9 = Car(self.canvas, colour[8], top[8][0], top[8][1], top[8][0] + 30, top[8][1] + 20, turn[8])
        car10 = Car(self.canvas, colour[9], top[9][0], top[9][1], top[9][0] + 30, top[9][1] + 20, turn[9])
        self.cars.append(car1)
        self.cars.append(car2)
        self.cars.append(car3)
        self.cars.append(car4)
        self.cars.append(car5)
        self.cars.append(car6)
        self.cars.append(car7)
        self.cars.append(car8)
        self.cars.append(car9)
        self.cars.append(car10)

    def moveCars(self):
        for i in range(70):
            for car in self.cars:
                car.move(10, 0)
            self.canvas.update()
            time.sleep(0.05)

# Create window
if __name__ == '__main__':
    print("hello")

root = Tk()

canvas = Canvas(root, width=450, height=250, bg="grey")
canvas.pack()
canvas.create_rectangle(0, 0, 200, 100, fill="green")
canvas.create_rectangle(0, 150, 200, 250, fill="green")
canvas.create_rectangle(250, 0, 450, 100, fill="green")
canvas.create_rectangle(250, 150, 450, 250, fill="green")

# Move cars
for i in range(5):
    routeController = RouteController(canvas)
    routeController.createCars()
    routeController.moveCars()

# GO!!
root.mainloop()
