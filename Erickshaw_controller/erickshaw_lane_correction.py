#!/usr/bin/env python

import rospy as rp 
from std_msgs.msg import Float64

eprev=0
correction=0
def lane_corr(data):
    global eprev
    global correction
    kp=1
    kd=0.001
    val=data.data
    setpoint = 0                   #change this variable to define offset
    e = setpoint - val
    diff=(e-eprev)*10
    correction = kp*e + kd*diff
    

if __name__=="__name__":
    rp.init_node("lane_correction_node",anonymous=True)
    rp.loginfo("Following lane")
    r=rp.Rate(10)
    sub=rp.Subscriber("steering_controller/value/deviation",Float64,lane_corr,queue_size=10)
    pub=rp.Publisher("placeholder",Float64,latch=True,queue_size=10)   #change the name of the topic accordingly
    while not rp.is_shutdown():
        pub.publish(correction)
        r.sleep()
        rp.spin()
