# Subsection B2
## Explanation
- Since, in the given data, the potholes all are of white colour and of same shape, I decided to use a blob detector on it
- So the image was resized, blurred, grayscaled, inverted and then thresholded
- Next the image was fed to the blob detector with adjustable parameters (area, circularity, convexity, inertia)
- From this keypoints were obtained and a bounding rectangle was constructed around the keypoints

- This code is the 'pothole_detector.py',when this is run with the corresponding video in the same directory (also the video name in the code needs to be suitably updated, see comments in the code) will diplay the video in the opencv window
- The scripts 'cvtestfinal2.py' and 'imagetovideo.py' were used to save images and create video respectively 
