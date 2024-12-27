import cv2
import time
import os

def startvideo():
   videoName = '3.MP4'

   # Create a videoCapture Object (this allows reading frames one by one)
   video = cv2.VideoCapture(videoName)

   # Check if it's ok
   if video.isOpened():
       print('Video successfully opened')
   else:
       print('Something went wrong; check if the video name and path are correct')

   # Define a scale level for visualization
   scaleLevel = 2  # It means reduce the size to 2**(scaleLevel-1)

   windowName = 'Video Reproducer'
   cv2.namedWindow(windowName)


# Let's reproduce the video
   while True:
       ret, frame = video.read()  # Read a single frame
       if not ret:  # This means it could not read the frame
           print("Could not read the frame")
           time.sleep(2)
           cv2.destroyWindow(windowName)
           break

       reescaled_frame = frame
       for i in range(scaleLevel - 1):
           reescaled_frame = cv2.pyrDown(reescaled_frame)

       cv2.imshow(windowName, reescaled_frame)

       waitKey = (cv2.waitKey(1) & 0xFF)
       if waitKey == ord('q'):  # If 'Q' pressed, close the video
           print("Closing video and exiting")
           cv2.destroyWindow(windowName)
           video.release()
           break
   print("Fertig")
