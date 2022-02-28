#!/usr/bin/env python3

import rospy
from tutorial.msg import HardwareStatus

if __name__ == '__main__':
    rospy.init_node("hardware_status_publisher")
    pub = rospy.Publisher("/my_robot/hardware_status", HardwareStatus, queue_size=10)
    publish_frequency = rospy.get_param("/number_publish_frequency")
    rate = rospy.Rate(publish_frequency)
    temperature = rospy.get_param("/temperature")
    while not rospy.is_shutdown():
        mymsg = HardwareStatus()
        mymsg.temperature = temperature
        mymsg.are_motors_up = True
        mymsg.debug_message = "Everything is running well"
        pub.publish(mymsg)
        rate.sleep()

