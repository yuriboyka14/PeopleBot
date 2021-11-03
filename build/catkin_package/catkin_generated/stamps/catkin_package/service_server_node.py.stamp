import rospy
import catkin_package.srv

def callback(request):
    return catkin_package.srv.multiplierResponse(request.a * request.b)

def multiply():
    rospy.init_node("multiplier_service")
    service = rospy.Service("multiplier", catkin_package.srv.multiplier, callback)
    rospy.loginfo("Service started successfully.")
    rospy.spin()

if __name__ == "__main__":
    multiply()