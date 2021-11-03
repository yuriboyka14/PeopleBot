# Setting interpreter
#!/usr/bin/env

import rospy
import std_msgs.msg
import catkin_package.msg

def callback(data):
    # we refer to string message using data and String has string message
    # inside called 'data'. Hence data.data
    # rospy.loginfo("Received data - " + str(data.data))
    rospy.loginfo(f"{data.message} - X: {data.x} Y: {data.y}")

def listener():
    rospy.init_node("subscriber_node", anonymous=True)
    # whenever new message is received we will call a callback function to which prints messages
    # rospy.Subscriber("talking_topic", std_msgs.msg.String, callback)
    rospy.Subscriber("talking_topic", catkin_package.msg.Position, callback)
    # it allows us to run the node until we shut it down
    rospy.spin()

if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass