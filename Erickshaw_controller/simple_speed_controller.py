#!/usr/bin/env python

"""
Now to add feedback to the system and give it to (w_gazebo)
Also to add system to determine the acceleration (a)

"""

import rospy
from std_msgs.msg import Float64
#from gazebo_msgs.msg import LinkStates

w_gazebo = 0.1
w=10
s=0.1
i=0

def Acc(a=1):
    # s=w_gazebo
    global s
    global w
#    t=abs(w-w_gazebo)/a
    t=abs(w-s)/a
    T=t*10
#    s=s+(w-w_gazebo)/T
    s=s+(w-s)/T
    f=s
    if f<0.1:
        f=0
    return f

"""
def Callback(msg):
    global w_gazebo
    global i
    if i==0:
        s=w_gazebo
        i=1
    w_gazebo =-(msg.twist[5].angular.y + msg.twist[4].angular.y)/2
    # w_gazebo =-msg.twist[5].angular.y
    # rospy.loginfo(w_gazebo)

"""


if __name__=='__main__':
    rospy.init_node('simple_controller_py', anonymous=True)
    #rospy.Subscriber("gazebo/link_states",LinkStates,Callback)
    pub_wheel= rospy.Publisher("wheel_controller/command",Float64, queue_size=10)
#    pub_right= rospy.Publisher("wheel_right_controller/command", Float64, queue_size=10)
    t=rospy.Rate(10)
    # rospy.spin()
    while not rospy.is_shutdown():
        x=Float64(Acc())
        # x=Float64(0)
        rospy.loginfo("x= {} s= {}".format(x,s))
        pub_wheel.publish(x)
#        pub_right.publish(x)
        t.sleep()
