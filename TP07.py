#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html
# A simple static factory method.
import sys
class Shape(object):
    pass

class Circle(Shape):
    def draw(self): print("Circle.draw")
    def erase(self): print("Circle.erase")

class Square(Shape):
    def draw(self): print("Square.draw")
    def erase(self): print("Square.erase")

class Tringle(Shape):
    def draw(self): print("Tringle.draw")
    def erase(self): print("Tringle.erase")

class Rectangle(Shape):
    def draw(self): print("Rectangle.draw")
    def erase(self): print("Rectangle.erase")

if __name__ == "__main__":
    for type in ("Circle", "Square" ,"Circle", "Square","Tringle","Tringle","Rectangle","Rectangle"):
        if type == "Circle":
            shape = Circle()
        elif type == "Square":
            shape = Square()
        elif type == "Tringle":
            shape = Tringle()
        elif type == "Rectangle":
            shape = Rectangle()
        else:
            print("Bad shape creation: " + type)
            #sys.exit()
        shape.draw()
        shape.erase()