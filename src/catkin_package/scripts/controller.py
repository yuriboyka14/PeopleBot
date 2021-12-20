# Setting interpreter
#!/usr/bin/env

import rospy
import std_msgs.msg
import catkin_package.msg

#--------------FOLLOW----------#

def robot_rot_movement(x):
    if x < 0:
        # rotate to left
    else:
        # rotate to right

def robot_lin_movement(size):

    SIZE_TO_OBTAIN = 20 # tu bedzie jakis tam sobie rozmiar ktory pileczka bedzie miala na 1m

    if size < SIZE_TO_OBTAIN:
        # move forward
    else:
        # move backwards

def camera_movement(y):
    if y < 0:
        # move up
    else:
        # move down

def movement(data):
    print(f"X:{data.x}, Y:{data.y}, radius:{data.size}, obj. found:{data.found}")
    # if data.found:
    #     robot_rot_movement(data.x)
    #     robot_lin_movement(data.size)
    #     camera_movement(data.y)

#--------------SEARCH----------#

def search_process():
    # rotate the robot and camera

#-------------SEARCH OR FOLLOW------#

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