#!/usr/bin/env python3
import rospy

from tutorial.srv import AddTwoInts


def handle_add_two_ints(req):
    result = req.a + req.b
    rospy.loginfo(f"Sum of {req.a} and {req.b} : {result}")
    return result

if __name__ == '__main__':
    rospy.init_node("add_two_ints_server")
    rospy.loginfo("Add two ints server node created")

    service = rospy.Service("/add_two_ints", AddTwoInts, handle_add_two_ints)
    rospy.loginfo("Service server has been started")
    rospy.spin()
    