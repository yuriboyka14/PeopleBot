import rospy
import catkin_package.srv as sv
import catkin_package.msg


def drive_the_robot(lin_x, ang_z):
    rospy.loginfo("Request has been sent.")
    catkin_package.srv.driver.linear_x = lin_x
    catkin_package.srv.driver.angular_z = ang_z

    rospy.init_node("client_node")
    rospy.wait_for_service("driver")
    # rate = rospy.Rate(100)

    try:
        drive_function = rospy.ServiceProxy("driver", catkin_package.srv.driver)
        response = drive_function(lin_x, ang_z)
        rospy.loginfo(response.msg_feedback)
        # rate.sleep()
    except rospy.ServiceException as e:
        print(f"Service call failed {e}")


def image_processing(data):
    if data.detected:
        if data.radius < 35:
            if int(data.x) < 0:
                rospy.loginfo(f"Too much to the left {data.x}")
                drive_the_robot(0.1, -0.2)
            elif int(data.x) > 0:
                rospy.loginfo(f"Too much to the right {data.x}")
                drive_the_robot(0.1, 0.2)
            else:
                rospy.loginfo("Ball is in the center!")
                drive_the_robot(0.5, 0.0)
        else:
            drive_the_robot(0.0, 0.0)
    else:
        drive_the_robot(0.0, 0.2)
        rospy.loginfo("Ball was not detected")


def main_client():
    rospy.init_node("client_node")
    rospy.Subscriber("talking_topic", catkin_package.msg.Position, image_processing) # here we subscribe to our
    rospy.spin()

if __name__ == "__main__":
    main_client()