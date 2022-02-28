#include <ros/ros.h>
#include <rospy_tutorials/AddTwoInts.h>

int main(int argc, char **argv) {
    ros::init(argc, argv, "add_two_ints_client");
    ros::NodeHandle nh;
    ros::ServiceClient client = nh.serviceClient<rospy_tutorials::AddTwoInts>("/add_two_ints");
    rospy_tutorials::AddTwoInts srv;
    std::cout<<"a=";
    float a, b;
    std::cin >> a;
    srv.request.a = a;
    std::cout<<"b=";
    std::cin >> b;
    srv.request.b = b;
    if(client.call(srv)){
        // process data
        ROS_INFO("Returned sum is %d", (int)srv.response.sum);
    }else{
        ROS_WARN("The service call is unsuccessful!");
    }
}