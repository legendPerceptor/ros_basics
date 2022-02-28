#!/usr/bin/env python3

from picar import front_wheels
from picar import back_wheels
import time
import picar
import random

class Picar():

    def __init__(self):
        self.fw = front_wheels.Front_Wheels(db='config')
        self.bw = back_wheels.Back_Wheels(db='config')

    def turn_left(self):
        self.fw.turn_left()

    def turn_right(self):
        self.fw.turn_right()

    def turn(self, angle):
        self.fw.turn(angle)

    def turn_straight(self):
        self.fw.turn_straight()

    def move_forward(self, speed=70):
        self.bw.speed = speed
        self.bw.forward()

    def move_backward(self, speed=70):
        self.bw.speed = speed
        self.bw.backward()
    
    def stop(self):
        self.bw.stop()
        self.fw.turn_straight()
    
