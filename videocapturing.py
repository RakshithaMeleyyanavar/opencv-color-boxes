import cv2
capture = cv2.VideoCapture(0)    # 0 means internal webcam

while True:
    isTrue, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS) 
    cv2.imshow('Video', frame)  # showing videos # showing videos
    cv2.imshow('Video',gray)
    if cv2.waitKey(20) & 0xFF == 8 :
        break

capture.release()
cv2.destroyAllWindows()

ReadingVideos
by
uploading
path

import cv2

capture = cv2.VideoCapture('Baby dog#cute puppy barking#4kviral#shorts.mp4')  # by videos path

while True:
    isTrue, frame = capture.read()
    cv2.imshow('Video', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
