import cv2


out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 24, (811,668))

for i in range(0,405):
    a = cv2.imread(f'scenario_final_img{i}.png')
    out.write(a)
    
    
out.release()
    