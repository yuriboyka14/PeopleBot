import rospy
import catkin_package.srv as sv
import catkin_pkg.msg.Position as pos


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


def image_processing(x, r, detected):  # nie wiem jak z ta kamera i jej ruchem na razie, wiec tu poki co nie podajemy y
    if detected:
        if r > 10:  # (size is yet to be set)
            if x < 500:  # (value yet to be set as well)
                rospy.loginfo("Too much to left")
                drive_the_robot(0.1, 0.5)
            elif x > 500:
                rospy.loginfo("Too much to right")
                drive_the_robot(0.1, -0.5)
            elif x == 500:
                rospy.loginfo("Ball is in center!")
                drive_the_robot(0.5, 0.0)
        else:
            drive_the_robot(0.0, 0.0)
    else:
        drive_the_robot(0.0, 0.1)


def main_client():
    rospy.init_node("client_node")
    rospy.Subscriber("talking_topic", pos, image_processing(pos.x, pos.size, pos.found))  # here we subscribe to our
    rospy.spin()                                                                          # cam input publisher



if __name__ == "__main__":
    main_client()