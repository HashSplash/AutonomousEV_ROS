#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

if __name__=="__main__":
    rospy.init_node('camera_publisher_node', anonymous=True)
    pub = rospy.Publisher('/image_raw',Image,queue_size=60)
    rate = rospy.Rate(10)
    vid=cv2.VideoCapture(0)
    bridgeObject=CvBridge()
    
    while not rospy.is_shutdown():
        returnVal, Frame = vid.read()
        if returnVal==True:
            rospy.loginfo('recieved')
            cv2.imshow('Frame',Frame)
            image=bridgeObject.cv2_to_imgmsg(Frame)
            pub.publish(image)
        rate.sleep()
    vid.release()
    cv2.destroyAllWindows()
    rospy.loginfo('deleted')
