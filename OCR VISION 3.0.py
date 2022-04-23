import cv2
import pytesseract
from picamera.array import PiRGBArray
from picamera import Picamera
camera = PiCamera()
Camera.resolution=(640,480)
camera.framerate=30
rawCapture=PirgbArray(camera,size=640,480))
for frame in camera.capture_continous(rawCapture,format="bgr",use_video_port=true):
    image=frame.array
    cv2.imshow("frame",image)
    key =cv2.waitkey(l)&0xff

    rawCapture.truncate(0)
    if key == ord("s"):
        text = pytesseract.image_to_dtring(image)
        print(text);
        cv2.imshow("frame",image)
