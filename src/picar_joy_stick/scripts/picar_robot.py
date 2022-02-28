#!/usr/bin/env python3
import copy
import rospy
import threading
from picar_joy_stick.msg import PicarJoy
from picar_joy_stick import Picar
from picar_joy_stick import PicarJoyMessages

class PicarRobot(object):
    def __init__(self):
        self.current_loop_rate = 25
        self.rate = rospy.Rate(self.current_loop_rate)
        self.joy_msg = PicarJoy()
        self.joy_mutex = threading.Lock()
        self.picar = Picar()
        self.angle = 90
        self.angle_step = 5
        rospy.Subscriber("picar_commands/joy_processed", PicarJoy, self.joy_control_cb)


    def joy_control_cb(self, msg):
        with self.joy_mutex:
            self.joy_msg = copy.deepcopy(self.msg)
        
    def controller(self):

        with self.joy_mutex:
            msg = copy.deepcopy(self.joy_msg)
        
        if msg.pan_cmd !=0:
            self.angle = msg.pan_cmd
            if self.angle > 135:
                self.angle = 135
            if self.angle < 45:
                self.angle = 45
            self.picar.turn(self.angle)
        else:
            self.picar.turn_straight()
            self.angle = 90
        
        if msg.speed_cmd != 0:
            if (msg.speed_cmd == PicarJoyMessages.MOVE_FORWARD):
                self.picar.move_forward(msg.speed)
            elif (msg.tilt_cmd == PicarJoyMessages.MOVE_BACKWARD):
                self.picar.move_backward(msg.speed)
        else:
            self.picar.stop()

def main():
    rospy.init_node("picar_robot")
    picar = PicarRobot()
    while not rospy.is_shutdown():
        picar.controller()
        picar.rate.sleep()

if __name__ == '__main__':
    main()