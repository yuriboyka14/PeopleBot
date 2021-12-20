# Setting interpreter
#!/usr/bin/env

import rospy
import catkin_package.msg
import cv2
import imutils
import numpy as np


def talk_to_me():
    pub = rospy.Publisher("talking_topic", catkin_package.msg.Position, queue_size=10)
    rospy.init_node("publisher_node", anonymous=True)
    rate = rospy.Rate(1)   # it has function sleep, we set sleep time to 1s
    rospy.loginfo("Publisher started, now publishing messages")
    while not rospy.is_shutdown():
        msg = catkin_package.msg.Position()

        # wywolanie funkcji odpowiedzialnej za rozpoznanie pileczki
        ball_reco(msg, pub)

        rate.sleep()

def ball_reco(msg, pub):
    cap = cv2.VideoCapture(-1)
    Cx = Cy = radius = 0
    object_detected = False

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, +1)  # Mirror image frame

        if not ret:  # If frame is not read then exit
            break

        font = cv2.FONT_HERSHEY_SIMPLEX  # Font style for writing text on video frame
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        x_half = width / 2
        y_half = height / 2

        redLower = (0, 138, 128)
        redUpper = (180, 255, 255)

        blurred = cv2.GaussianBlur(frame, (11, 11), 0)  # It is useful for removing noise.
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)  # BGR to HSV

        mask = cv2.inRange(hsv, redLower, redUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)  # To remove any small blobs left in the mask

        contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        center = None

        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)  # Find the Center of the ball
            Cx = int(M['m10'] / M['m00'])
            Cy = int(M['m01'] / M['m00'])
            x_coord = Cx - x_half
            y_coord = -(Cy - y_half)
            S = '(X: ' + str(x_coord) + ' Y:' + str(y_coord) + ')'
            cv2.putText(frame, S, (10, 50), font, 1, (0, 0, 0), 2,
                        cv2.LINE_AA)  #(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            # To see the centroid clearly
            if radius > 10:
                cv2.circle(frame, (int(x), int(y)), int(radius), (60, 60, 255),
                           3)  # big circle ((image, center_coordinates, radius, color, thickness))
                cv2.circle(frame, center, 5, (0, 0, 0), -1)  # small circle

        if len(contours) > 0:
            object_detected = True
        else:
            object_detected = False

        T = '(Object on the screen: ' + str(object_detected) + ')'
        cv2.putText(frame, T, (10, 100), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow("Ball tracking", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # msg.x, msg.y, msg.size, msg.found = Cx, Cy, radius, object_detected
        # pub.publish(msg)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        talk_to_me()
    except rospy.ROSInterruptException:
        pass