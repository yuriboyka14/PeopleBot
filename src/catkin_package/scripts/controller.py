# Setting interpreter
#!/usr/bin/env

# This node controls the flow of operation, it decides whether it should search or follow the ball based on input data.

import rospy
import std_msgs.msg
import catkin_package.msg
from move_functions import movement, search_process

# -------------SEARCH OR FOLLOW------#


def follow(data):
    if data.found:
        return True
    else:
        return False


def listener():
    rospy.init_node("subscriber_node", anonymous=True)
    # whenever new message is received we will call a callback function to which prints messages
    # rospy.Subscriber("talking_topic", std_msgs.msg.String, callback)
    if follow:
        rospy.Subscriber("talking_topic", catkin_package.msg.Position, movement)
    else:
        rospy.Subscriber("talking_topic", catkin_package.msg.Position, search_process)
    # it allows us to run the node until we shut it down
    rospy.spin()


if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass