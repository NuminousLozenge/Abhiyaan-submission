#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

X1 = 4
Y1 = 0

def solver(Va,ra,G,m1,m2):
	a = 1 + (Y1/X1)**2
	b = 2*(Va)*ra*Y1/(X1**2)
	c = (Va**2)*((ra**2/X1**2)-1) + (2*G*m2/(X1**2+Y1**2)**0.5) - (2*G*m2/ra)
	
	V1x = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
	V1y = (Va*ra + Y1*V1x)/X1
	
	V2x = m1*V1x/m2
	V2y = m1*V1y/m2
	return [V1x,V1y,V2x,V2y]




def callback(Pose):
    global X1
    global Y1    
    X1 = Pose.x - 5.544444561004639
    Y1 = Pose.y - 5.544444561004639
    rospy.loginfo(X1)

 
def turtle_circle():

    rospy.Subscriber('/turtle1/pose',Pose, callback)

    rospy.init_node('turtlesim', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel',
                          Twist, queue_size=10)
    rate = rospy.Rate(10)
    vel = Twist()
    while not rospy.is_shutdown():
        solved  = solver(3,4,72,1,1)	 	 
        vel.linear.x = 1
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 1

        rospy.loginfo("X1 = %f",X1)
        rospy.loginfo("Y1 = %f",Y1)
        pub.publish(vel)
        rate.sleep()
        

 
 
if __name__ == '__main__':
    try:
        turtle_circle()
    except rospy.ROSInterruptException:
        pass
        
        
        
        
        
        
        
        
        
'''
rosservice call /kill "turtle1"
rosservice call /spawn 9.544444561004639 5.544444561004639 0 "turtle1"
rosrun abhiyaan_package turtle_circle_code.py


'''
