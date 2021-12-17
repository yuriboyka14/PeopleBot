# Setting interpreter
#!/usr/bin/env

import rospy
import std_msgs.msg
import catkin_package.msg
from ball_recognition import ball_recognition


def talk_to_me():
    # pub = rospy.Publisher("talking_topic", std_msgs.msg.String, queue_size=10)
    pub = rospy.Publisher("talking_topic", catkin_package.msg.Position, queue_size=10)
    rospy.init_node("publisher_node", anonymous=True)
    rate = rospy.Rate(1)   # it has function sleep, we set sleep time to 1s
    rospy.loginfo("Publisher started, now publishing messages")
    while not rospy.is_shutdown():
        msg = catkin_package.msg.Position()
        # wywolanie funkcji odpowiedzialnej za rozpoznanie pileczki, funkcja powinna zwracac liste [x, y, size]
        msg.x, msg.y, msg.size, msg.found = ball_recognition()

        # logika dla sprawdzenia czy algorytm znalazl pileczke, ustawienie msg.found = True/False

        pub.publish(msg)
        rate.sleep()

if __name__ == "__main__":
    try:
        talk_to_me()
    except rospy.ROSInterruptException:
        pass