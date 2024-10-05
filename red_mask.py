import cv2
import numpy as np
 
 
# Initialize the webcam
cap = cv2.VideoCapture(0)
 
 
# Allow the camera to warm up
cv2.waitKey(1000)  # Wait for 1 second
 
 
# Read the frame from the webcam
ret, img = cap.read()
 
 
# Check if the frame was captured successfully
if not ret:
    print("Failed to capture image")
else:
    # Flip the frame horizontally
    img = np.flip(img, axis=1)
 
 
    # Convert the color space from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 
 
    # Generate masks to detect red color
    lower_red = np.array([0, 120, 50])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
 
 
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
 
 
    # Combine both masks to cover the full red spectrum
    mask = mask1 + mask2
 
 
    # Show the mask for red color detection
    cv2.imshow("Red Color Mask", mask)
    cv2.waitKey(0)
 
 
# Release the webcam
cap.release()
cv2.destroyAllWindows()