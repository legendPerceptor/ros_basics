#include <ros/ros.h>
#include<std_msgs/String.h>
#include <iostream>
#include <string>

int main(int argc, char** argv) {
    ros::init(argc, argv, "robot_news_radio");
    ros::NodeHandle nh;
    ros::Publisher pub = nh.advertise<std_msgs::String>("/robot_news_radio", 10);
    double publish_frequency;
    std::string msg_to_publish;
    nh.getParam("/number_publish_frequency", publish_frequency);
    nh.getParam("/msg_to_publish", msg_to_publish);
    ros::Rate rate(publish_frequency);
    while(ros::ok()) {
        std_msgs::String msg;
        msg.data = msg_to_publish;
        pub.publish(msg);
        std::cout << msg.data<<std::endl;
        rate.sleep();
    }
    return 0;
}