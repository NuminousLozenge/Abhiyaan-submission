import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (9.8,3.53)

def rescaleFrame(frame, scale = 0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    
    dimensions = (width,height)
    
    return cv2.resize(frame, dimensions, interpolation = cv2.INTER_AREA)



name = 'scenario'
raw_data = cv2.imread(name+'.png') #read image here
raw_data = rescaleFrame(raw_data)
data = cv2.cvtColor(raw_data, cv2.COLOR_BGR2GRAY) #convert to grayscale
final = raw_data.copy()


launchpt = [data.shape[1]//2,data.shape[0]//2]  #input x y here

vel = 10  #(in m/s) assuming the scale of the image is 
t = 1 #(in s)
D = (5 + vel*t)*15  #in pixels   D = 5 + vel*t in m

# color = image[y,x]

def dist(x1,y1,x2,y2):
    return (((x1-x2)**2) + ((y1-y2)**2))**0.5

def ray(launchpt,theta,D,image):
    
    sint = np.sin(theta*(np.pi)/180)  #sin(theta)
    cost = np.cos(theta*(np.pi)/180)  #cos(theta)
    
    dl = 1   #increment in lenght
    l = 0    #lenght of ray in pixels
    x1 = launchpt[0]
    y1 = launchpt[1]
    
    x2 = launchpt[0]
    y2 = launchpt[1]
    
    color = 255
    
    while(((color == 255) and dist(x1,y1,x2,y2)<=D) and (x2<image.shape[1]-1) and (y2<image.shape[0]-1)):
        x2 = int(x1 + l*cost)
        y2 = int(y1 + l*sint)
        l += dl
        
        if(x2>image.shape[1]-1 or y2>image.shape[0]-1):
            color = 255      
        else:
            color = image[y2,x2] 
               
    return (x2,y2,dist(x1,y1,x2,y2)/D)
    
    #returns point of collision with obstacle or bounding edge
    #and also the normalized distance of line
    
for i in range(1,1601,2):
    feature = [0 for j in range(360)]
    lenght_distribution = [0 for j in range(360)]
    final = raw_data.copy()


    for angle in range(360):
        feature[angle] = ray([i,launchpt[1]],angle,D,data)
        cv2.line(final,(i,launchpt[1]),(feature[angle][0],feature[angle][1]),(0,255,0),1 )
        lenght_distribution[angle] = feature[angle][2]

    plt.plot(lenght_distribution,'.',color = 'lightblue')
    plt.savefig(f'{name}_final_plot{i//2}.png', bbox_inches = 'tight')
    plt.clf()
    plotted = cv2.imread(f'{name}_final_plot{i//2}.png')
    vis = np.concatenate((final,plotted), axis=0)
    cv2.imwrite(f'{name}_final_img{i//2}.png',vis)    

cv2.waitKey(0)