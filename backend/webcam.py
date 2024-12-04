#This is a python script that opens a webcam preview and allows the user
#to take a picture of the webcam preview with a self timer

#---CONTROLS---
#Space-Capture image 
#ESC-close the program

import cv2
import time
import threading

cam = cv2.VideoCapture(0)
username = input("Please enter your name: ")
picture_saved_event = threading.Event()

def take_picture(username, frame) :
    img_name = "{}'s fit.jpg".format(username)
    print ("Taking picture in...")
    for x in range(10):
        print (10-x)
        time.sleep(1)
    cv2.imwrite(img_name, frame)
    print("{} saved".format(img_name))
    picture_saved_event.set()

while True:
    ret, frame = cam.read()
    if not ret:
        print("frame capture failed")
        break

    cv2.imshow("HEATCHECK", frame)
    k = cv2.waitKey(1)

    if k%256 == 27:
    # ESC pressed
        print("closing program...")
        break

    elif k%256 == 32:
        pic_t = threading.Thread(target=take_picture, args=(username, frame))
        pic_t.start()

    if picture_saved_event.is_set():
        break

cam.release()
cv2.destroyAllWindows()
