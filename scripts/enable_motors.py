#!/usr/bin/env python
import rospy
from p2os_driver.msg import MotorState


def enable_motors():
    
    pub = rospy.Publisher('/cmd_motor_state', MotorState, latch=True)
    rospy.init_node('enable_motors')
    pub.publish(MotorState(4))


if __name__ == '__main__':
    try:
        rospy.sleep(10)
        enable_motors()
    except rospy.ROSInterruptException:
        pass
