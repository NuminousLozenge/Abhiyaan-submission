#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(data.data)
    
def listener():

    rospy.init_node('node2', anonymous=True)
    rospy.Subscriber("team_abhiyaan", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
