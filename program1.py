import cv2
import queue

# Define the queue object that will hold the frames from the camera
frame_queue = queue.Queue(maxsize=2)

# Open the camera feed
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    if not ret:
        break
    # Put the frame in the queue for processing
    frame_queue.put(frame)
    # Display the frame
    cv2.imshow('Program 1', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera
cap.release()

# Close all windows
cv2.destroyAllWindows()
