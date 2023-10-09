# VISION 3.0
Problem Statement:

People who are blind have difficulties moving around, reading text, and recognizing objects.
White canes and assistive technologies to detect proximities are available on the market, but they don't help in identifying the object.
1.4 million blind children in the world. At least 200,000 children in India have severe visual impairment or blindness. 
People who are blind can read only Braille text and Braille is not available everywhere they go.

Solution:

This project is an object recognition, text recognition and proximity detection to aid the visually impaired people. 
This device can be utilized by any adult or child unless the person is not deaf. 
With the press of the 1st button, the person can detect any object and hear it as audio, with the press of the 2nd button, the person can recognize text and hear the text. 
At other times the device is on standby to avoid unwanted recognition and confusion. 
But, the proximity detection stay’s on the whole time when the device is powered on. 
Audio output is to be given in the user’s preferred regional language. 

# Python Script Documentation

## Overview

This Python script captures continuous video frames from a Raspberry Pi camera, displays them in real-time, and extracts text from the current frame when the "s" key is pressed using Tesseract OCR.

## Required Libraries

- **cv2 (OpenCV)**: Used for capturing video frames from the camera and displaying them.
- **pytesseract**: An OCR tool for Python using the Tesseract-OCR engine to extract text from images.
- **PiRGBArray**: A class from the `picamera` module that provides a 3-dimensional RGB array from the camera output.
- **PiCamera**: A class from the `picamera` module that provides an interface to the Raspberry Pi camera.

## Code Description

1. **Imports**: Import necessary libraries.

```python
import cv2
import pytesseract
from picamera.array import PiRGBArray
from picamera import PiCamera
```

2. **Camera Setup**: Initialize the camera, set resolution and framerate.

```python
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
```

3. **Capture Setup**: Create an instance of `PiRGBArray` to store the frames.

```python
rawCapture = PiRGBArray(camera, size=(640, 480))
```

4. **Capture Loop**: Continuously capture frames from the camera.

```python
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    cv2.imshow("frame", image)
```

5. **Text Extraction**: When the 's' key is pressed, extract text using Tesseract OCR and print it.

```python
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    
    if key == ord("s"):
        text = pytesseract.image_to_string(image)
        print(text)
```

6. **Display**: Display the captured frames.

```python
        cv2.imshow("frame", image)
```

## Example Usage

To run this script, you would need a Raspberry Pi with a camera module. Install the required libraries if not already installed:

```bash
pip install opencv-python-headless
pip install pytesseract
```

Then, run the script:

```bash
python script_name.py
```

Press the "s" key when you want to extract text from the current frame, and the text will be printed to the console.

## Applications

This script can be used in a variety of applications, including:

1. **License Plate Recognition**: Extract license plate numbers from vehicles.
2. **Document Scanning**: Extract text from scanned documents or images.
3. **Signboard Translation**: Translate text from signboards in real-time.
4. **Inventory Management**: Read barcodes or product information for inventory management.
5. **Attendance Systems**: Extract student or employee IDs from ID cards for attendance tracking.
6. **Event Ticketing Systems**: Read ticket information for entry validation.
7. **Robotic Vision**: Enable robots to read and understand text in their environment.
