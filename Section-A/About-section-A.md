## Section A
### Task 1
- Ubuntu 20.04 was setup in computer
- ROS Noetic was installed

### Task 2
- Catkin workspace was created 
- The script for the 3 required nodes can be found in catkin_ws/src/abhiyaan_package/scripts
- Named as node1_code.py  node2_code.py  node3_code.py
- Required launch file can be found in catkin_ws/src/abhiyaan_package/Launch
- Named as node1_2.launch

### Task 3
- Required script for the node can be found in catkin_ws/src/abhiyaan_package/scripts
- Named as turtle_gravity_code.py
- Before running the node, however the initial conditions must be setup hence, please copy paste the following


'''

rosservice call /kill "turtle1"

rosservice call /kill "turtle2"

rosservice call /clear

rosservice call /spawn 8.544444561004639 5.544444561004639 0 "turtle1"

rosservice call /spawn 2.544444561004639 5.544444561004639 0 "turtle2"

rosrun abhiyaan_package turtle_gravity_code.py

'''

