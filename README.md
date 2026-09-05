🚗 Lane Detection using OpenCV & Image Processing

«A Computer Vision project that detects and highlights potential lane boundaries from road-driving video using Python, OpenCV, and image processing techniques.»

🎥 Project Demo

<!-- Upload your project video to GitHub and replace the URL below -->
![lv_0_20260830005610.jpg](https://github.com/user-attachments/assets/e29043f2-93e8-471d-a635-e67ebab3c9df)

---

📌 About the Project

Lane Detection using OpenCV is a Computer Vision project developed using Python, OpenCV, and NumPy to identify and highlight potential lane boundaries from a road-driving video.

The system processes the input video frame-by-frame, applies a series of image processing operations, and analyzes the resulting features to identify regions that may correspond to lane boundaries.

This project focuses on understanding how traditional Computer Vision and Image Processing techniques can be combined to solve a practical road-scene analysis problem.

---

🎯 Project Objectives

- 🚗 Process road-driving video frame-by-frame
- 🛣️ Detect potential lane-related features
- 👁️ Identify strong edges within each frame
- 🎯 Reduce unnecessary detections using region masking
- 🔍 Detect and analyze contours
- 📐 Calculate minimum-area bounding rectangles
- 🖼️ Visualize detected regions on the original video
- ⚡ Perform real-time frame visualization

---

✨ Key Features

🎥 Video Processing

The input road video is read frame-by-frame using OpenCV's "VideoCapture".

⚫ Grayscale Conversion

Each BGR video frame is converted into grayscale to simplify the subsequent image processing operations.

📈 Custom Edge Detection

A Sobel-like horizontal gradient kernel is applied using "cv2.filter2D()" to emphasize strong intensity changes within the frame.

🎚️ Binary Thresholding

Thresholding is applied to the filtered image to isolate relevant edge information.

🚫 Region Masking

The upper portion of the frame is removed to reduce unnecessary detections from areas that are less relevant to the road surface.

🔎 Contour Detection

"cv2.findContours()" is used to detect connected regions in the processed binary image.

📐 Bounding Rectangle Detection

"cv2.minAreaRect()" is used to calculate minimum-area rotated bounding rectangles around selected contours.

🖥️ Real-Time Visualization

Detected contours and bounding rectangles are drawn onto the original video frames for visual analysis.

---

🔄 Computer Vision Pipeline

             🎥 Input Video
                    │
                    ▼
          Read Video Frame
                    │
                    ▼
            BGR → Grayscale
                    │
                    ▼
       Custom Gradient Filtering
          (cv2.filter2D)
                    │
                    ▼
          Binary Thresholding
                    │
                    ▼
            Region Masking
                    │
                    ▼
          Contour Detection
        (cv2.findContours)
                    │
                    ▼
          Contour Filtering
                    │
                    ▼
      Minimum-Area Rectangle
         (cv2.minAreaRect)
                    │
                    ▼
       Draw Detection Results
                    │
                    ▼
           🎬 Output Frame

---

🧠 Image Processing Workflow

1. Video Input

The system reads the road-driving video using OpenCV's "VideoCapture".

cap = cv2.VideoCapture("input_video.mp4")

Each frame is processed independently.

---

2. BGR → Grayscale

The captured frame is converted from BGR to grayscale.

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

This reduces the image to a single intensity channel and simplifies further processing.

---

3. Custom Gradient Kernel

A Sobel-like horizontal gradient kernel is applied using "cv2.filter2D()".

filtered = cv2.filter2D(gray, -1, kernel)

The purpose of this step is to emphasize strong changes in image intensity that may correspond to useful road/lane features.

---

4. Thresholding

A threshold is applied to separate strong edge information from the background.

_, binary = cv2.threshold(
    filtered,
    threshold_value,
    255,
    cv2.THRESH_BINARY
)

This produces a binary representation suitable for contour analysis.

---

5. Region Masking

The upper region of the frame is removed to reduce irrelevant detections.

┌─────────────────────────────┐
│                             │
│       Ignored Region        │
│                             │
├─────────────────────────────┤
│                             │
│       Road / ROI            │
│                             │
│        ╲          ╱         │
│         ╲        ╱          │
│          ╲      ╱           │
└─────────────────────────────┘

This helps concentrate the detection process on the region where lane boundaries are expected.

---

6. Contour Detection

Contours are extracted from the processed binary image using:

contours, _ = cv2.findContours(
    binary,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

The detected contours are then analyzed individually.

---

7. Contour Filtering

Small or irrelevant contours can be removed based on their area.

area = cv2.contourArea(contour)

if area > MIN_AREA:
    # Process contour

This helps reduce noise and unnecessary detections.

---

8. Minimum-Area Bounding Rectangle

For selected contours, a minimum-area rotated rectangle is calculated using:

rect = cv2.minAreaRect(contour)

The rectangle can then be converted into corner points and drawn on the original frame.

---

9. Visualization

The detected contours and bounding rectangles are displayed on the original video frame.

Original Road Frame
        │
        ▼
Detected Features
        │
        ▼
Bounding Regions
        │
        ▼
Visualized Output

---

🛠️ Technologies Used

Technology| Purpose
🐍 Python| Main programming language
👁️ OpenCV| Computer Vision & video processing
🔢 NumPy| Numerical operations and image kernels
🧠 Image Processing| Feature and edge extraction

---

🔑 OpenCV Functions Used

Function| Purpose
"cv2.VideoCapture()"| Read video frames
"cv2.cvtColor()"| BGR → Grayscale conversion
"cv2.filter2D()"| Apply custom image filtering
"cv2.threshold()"| Binary thresholding
"cv2.findContours()"| Detect contours
"cv2.contourArea()"| Calculate contour area
"cv2.minAreaRect()"| Calculate minimum-area rotated rectangle
"cv2.boxPoints()"| Obtain rectangle corner points
"cv2.drawContours()"| Draw detected contours

---

⚙️ Installation

1. Clone the Repository

git clone https://github.com/induwaralakshan4/Lane-Detection

2. Navigate to the Project Directory

cd Lane-Detection


pip install opencv-python numpy

---

▶️ Run the Project

Place your input road video in the appropriate directory and run:

python lane_detection.py

The processed frames will display the detected contours and bounding regions.


---

📊 Detection Process

The system can be summarized as:

Stage| Operation
01| Read video frame
02| Convert BGR to grayscale
03| Apply custom gradient kernel
04| Apply threshold
05| Mask upper frame region
06| Detect contours
07| Filter contours by area
08| Calculate minimum-area rectangles
09| Draw detection results
10| Display processed frame

---

🧠 What I Learned

This project provided valuable hands-on experience with traditional Computer Vision techniques.

Key learning outcomes:

- 🔹 Processing videos frame-by-frame
- 🔹 Understanding grayscale image processing
- 🔹 Designing and applying custom image kernels
- 🔹 Using "cv2.filter2D()" for image filtering
- 🔹 Applying binary thresholding
- 🔹 Understanding region-of-interest masking
- 🔹 Detecting and filtering contours
- 🔹 Working with contour geometry
- 🔹 Using minimum-area bounding rectangles
- 🔹 Visualizing Computer Vision results in real time

---

⚠️ Limitations

This project uses traditional image processing rather than a trained Deep Learning model.

Therefore, detection performance can be affected by:

- Lighting conditions
- Road surface appearance
- Shadows
- Camera angle
- Lane markings
- Weather conditions
- Video quality
- Complex road environments

The detected contours and bounding regions should therefore be considered potential lane-related features, rather than guaranteed lane boundaries.

---

🚀 Future Improvements

Possible future improvements include:

- 🛣️ Implementing a dedicated Region of Interest (ROI)
- 📐 Detecting lane lines using Hough Line Transform
- 🎯 Improving contour filtering
- 📊 Calculating lane position
- 🚗 Estimating vehicle position relative to lanes
- 🧠 Implementing Deep Learning-based lane detection
- ⚡ Optimizing real-time performance
- 🎥 Supporting live camera input
- 🌧️ Improving robustness under different lighting and weather conditions

---

🌍 Potential Applications

The techniques explored in this project can contribute to applications such as:

- 🚗 Driver assistance systems
- 🛣️ Road-scene analysis
- 🤖 Autonomous driving research
- 📹 Traffic monitoring
- 🧭 Road boundary detection
- 🚘 Intelligent transportation systems

---

📌 Project Status

Status: 🟢 Completed — Initial Version

This project is part of my journey in learning and applying Computer Vision, Image Processing, and Python to practical problems.

---

👨‍💻 About

I’m exploring Python, Computer Vision, Artificial Intelligence, and Machine Learning by building practical projects.

This project strengthened my understanding of how traditional image processing techniques can be combined to analyze road scenes and detect lane-related features.

«Learn → Build → Experiment → Improve 🚀»

---

⭐ Support

If you find this project interesting, consider giving the repository a ⭐ Star.

Your support motivates me to continue learning and building more Computer Vision and AI projects.

---

🔖 Topics

"Python" "OpenCV" "NumPy" "Computer Vision" "Lane Detection" "Image Processing" "Edge Detection" "Contour Detection" "Video Processing" "Artificial Intelligence" "Machine Learning"