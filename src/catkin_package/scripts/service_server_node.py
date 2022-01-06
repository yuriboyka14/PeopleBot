import rospy
import catkin_package.srv as sv
import geometry_msgs.msg.Twist as tw

global motor_command  # this one will be of a type geometry_msgs.msg.Twist but there are no declarations in python...


def callback(request):              # this callback function handles drive requests and displays responses
    rospy.loginfo(f"Drive request received - forward movement: {sv.driver(request.linear_x)}"
                  f", rotate: {sv.driver(request.angular_z)}")

    # setting values of velocities to requested values
    motor_command.linear.x = sv.driver(request.linear_x)
    motor_command.angular.z = sv.driver(request.angular_z)

    pub = rospy.Publisher("cmd_vel", tw, queue_size=10)  # nie jestem pewien czy w callbacku powinien byc publisher
    pub.publish(motor_command)                           # ale ziomek tak mial w repo

    rospy.loginfo(catkin_package.srv.driverResponse(f"Forward linear x: {str(sv.driver(request.linear_x))}\nrotate "
                                                    f"angular z: {sv.driver(request.angular_z)}"))


def main_server():
    rospy.init_node("drive_bot_service")
    rospy.Service("driver", catkin_package.srv.driver, callback)
    rospy.loginfo("Service started successfully.")
    rospy.spin()


if __name__ == "__main__":
    main_server()