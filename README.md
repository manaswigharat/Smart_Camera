
# 📸 Smart Camera – AI-Based Camera with Gesture Controls

A Python-based Smart Camera application built using **OpenCV, MediaPipe, and NumPy**. It provides real-time camera filters, hand landmark detection, gesture-based controls, and digital zoom for an interactive camera experience.

---

## 🚀 Features

### 🎨 25 Real-Time Camera Filters

Explore 25 creative filters divided into different categories:

- **Basic Filters:** Normal, Grayscale, Sepia, Blur, Black Mist
- **Color Filters:** Warm, Cool, Vintage, Bright, Cinematic
- **Aesthetic Filters:** Pink Glow, Peach, Lavender, Rose, Dreamy
- **Creative Filters:** Golden Hour, Sunset, Ocean, Mint, Film Fade
- **Advanced Filters:** Matte, Noir, Teal & Orange, Soft Skin, Neon Edge

### ✋ AI-Based Hand Gesture Recognition

Uses MediaPipe Hands to detect hand landmarks and recognize gestures.

| Hand Gesture | Action |
|---|---|
| Pinch (Thumb + Index) | Change to Next Filter |
| Thumbs Up 👍 | Zoom In |
| Thumbs Down 👎 | Zoom Out |
| Open Palm ✋ | Reset Zoom |

### 🔍 Digital Zoom

- Zoom In and Zoom Out
- Smooth digital image enlargement
- Minimum Zoom: 1x
- Maximum Zoom: 3x
- Gesture and keyboard-based zoom control

### 🖱️ Mouse Controls

- Previous Button – Select Previous Filter
- Next Button – Select Next Filter

### ⌨️ Keyboard Shortcuts

| Key | Function |
|---|---|
| `N` | Next Filter |
| `P` | Previous Filter |
| `+` | Zoom In |
| `-` | Zoom Out |
| `0` | Reset Zoom |
| `L` | Toggle Hand Landmarks |
| `Q` / `ESC` | Exit Camera |

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main Programming Language |
| OpenCV | Real-Time Video Capture and Image Processing |
| MediaPipe | Hand Tracking and Gesture Recognition |
| NumPy | Image Manipulation and Numerical Operations |

---

## 📂 Project Structure

```text
Smart_Camera/
│
├── filter_test.py
├── requirements.txt
├── README.md
├── .gitignore
└── .venv/              # Local environment (not uploaded)
```

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart_Camera.git
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Navigate to the Project Folder

```bash
cd Smart_Camera
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

If MediaPipe compatibility issues occur, use:

```bash
pip install mediapipe==0.10.21
```

### 6. Run the Application

```bash
python filter_test.py
```

Make sure your webcam is connected and accessible.

---

## 🧠 How It Works

1. **Video Capture:** OpenCV captures live video from the webcam.
2. **Image Processing:** The selected filter is applied to each video frame.
3. **Hand Detection:** MediaPipe identifies hand landmarks in real time.
4. **Gesture Recognition:** Finger positions and distances are analyzed to identify gestures.
5. **Camera Control:** Recognized gestures trigger filter changes and zoom operations.
6. **Display:** The processed video is displayed with camera information and controls.

---

## 🎯 Project Objectives

- Develop an interactive camera application using Python.
- Implement real-time image processing and creative filters.
- Explore AI-based hand tracking using MediaPipe.
- Enable touch-free camera interaction through hand gestures.
- Integrate digital zoom and multiple user controls.

---

## 🔮 Future Enhancements

- Capture and save photographs.
- Record videos with selected filters.
- Add face detection and face tracking.
- Introduce more Snapchat-style AR filters.
- Add background replacement and blur effects.
- Develop a graphical user interface (GUI).
- Add customizable gesture controls.

---

## 👩‍💻 Developed With

Python | OpenCV | MediaPipe | NumPy

**Project:** Smart Camera  
**Category:** Computer Vision and Image Processing

---

⭐ If you find this project interesting, consider giving the repository a star!