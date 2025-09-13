import cv2
from ultralytics import YOLO
import time  # For FPS calculation

# Load the pre-trained YOLOv8 nano model (efficient for real-time)
model = YOLO('yolov8n.pt')  # Auto-downloads if not present

# Open webcam (0 for default; replace with video file path for offline)
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# Optional: Filter to specific classes (COCO dataset names)
# classes_to_detect = ['person', 'car', 'dog']  # Uncomment and modify to filter
classes_to_detect = None  # Detect all 80 classes

# Confidence threshold for detections (higher = fewer false positives)
conf_threshold = 0.25

# Image size for inference (640 is balanced; lower for speed)
imgsz = 640

# FPS tracking
fps_counter = 0
start_time = time.time()

print("Starting real-time detection. Press 'q' to quit.")

while True:
    # Read frame from video capture
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Run YOLO inference
    results = model(frame, conf=conf_threshold, imgsz=imgsz, classes=classes_to_detect, verbose=False)

    # Draw results on frame
    annotated_frame = results[0].plot()  # Includes boxes, labels, confidences

    # Calculate and display FPS
    fps_counter += 1
    if fps_counter % 30 == 0:  # Update every 30 frames
        end_time = time.time()
        fps = 30 / (end_time - start_time)
        start_time = end_time
        print(f"Current FPS: {fps:.2f}")

    # Add FPS text to frame
    cv2.putText(annotated_frame, f"FPS: {fps_counter / (time.time() - start_time):.1f}", 
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the annotated frame
    cv2.imshow('YOLOv8 Real-Time Detection', annotated_frame)

    # Break on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
print("Detection stopped.")
