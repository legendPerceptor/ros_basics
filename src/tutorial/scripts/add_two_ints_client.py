#!/usr/bin/env python3
import rospy
from tutorial.srv import AddTwoInts

if __name__ == '__main__':
    rospy.init_node("add_two_ints_client")
    rospy.wait_for_service("/add_two_ints")
    try:
        add_two_ints = rospy.ServiceProxy("/add_two_ints", AddTwoInts)
        a = int(input("a="))
        b = int(input("b="))
        response = add_two_ints(a,b)
        rospy.loginfo(f"Sum is {response.sum}")
    except rospy.rospy.ServiceException as e:
        rospy.logwarn(f"Service failed: {e}")
    
