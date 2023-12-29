#!/usr/bin/env python

"""
This code transfers data from Jetson nano to arduino as struct messages

"""


from pySerialTransfer import pySerialTransfer as txfer
import rospy
from std_msgs.msg import Int16

x=0

def Callback(data):
    global x
    x = data.data

class struct():
    
    def __init__(self,servo=0):
        self.servo=servo


if __name__=="__main__":
    rospy.init_node('arduino_serial_transfer',anonymous=True)
    rospy.Subscriber('/wheel_controller/command',Int16,Callback)
    t=rospy.Rate(20)
    message=struct()
    link = txfer.SerialTransfer('/dev/ttyACM0')
    link.open()
    rospy.sleep(5)
    while not rospy.is_shutdown():
        sendSize=0
        rospy.loginfo(x)
        message.servo=x
        sendSize=link.tx_obj(message.servo, start_pos=sendSize)
        link.send(sendSize)
        t.sleep()
