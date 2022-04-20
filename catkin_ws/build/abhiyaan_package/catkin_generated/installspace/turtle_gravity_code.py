#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


'''
copy paste below commands in terminal
after the command
rosrun turtlesim turtlesim_node
'''

'''
rosservice call /kill "turtle1"
rosservice call /kill "turtle2"
rosservice call /clear
rosservice call /spawn 8.544444561004639 5.544444561004639 0 "turtle1"
rosservice call /spawn 2.544444561004639 5.544444561004639 0 "turtle2"
rosrun abhiyaan_package turtle_gravity_code.py
''' 


def callback(Pose): # callback function for turtle1
    global X1
    global Y1    
    X1 = Pose.x - 5.544444561004639  #shifting origin to centre of window
    Y1 = Pose.y - 5.544444561004639
    #rospy.loginfo(X1)

def callback2(Pose): # callback function for turtle2
    global X2
    global Y2    
    X2 = Pose.x - 5.544444561004639
    Y2 = Pose.y - 5.544444561004639
    #rospy.loginfo(X2)


 
def turtle_gravity():

	rospy.Subscriber('/turtle1/pose',Pose, callback)
	rospy.Subscriber('/turtle2/pose',Pose, callback2)

	rospy.init_node('turtlesim_gravity', anonymous=True)

	pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
	pub2 = rospy.Publisher('/turtle2/cmd_vel',Twist, queue_size=10)    

	rate = rospy.Rate(200)
	vel = Twist()
	vel2 = Twist()
	
	V1X = 0
	V2X = 0
	V1Y = 0.89
	V2Y = -0.89
	c = 0
	
	while not rospy.is_shutdown():

		m1 = 1 #constants
		m2 = 1
		G  = 40 
		dt = 0.001 # small time for numerical integration

		# applying newtoninan gravity and writing components for force
		r = ((X2-X1)**2 + (Y2-Y1)**2 )**0.5
		F = G*m1*m2/(r**2)
		sint = (Y1-Y2)/r
		cost = (X1-X2)/r
		Fx = F*cost
		Fy = F*sint


		# assuming uniform acceleration for small time dt
		V1X += -Fx*dt/m1
		V1Y += -Fy*dt/m1 
		V2X += Fx*dt/m2
		V2Y += Fy*dt/m2    
		
		#modifying velocities of turtle1     	 
		vel.linear.x = V1X
		vel.linear.y = V1Y
		vel.linear.z = 0
		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 0


		#modifying velocities of turtle2 
		vel2.linear.x = V2X
		vel2.linear.y = V2Y
		vel2.linear.z = 0
		vel2.angular.x = 0
		vel2.angular.y = 0
		vel2.angular.z = 0
		


		#rospy.loginfo("X1 = %f",X1)
		#rospy.loginfo("Y1 = %f",Y1)
		#rospy.loginfo("X2 = %f",X2)
		#rospy.loginfo("Y2 = %f",Y2)
					
			
		pub.publish(vel)
		pub2.publish(vel2)
		rate.sleep()


 
 
if __name__ == '__main__':
    try:
        turtle_gravity()
    except rospy.ROSInterruptException:
        pass
               
        

