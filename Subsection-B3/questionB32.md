## B.3: Literature Review and Theory
### 1. Sensors and navigation stack
#### 1.1 Mapping
These refer to the sensors(both active and passive) that aid in mapping of the environment.

- Camera (visible,infrared) (mono,stereo)
- Ultrasonic sensor
- LiDAR (Light Detection And Ranging)
- Radar (Short-range 24GHz) (Long-range 76GHz)

#### 1.2 Odometry
These refer to the sensors that aid in determining position, velocity and acceleration

- Wheel encoders
- Visual odometry
- IMU (inertial measurement unit)

#### 1.3 Advantages and Disadvantages and Usage
|Sensor|Advantages|Disadvantages|
|----|--------|-----------|
|Cameras|	Color information, high resolution, compact|	Highly dependent on lighting(negatively affected by low light or harsh lighting) and weather(negatively affected by rain and snow)
|Ultrasonic sensor|	Reliable distance data|	Low resolution, limited range|
|LiDAR|	High resolution 3D information, works for long ranges|	High cost, lacks color information
|Radar|	Works independent of weather and lighting condition, compact, provides 3D information|	Low resolution, no color information
|Wheel encoders|	Inexpensive, good short term accuracy|	Prone to position drift and errors|
|Visual odometry|	Reliable, cost effective|	Affected by lighting and weather, computationally expensive|
|IMU|	Dosen't need external refrences after initialization|	Prone to integration drift|


#### 1.4 Sensor fusion
In a realistic scenario, sensors will be prone to errors and subject to noise. Hence there is a need of combining data from various sensors and minimizing the errors. This is achieved by introducing redundancy in the system and by using Kalman filter over the data.

Moreover, fusing data from sensors will allow us to take advantage of various strenghts of each sensor and allow the autonomous system to take better actions.

### 2. Intersection recognition from LiDAR point cloud
In reference to the research paper given in the application.

Link to the paper: https://robotik.informatik.uni-wuerzburg.de/telematics/download/iv2012.pdf

#### 2.1 Explanation of the algorithm

- An algorithm for real-time recongition of intersections is proposed
- First the obtained data is preprocessed to remove vehicles and pedestrians
- This yields a binary image of the scene in bird-eye view
- Now a beam model is launched from a certain **velocity dependent adaptive distance** (D = 5 + vt) as opposed to constant distance in conventional algorithms
- Furthur each **beam is assigned a width** as well as opposed to conventinal algorithms
- Beams are launched for every 1 degree (enumerated 0 to 359)
- Each beam propagates until it either hits an obstacle or it reaches D distance
- The lenghts of all 360 beams are normalized and plotted against the angle
- This yields a 360 dimensional vector, which is then treated as a feature classification problem
- Classifier (Support Vector Machine) is trained using known data and used to recognize unknown scenarios

#### 2.2 Insights/ Results
- From the available information from 10^6 - 10^4 pixels, infromation about 360 pixels is enough to classify an image in this case
- Regarding the graph, minimas correspond to the angular range where there are obstacles
- Whereas, maximas correspond to the angular range where motion is possible
- The assignment of velocity dependent distance to the beam is also logical, in the sense that 
at higher velocity the car will cover greater distances and will therefore need information about a greater amount of area to take decisions

#### 2.3 Suggestions/ Improvements
- In the case there is heavy traffic on the road consisting of buses and trucks as is the case in many cities, data acquisition may become tough as LiDAR will be blocked completely by vehicles
- Perhaps placing the LiDAR below the car maybe helpful as then the rays will pass from under the vehicles and directly detect the curbs
- In roads where curbs are absent, detecting the road type maybe difficult
- This scale of the road is not taken into account during recognition, though this data may not be strictly required to classify the road, the data can be used to determine the dimensions of the road and fed to the navigation stack
- This may be done by taking D itself as a part of the feature as it contains scale and velocity information

**Bonus Question 1 has been solved by implementing the above algorithm in python**