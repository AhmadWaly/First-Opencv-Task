import cv2
import numpy as np


events= open("events.txt","w")
camera=cv2.VideoCapture(0)
count =0
while True:
    ret, frame =camera.read()

    key=cv2.waitKey(15)
    if key==82 :
        cv2.imwrite("frame%d.jpg"%count ,frame) #save image as frame(count)
        events.write("frame%d  up\n"% count)
        count+=1
    elif key==81 :
        cv2.imwrite("frame%d.jpg"%count ,frame)
        events.write("frame%d  left\n"% count)
        count+=1
    elif key==83 :
        cv2.imwrite("frame%d.jpg"%count ,frame)
        events.write("frame%d  right\n"% count)
        count+=1
    elif key==84 :
        cv2.imwrite("frame%d.jpg"%count ,frame)
        events.write("frame%d  down\n"% count)
        count+=1
    else :
        cv2.imshow("frame",frame)
        cv2.waitKey(1)


events.close()

camera.release()
cv2.destroyAllWindows()



