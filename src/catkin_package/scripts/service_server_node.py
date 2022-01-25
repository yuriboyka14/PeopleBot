import rospy
import catkin_package.srv
from geometry_msgs.msg import Twist


# this callback function handles drive requests and displays responses
def callback(request):
    rospy.loginfo(f"Drive request received")
    motor_command = Twist()

    # setting values of velocities to requested values
    motor_command.linear.x = request.linear_x
    motor_command.angular.z = request.angular_z

    pub = rospy.Publisher("/RosAria/cmd_vel", Twist, queue_size=10)
    # rate = rospy.Rate(1)

    pub.publish(motor_command)

    # not sure if it should be in the loop
    # while not rospy.is_shutdown():
    #     pub.publish(motor_command)
    #     rate.sleep()

    return catkin_package.srv.driverResponse(f"Forward linear x: {str(request.linear_x)}\nrotate "
                                                    f"angular z: {request.angular_z}")


def main_server():
    rospy.init_node("drive_bot_service")
    service = rospy.Service("driver", catkin_package.srv.driver, callback)
    rospy.loginfo("Service started successfully.")
    rospy.spin()


if __name__ == "__main__":
    main_server()