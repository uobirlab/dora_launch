#!/usr/bin/env python
import rospy
from p2os_driver.msg import MotorState

    
pub = rospy.Publisher('/cmd_motor_state', MotorState)
rospy.init_node('enable_motors')
r = rospy.Rate(2) # hz
while not rospy.is_shutdown():
   pub.publish(MotorState(4))
   r.sleep()

