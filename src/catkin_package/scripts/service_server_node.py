import rospy
import catkin_package.srv as sv
from geometry_msgs.msg import Twist


# this callback function handles drive requests and displays responses
def callback(request):
    rospy.loginfo(f"Drive request received")
    motor_command = Twist()

    # setting values of velocities to requested values
    motor_command.linear.x = sv.driver(request.linear_x)
    motor_command.angular.z = sv.driver(request.angular_z)

    pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(1)

    pub.publish(motor_command)

    # not sure if it should be in the loop
    # while not rospy.is_shutdown():
    #     pub.publish(motor_command)
    #     rate.sleep()

    rospy.loginfo(sv.driverResponse(f"Forward linear x: {str(sv.driver(request.linear_x))}\nrotate "
                                                    f"angular z: {sv.driver(request.angular_z)}"))


def main_server():
    rospy.init_node("drive_bot_service")
    rospy.Service("driver", sv.driver, callback)
    rospy.loginfo("Service started successfully.")
    rospy.spin()


if __name__ == "__main__":
    main_server()