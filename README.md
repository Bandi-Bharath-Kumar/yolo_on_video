# 🎯 YOLOv8 Object Detection on Video using OpenCV

This project demonstrates real-time object detection on a video file using the YOLOv8 model from Ultralytics and OpenCV.  
The detected objects are displayed live and also saved as an output video.

---

## 📌 Project Overview

- Uses **YOLOv8 (Nano version)** for fast and accurate object detection  
- Reads input from a **video file or webcam**  
- Draws **bounding boxes and class labels** on detected objects  
- Displays detection results **in real-time**  
- **Saves** the processed video to disk  

---

## 🚀 Features

- Real-time object detection  
- Supports **MP4 video files** and **webcam input**  
- Lightweight **YOLOv8n** model for faster inference  
- Automatically saves **output video**  
- Easy to **modify and extend**  

---

## 🛠️ Technologies Used

- Python  
- OpenCV (`cv2`)  
- Ultralytics YOLOv8  
- Pre-trained **COCO** dataset  

---

## 📂 Project Structure

    YOLOv8-Object-Detection/
    │
    ├── yolo.py              # Python script for object detection
    ├── output.mp4           # Generated output video
    ├── README.md            # Project documentation
    └── requirements.txt     # Required dependencies

---

## 📦 Requirements

Make sure you have **Python 3.8 or above** installed.

### Required Libraries

- `opencv-python`  
- `ultralytics`  

---

## 🔧 Installation

1. **Clone the repository**

    git clone https://github.com/your-username/YOLOv8-Object-Detection.git  
    cd YOLOv8-Object-Detection

2. **Install dependencies**

   Using `requirements.txt`:

    pip install -r requirements.txt

   Or install manually:

    pip install opencv-python ultralytics

---

## ▶️ How to Run the Project

1. Update the **input video path** in the code:

    video_path = "path_to_your_video.mp4"

2. Update the **output video path** if required:

    output_video = "path_to_save_output.mp4"

3. Run the script:

    python main.py

4. Press **q** in the video window to stop execution.

---

## 🧠 How It Works

1. Loads a YOLOv8 pre-trained model (`yolov8n.pt`)  
2. Reads frames from a video file (or webcam)  
3. Performs object detection on each frame  
4. Draws bounding boxes and labels on detected objects  
5. Displays detected frames in real-time  
6. Saves the processed frames into an output video file  

---

## 🧪 Model Used

- **YOLOv8n (Nano)**
  - Fast and lightweight  
  - Ideal for **real-time detection**  
  - Trained on **COCO dataset** (80 object classes)  

---

## 📊 Supported Object Classes

The model can detect common objects such as:

- Person  
- Car  
- Bicycle  
- Bus  
- Truck  
- Dog  
- Cat  
- Laptop  
- Mobile phone  
- …and many more.

---

## 📌 Use Cases

- Video surveillance  
- Traffic monitoring  
- Smart cities  
- Autonomous vehicles  
- Retail analytics  
- Educational demonstrations  

---

## 🔮 Future Enhancements

- Webcam live detection  
- Custom-trained YOLO model  
- FPS counter  
- Object tracking  
- GUI using Streamlit or Tkinter  
