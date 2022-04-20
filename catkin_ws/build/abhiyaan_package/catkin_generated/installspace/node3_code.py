#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

Data = ""
pub = rospy.Publisher('naayihba_maet', String, queue_size=10)


def reverse(text):
	reverse_text = ""
	n = len(text)
	
	for i in range(n):
		reverse_text += text[n-i-1]

	return reverse_text
	
def reverse_words(text):
	reverse_words_final = ""
	word_list = text.split(" ")
	m = len(word_list)
	for i in range(m):
		if (i != m-1):
			reverse_words_final += str(word_list[m-i-1]) + " "
		else:
			reverse_words_final += str(word_list[m-i-1])
	return reverse_words_final

def callback(data):
	
    global Data
    Data = reverse_words(reverse(data.data))
    rospy.loginfo(Data)

       
def listener():

    rospy.init_node('node3', anonymous=True)
    rospy.Subscriber("team_abhiyaan", String, callback)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
	    pub.publish(Data)
	    rate.sleep()

if __name__ == '__main__':
    listener()    
