# Setting interpreter
#!/usr/bin/env

import rospy
import std_msgs.msg
import catkin_package.msg

def search_process(data):
    if not data.found:
        # rotate the robot and camera

def listener():
    rospy.init_node("subscriber_node", anonymous=True)
    # whenever new message is received we will call a callback function to which prints messages
    # rospy.Subscriber("talking_topic", std_msgs.msg.String, callback)
    rospy.Subscriber("talking_topic", catkin_package.msg.Position, search_process)
    # it allows us to run the node until we shut it down
    rospy.spin()

if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass