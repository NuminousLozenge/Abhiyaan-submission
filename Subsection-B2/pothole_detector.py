import cv2
import numpy as np


def rescaleFrame(frame, scale = 0.75):   # function to resize images to fit screen
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    
    dimensions = (width,height)
    
    return cv2.resize(frame, dimensions, interpolation = cv2.INTER_AREA)

 
capture = cv2.VideoCapture('bolt_test_pothole.mp4')   #insert the video here


while True:
    isTrue, frame = capture.read()                       # reading individual frame
    frame_resized = rescaleFrame(frame)                  # resize
    blur = cv2.GaussianBlur(frame_resized, (7,7), cv2.BORDER_DEFAULT) # blur image to improve detection
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)        # convert to grayscale for thresholding image
    ret, thresh = cv2.threshold(gray, 125,255, cv2.THRESH_BINARY_INV) # thresholding and inverting image as
    
    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 125
    params.maxThreshold = 175

    # Filter by Area.
    params.filterByArea = True
    params.minArea = 627

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

    # Detect blobs and create keypoints
    keypoints = detector.detect(thresh)
    
    #Extract size and location(x,y) from keypoints
    size = [key_point.size for key_point in keypoints]
    pts = [key_point.pt for key_point in keypoints]
    
    # from the keypoints contruct a bounding rectangle
    for i in range(len(pts)):
        cv2.rectangle(frame_resized, (int(pts[i][0]-size[i]),int(pts[i][1]-size[i]*0.4)), (int(pts[i][0]+size[i]),int(pts[i][1]+size[i]*0.4)), (0, 255, 0), 2)
                
    # Display the output image
    cv2.imshow('Output',frame_resized) 
    
    if cv2.waitKey(20) & 0xFF == ord('d'):       #stop animation if 'd' is pressed
        break
        
capture.release()
cv2.destroyAllWindows()
       
cv2.waitKey(0)