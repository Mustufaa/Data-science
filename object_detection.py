import cv2

# Open the video file
video_path = r'C:\Users\lenovo\Downloads\8566515-uhd_2560_1440_30fps.mp4'

cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Failed to open video file")
    exit()

# Read the first frame
ret, frame = cap.read()
if not ret:
    print("Failed to read the video frame")
    cap.release()
    cv2.destroyAllWindows()
    exit()

# Resize the frame for faster processing (optional)
frame_resized = cv2.resize(frame, (500, 500))

# Select ROI (Region of Interest) for tracking
bbox = cv2.selectROI(frame_resized, False)

# Create a tracker object using the modern API
tracker = cv2.TrackerKCF_create()
tracker.init(frame_resized, bbox)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame to match initial resize (optional)
    frame_resized = cv2.resize(frame, (500, 500))

    # Update the tracker
    success, bbox = tracker.update(frame_resized)

    if success:
        # Draw bounding box on the frame
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame_resized, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Frame', frame_resized)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
