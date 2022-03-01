#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Joy
from picar_joy_stick.msg import PicarJoy
# from enum import Enum

class PicarJoyMessages():
    MOVE_FORWARD = 1
    MOVE_BACKWARD = 2


controller_type = 'ps4'


ps4 = {
    "SPEED": 4,
    "PAN": 3
}
cntlr = ps4

class JoyStateControl:
    def __init__(self):
        self.threshold = rospy.get_param("~threshold")
        self.prev_joy_cmd = PicarJoy()
        self.pub_joy_cmd = rospy.Publisher("picar_commands/joy_processed", PicarJoy, queue_size=10)
        self.sub_joy_raw = rospy.Subscriber("picar_commands/joy_raw", Joy, self.joy_state_cb)

    def joy_state_cb(self, msg):
        joy_cmd = PicarJoy()

        if msg.axes[cntlr["PAN"]] >= self.threshold:
            joy_cmd.pan_cmd = msg.axes[cntlr["PAN"]] * 45 + 90
        elif msg.axes[cntlr["PAN"]]  <= -self.threshold:
            joy_cmd.pan_cmd = msg.axes[cntlr["PAN"]] * 45 + 90
        if msg.axes[cntlr["SPEED"]] >= self.threshold:
            joy_cmd.speed_cmd = PicarJoyMessages.MOVE_FORWARD
            joy_cmd.speed = 70 * msg.axes[cntlr["SPEED"]]
        elif msg.axes[cntlr["SPEED"]] <= -self.threshold:
            joy_cmd.speed_cmd = PicarJoyMessages.MOVE_BACKWARD
            joy_cmd.speed = 70 * (-msg.axes[cntlr["SPEED"]])
        
        if not (self.prev_joy_cmd.pan_cmd == joy_cmd.pan_cmd and self.prev_joy_cmd.speed_cmd == joy_cmd.speed_cmd):
            self.pub_joy_cmd.publish(joy_cmd)
        self.prev_joy_cmd = joy_cmd

def main():
    rospy.init_node("picar_joy_control")
    controller_type = rospy.get_param("~controller")
    # if(controller_type=='ps4'):
    print("The controller type is", controller_type)
    # cntlr = ps4
    joyState = JoyStateControl()
    rospy.spin()
    

if __name__ == '__main__':
    main()