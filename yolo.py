import cv2
from ultralytics import YOLO

# Open video file or webcam
video_path = "C:\\Users\\BANDI BHARATH KUMAR\\Downloads\\2252223-uhd_3840_2160_30fps.mp4"
cap = cv2.VideoCapture(video_path)

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Get video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define output video writer
output_video = "C:\\Users\\BANDI BHARATH KUMAR\\OneDrive\\Videos\\output.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video, fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection
    results = model(frame)
    detected_frame = results[0].plot()

    # Display the frame
    cv2.imshow("YOLOv8 Object Detection", detected_frame)

    # Write frame to output video
    out.write(detected_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()