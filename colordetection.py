import cv2
import numpy as np

def nothing(x):
    pass

# Initialize the camera
cap = cv2.VideoCapture(0)
# cap=cv2.imread("Blue.png")
# Create a window
cv2.namedWindow("Tracking")

# Create trackbars for BGR values
cv2.createTrackbar("Lower B", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Lower G", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Lower R", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Upper B", "Tracking", 255, 255, nothing)
cv2.createTrackbar("Upper G", "Tracking", 255, 255, nothing)
cv2.createTrackbar("Upper R", "Tracking", 255, 255, nothing)
#
while True:
# for i in range (100):
    # Capture the frame
    _, frame = cap.read()

    # Get trackbar positions for lower and upper BGR values
    l_b = cv2.getTrackbarPos("Lower B", "Tracking")
    l_g = cv2.getTrackbarPos("Lower G", "Tracking")
    l_r = cv2.getTrackbarPos("Lower R", "Tracking")
    u_b = cv2.getTrackbarPos("Upper B", "Tracking")
    u_g = cv2.getTrackbarPos("Upper G", "Tracking")
    u_r = cv2.getTrackbarPos("Upper R", "Tracking")

    # Define lower and upper color bounds
    lower_bound = np.array([l_b, l_g, l_r])
    upper_bound = np.array([u_b, u_g, u_r])
    # lower_bound = np.array([0, 0, 130])
    # upper_bound = np.array([255, 255, 255])

    # Create a mask for the selected color range
    mask = cv2.inRange(frame, lower_bound, upper_bound)

    # Perform bitwise AND on the original frame and mask to extract the color
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame and the result
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Tracking", result)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy windows
cap.release()
cv2.destroyAllWindows()
# import pyttsx3
# engine=pyttsx3.init()
# engine.say("hello guys , welcome in  ROBOMANTHAN,now you can see new technology of smart automation ,  are  you interested to see this new technology of robomanthan ")
# engine.runAndWait()