import cv2
import numpy as np

capture = cv2.VideoCapture('bolt_test_pothole.mp4')
count  = 0

while True:
    isTrue, frame = capture.read()
    
    blur = cv2.GaussianBlur(frame, (7,7), cv2.BORDER_DEFAULT)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 125,255, cv2.THRESH_BINARY_INV)
    
    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 125
    params.maxThreshold = 175

    # Filter by Area.
    params.filterByArea = True
    params.minArea = int(627*(1/0.75)*(1/0.75))

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.4

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.9

    # Filter by Inertia
    params.filterByInertia = True
    params.minInertiaRatio = 0.01

    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs.
    keypoints = detector.detect(thresh)
    
    #Extract size and location(x,y) from keypoints
    size = [key_point.size for key_point in keypoints]
    pts = [key_point.pt for key_point in keypoints]
    
    
    
          
    for i in range(len(pts)):
        cv2.rectangle(frame, (int(pts[i][0]-size[i]),int(pts[i][1]-size[i]*0.4)), (int(pts[i][0]+size[i]),int(pts[i][1]+size[i]*0.4)), (0, 255, 0), 2)
    
    out = frame.copy()

    
    while isTrue:
        cv2.imwrite("frame%d.jpg" % count, out)     # save frame as JPEG file      
        success,image = capture.read()
        print('Read a new frame: ', success)
        count += 1
        break
    
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break
        
capture.release()
cv2.destroyAllWindows()
       
