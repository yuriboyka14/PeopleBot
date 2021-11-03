# Setting interpreter
#!/usr/bin/env

import rospy
import std_msgs.msg
import catkin_package.msg



def talk_to_me():
    # pub = rospy.Publisher("talking_topic", std_msgs.msg.String, queue_size=10)
    pub = rospy.Publisher("talking_topic", catkin_package.msg.Position, queue_size=10)
    rospy.init_node("publisher_node", anonymous=True)
    rate = rospy.Rate(1)   # it has function sleep, we set sleep time to 1s
    rospy.loginfo("Publisher started, now publishing messages")
    while not rospy.is_shutdown():
        # msg = "Hello - " + str(rospy.get_time())

        msg = catkin_package.msg.Position()
        msg.message = "My position is: "
        msg.x = 2.0
        msg.y = 1.5

        pub.publish(msg)
        rate.sleep()

if __name__ == "__main__":
    try:
        talk_to_me()
    except rospy.ROSInterruptException:
        pass