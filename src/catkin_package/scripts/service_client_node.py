import rospy
import catkin_package.srv as sv
import catkin_package.msg


def drive_the_robot(lin_x, ang_z):
    rospy.loginfo("Request has been sent.")
    sv.request.linear_x = lin_x
    sv.request.angular_z = ang_z

    rospy.wait_for_service("driver")
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        try:
            drive_function = rospy.ServiceProxy("driver", sv.driver)
            response = drive_function(lin_x, ang_z)
            rospy.loginfo(response.msg_feedback)
            rate.sleep()
        except rospy.ServiceException as e:
            print(f"Service call failed {e}")


def image_processing(data):  # nie wiem jak z ta kamera i jej ruchem na razie, wiec tu poki co nie podajemy y
    if data.detected:
        if data.size > 10:  # (size is yet to be set)
            if int(data.x) < 0:
                rospy.loginfo("Too much to left")
                drive_the_robot(0.1, 0.5)
            elif int(data.x) > 0:
                rospy.loginfo("Too much to right")
                drive_the_robot(0.1, -0.5)
            else:
                rospy.loginfo("Ball is in center!")
                drive_the_robot(0.5, 0.0)
        else:
            drive_the_robot(0.0, 0.0)
    else:
        drive_the_robot(0.0, 0.1)


def main_client():
    rospy.init_node("client_node")
    rospy.Subscriber("talking_topic", catkin_package.msg.Position, image_processing) # here we subscribe to our
    rospy.spin()                                                                          # cam input publisher


if __name__ == "__main__":
    main_client()