import cv2
import numpy as np
import pyttsx3

def nothing(x):
    pass

# Initialize the camera
cap = cv2.VideoCapture(0)

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.say("Hello guys, welcome to ROBOMANTHAN. Now you can see the new technology of smart automation. Are you interested to see this new technology of Robomanthan?")
engine.runAndWait()

# Create a window
cv2.namedWindow("Tracking")

# Create trackbars for BGR values
cv2.createTrackbar("Lower B", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Lower G", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Lower R", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Upper B", "Tracking", 255, 255, nothing)
cv2.createTrackbar("Upper G", "Tracking", 255, 255, nothing)
cv2.createTrackbar("Upper R", "Tracking", 255, 255, nothing)

# Previous color state
prev_color_name = ""

def get_color_name(b, g, r):
    """Rough logic to guess the color name based on dominant channel"""
    if r > 150 and g < 100 and b < 100:
        return "Red"
    elif g > 150 and r < 100 and b < 100:
        return "Green"
    elif b > 150 and r < 100 and g < 100:
        return "Blue"
    elif r > 150 and g > 150 and b < 100:
        return "Yellow"
    elif r > 180 and g > 180 and b > 180:
        return "White"
    elif r < 50 and g < 50 and b < 50:
        return "Black"
    else:
        return "Unknown Color"

while True:
    # Capture the frame
    ret, frame = cap.read()
    if not ret:
        break

    # Get trackbar positions for lower and upper BGR values
    l_b = cv2.getTrackbarPos("Lower B", "Tracking")
    l_g = cv2.getTrackbarPos("Lower G", "Tracking")
    l_r = cv2.getTrackbarPos("Lower R", "Tracking")
    u_b = cv2.getTrackbarPos("Upper B", "Tracking")
    u_g = cv2.getTrackbarPos("Upper G", "Tracking")
    u_r = cv2.getTrackbarPos("Upper R", "Tracking")

    # Define lower and upper bounds
    lower_bound = np.array([l_b, l_g, l_r])
    upper_bound = np.array([u_b, u_g, u_r])

    # Create mask and result
    mask = cv2.inRange(frame, lower_bound, upper_bound)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Count number of non-zero pixels to detect presence
    non_zero_count = cv2.countNonZero(mask)
    if non_zero_count > 5000:  # color area is significant
        # Take average color in mask region
        mean_val = cv2.mean(frame, mask=mask)
        b, g, r = int(mean_val[0]), int(mean_val[1]), int(mean_val[2])
        color_name = get_color_name(b, g, r)

        # Speak only if color is new
        if color_name != prev_color_name and color_name != "Unknown Color":
            engine.say(f"{color_name} color detected")
            engine.runAndWait()
            prev_color_name = color_name
    else:
        prev_color_name = ""

    # Show output
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Tracking", result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
