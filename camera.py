import cv2
import queue
import threading

# Define the queue object that will hold the frames from the camera
frame_queue = queue.Queue(maxsize=2)

# Define a function that captures frames from the camera and stores them in the queue
def capture_frames():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Put the frame in the queue for processing
        frame_queue.put(frame)
    # Release the camera
    cap.release()

# Create a thread to run the capture function
capture_thread = threading.Thread(target=capture_frames)

# Start the thread
capture_thread.start()

# Wait for the capture thread to finish
capture_thread.join()
