import rospy
import std_msgs.msg
import catkin_package.msg

# Here are the functions which we provide the controller with to perform action. Yet to be implemented.

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