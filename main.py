# Create window
import random
import time
from tkinter import Tk
from turtle import Canvas
import math


class Car():
    # car properties
    pos_x = 100  # initial position
    pos_y = 100
    heading = 0  # car direction in rad
    speed = 10  # car speed in pixels / step
    size = 10  # car size in pixels
    color = "red"

    def __init__(self):
        """
        generate a valid heading and corresponding start position eac time a new car is generated
        """
        self.heading = random.choice([0, math.pi / 2, math.pi, math.pi * 1.5])
        if (self.heading == 0):  # car heading right
            self.pos_x = 0
            self.pos_y = height / 2 + roadWidth / 3
        elif (self.heading == math.pi / 2):  # car heading down
            self.pos_x = width / 2 - roadWidth / 3
            self.pos_y = 0
        elif (self.heading == math.pi):  # car heading left
            self.pos_x = width
            self.pos_y = height / 2 - roadWidth / 3
        elif (self.heading == math.pi * 1.5):  # car heading up
            self.pos_x = width / 2 + roadWidth / 3
            self.pos_y = height

        self.color = random.choice(["blue", "green", "red", "yellow", "black", "white", "purple", "pink"])

    def turn(self):
        directionTurn = random.choice(["left", "right", "none"])
        if directionTurn == "left":
            # do something
            self.heading = self.heading + math.pi / 2

    def move(self):
        """
        calculate new car position given speed and heading
        """
        self.pos_x = self.pos_x + math.cos(self.heading) * self.speed
        self.pos_y = self.pos_y + math.sin(self.heading) * self.speed

    def draw(self):
        # draw the car. Depending on direction, turn the car
        if (self.heading == 0 or self.heading == math.pi):  # going left or right
            canvas.create_rectangle(self.pos_x - 2 * self.size, self.pos_y - self.size, self.pos_x + 2 * self.size,
                                    self.pos_y + self.size, fill=self.color)
        else:  # going up or down
            canvas.create_rectangle(self.pos_x - self.size, self.pos_y - 2 * self.size, self.pos_x + self.size,
                                    self.pos_y + 2 * self.size, fill=self.color)


def draw_scene():
    """Clear the current scene and build it up again"""

    # first entirely clear the canvas
    canvas.delete("all")

    # draw the green parks
    canvas.create_rectangle(0, 0, (width - roadWidth) / 2, (height - roadWidth) / 2, fill="green")
    canvas.create_rectangle(0, (height + roadWidth) / 2, (width - roadWidth) / 2, height, fill="green")
    canvas.create_rectangle((width + roadWidth) / 2, 0, width, (height - roadWidth) / 2, fill="green")
    canvas.create_rectangle((width + roadWidth) / 2, (height + roadWidth) / 2, width, height, fill="green")

    # draw the dashed lines on the road
    canvas.create_line(0, height / 2, width, height / 2, fill="white", dash=(20, 20))
    canvas.create_line(width / 2, 0, width / 2, height, fill="white", dash=(20, 20))


def simulate_cars():
    """ iterate forever through cars and draw them """
    while (1 == 1):
        # draw the park scene on the canvas
        draw_scene()

        # add a new car every now and then
        if random.randint(0, 9) > 8:
            newCar = Car();
            cars.append(newCar)

        # draw all cars in the scene
        for car in cars:
            car.move()
            car.draw()

            # remove cars that drove out of the scene
            if (car.pos_x < 0 or car.pos_x > width or car.pos_y < 0 or car.pos_y > height):
                cars.remove(car)

        canvas.update()
        time.sleep(0.01)


if __name__ == '__main__':
    root = Tk()

    # main global variables
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    roadWidth = 200

    #  canvas is a white piece of paper on which you can draw
    canvas = Canvas(root, width=width, height=height, bg="black")
    canvas.pack()

    # list of cars in the scene
    cars = []

    # run the simulation
    simulate_cars()

    # must be the last line before exit for TKinter
    root.mainloop()
