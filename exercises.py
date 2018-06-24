import datetime as datetime
import math
import time
from tkinter import Tk
from turtle import Canvas

a = 5
print(a)
a += 3  # this is the equivalent for a = a + 3
print(a)
b = 5
print(a + b)

a = int(input("How much?"))
if (a >= 2):
    print("wow that's nice!")
elif (a < 2 and a >= 0):
    print("better improve on it")
else:
    print("oh whatever")

a = 50
while a > 10:
    a -= 1  # this is equivalent to: a = a-1
    print(a)
print("end result: " + str(a))

a = int(input("How much?"))
while a > 10:
    print("That is invalid. Try again")
    a = int(input("How much?"))
print("Good job! End result: " + str(a))

import math


def calculate_distance(x1, y1, x2, y2):
    """This method calculates the distance between two points"""
    dx = x2 - x1
    dy = y2 - y1
    result = math.sqrt(dx ** 2 + dy ** 2)  # dx ** 2 is dx to the power of 2
    return result


# now reuse the method multiple times
print(calculate_distance(0, 0, 3, 4))  # result is 5, the famous 3, 4, 5 triangle
print(calculate_distance(0, 0, 6, 8))  # result is 10, the famous 6, 8, 10 triangle
print(calculate_distance(1, 10, 6, 22))  # result is 13, the famous 5, 12, 13 triangle

divide_by = int(input("Divide by?"))
result = 0
try:
    result = 15 / divide_by
except Exception as e:
    print("Something is wrong with your calculation. Reverting to the default result: ")
    result = 15 / 2
finally:
    print(result)

import random


class Car:
    color = "red"
    max_speed = 0  # in km/h
    velocity = 0  # in km/h
    heading = 0  # in degrees
    traveltime = 0  # in seconds

    def __init__(self):
        """When this class is instantiated, generate some interesting actual random values"""
        self.color = random.choice(["green", "yellow", "white", "blue"])
        self.heading = random.randint(0, 360)
        self.max_speed = random.randint(0, 400)
        self.velocity = random.randint(0, self.max_speed)
        self.traveltime = random.randint(0, 1000)

    def traveled_distance(self):
        """calculates the distance this car traveled given the time and velocity"""
        result = self.velocity * (self.traveltime / 3600)  # in km
        return result

    def print_properties(self):
        print(self.color + " " + str(self.velocity) + "km/h " + str(
            self.heading) + "deg " + str(self.traveled_distance()) + "km")


car1 = Car()
car2 = Car()

car1.print_properties()
car2.print_properties()

numbers = []
for i in range(0, 100, 3):
    print(i)

fruits = ["pear", "banana", "cherry", "orange"]
for x in fruits:
    if x == "cherry":
        break
    if x == "pear":
        continue
    print(x)

fruits = ["pear", "banana", "cherry", "orange"]
print(fruits)
fruits.append("seafruit")
fruits.insert(0, "guava")  # list count starts at 0
fruits.remove("cherry")
print(fruits)
fruits.sort()
fruits.reverse()
print(fruits)
print(fruits[3])  # this is the fourth element in the list
fruits.append("guava")
print((fruits.count("guava")))

cars = []  # create emty list
cars.append(car1)  # add a car to it
cars.append(car2)  # add another car etc
print(cars.__len__())  # amount of cars in the list

# smart way to add a lot of cars
cars = []  # create emty list
while cars.__len__() < 100:
    new_car = Car()
    new_car.print_properties()
    cars.append(new_car)

print(cars.__len__())  # amount of cars in the list


# Draw a Clock
# create the drawing system
root = Tk()

# main dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#  canvas is a white piece of paper on which you can draw
canvas = Canvas(root, width=screen_width, height=screen_height, bg="black")
canvas.pack()


def draw_hand(angle, someradius, some_thinkness, some_color):
    # this function draws a hand with a certain angle and radius
    canvas.create_line(screen_width / 2,  # x1
                       screen_height / 2,  # y1
                       screen_width / 2 + math.cos(angle) * someradius,  # x2
                       screen_height / 2 + math.sin(angle) * someradius,  # y2
                       width=some_thinkness,  # line thickness
                       fill=some_color)  # line color


def draw_clock():
    # draw a clock background
    canvas.create_rectangle(screen_width / 3, screen_height / 3, screen_width * 2 / 3, screen_height * 2 / 3,
                            fill='green')

    # draw the clock itself
    radius = screen_height / 4
    canvas.create_oval(screen_width / 2 - 100, screen_height / 2 - 100, screen_width / 2 + 100, screen_height / 2 + 100,
                       fill="gray")

    # draw all hands
    now = datetime.datetime.now()
    hour_angle = 2 * math.pi * now.hour / 12 - math.pi / 2  # clock zero angle starts at top
    draw_hand(hour_angle, radius / 4, 4, "red")
    minute_angle = 2 * math.pi * now.minute / 60 - math.pi / 2  # clock zero angle starts at top
    draw_hand(minute_angle, radius / 3, 3, "blue")
    seconds_angle = 2 * math.pi * now.second / 60 - math.pi / 2  # clock zero angle starts at top
    draw_hand(seconds_angle, radius / 3, 1, "yellow")


while (1 < 2):  # loop forever
    canvas.delete("all")
    draw_clock()
    canvas.update()
    time.sleep(0.01)

# must be the last line before exit for TKinter
root.mainloop()
