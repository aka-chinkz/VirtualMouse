# 🖐️ Hand Gesture Mouse Control

A virtual mouse application built with Python and computer vision that lets you control your computer's cursor using hand movements captured through a webcam. It uses MediaPipe to track hand landmarks and PyAutoGUI to move the cursor and perform clicks based on finger positions.

## ✨ Features

- 🖱️ **Hand-Based Cursor Control** — Move the cursor by moving your index finger.
- 👆 **Gesture-Based Clicking** — Trigger a mouse click when the index and middle fingertips come close together.
- 🎯 **Cursor Smoothing** — Reduce sudden cursor movements for smoother navigation.
- 📷 **Real-Time Hand Tracking** — Detect hand landmarks using MediaPipe.
- 🟪 **Visual Hand Tracking** — Display detected hand landmarks, connections, fingertip markers, and a tracking boundary.
- ⌨️ **Quick Exit** — Press `Q` to close the application.

## 🛠️ Tech Stack

- **Python** — Core programming language
- **OpenCV** — Webcam capture, image processing, and visual display
- **MediaPipe** — Real-time hand landmark detection
- **PyAutoGUI** — Mouse cursor movement and clicking

## ⚙️ How It Works

1. **Webcam Capture:** OpenCV captures video frames at a resolution of 640 × 480.
2. **Hand Detection:** MediaPipe detects the hand and identifies its landmarks.
3. **Cursor Movement:** The index fingertip (landmark 8) is mapped to screen coordinates to control the mouse.
4. **Cursor Smoothing:** A smoothing factor of `4` reduces abrupt changes in cursor position.
5. **Mouse Clicking:** When the index fingertip and middle fingertip (landmark 12) are within 40 pixels vertically, the program triggers a left-click.
6. **Live Visualization:** OpenCV displays the webcam feed with hand landmarks and fingertip indicators.

## 📋 Prerequisites

- Python installed on your system
- A working webcam
- A display and mouse-control permissions
- An internet connection to install dependencies

## 🚀 Installation

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_REPOSITORY_NAME>
```

### 2. Install dependencies

```bash
pip install opencv-python mediapipe pyautogui
```

### 3. Run the application

Save the Python script as `main.py`, then run:

```bash
python main.py
```

## 🎮 Controls

| Action | How to perform |
|---|---|
| Move cursor | Move your index finger |
| Left-click | Bring the index and middle fingertips close together vertically |
| Exit application | Press `Q` in the webcam window |

**Tip:** Keep your hand visible to the webcam and move it within the camera's field of view for better tracking.

## 📁 Project Structure

```text
Hand-Gesture-Mouse-Control/
├── main.py
└── README.md
```

## 🔧 Configuration

You can customize the following variables in the Python script:

| Variable | Purpose |
|---|---|
| `smoothing = 4` | Controls cursor smoothing |
| `frameR = 100` | Sets the visual tracking boundary |
| `Wcam, Hcam = 640, 480` | Defines the camera coordinate dimensions |

A higher smoothing value generally produces smoother but slower cursor movement.

## 🚀 Future Improvements

- Add right-click and double-click gestures.
- Implement gesture-based scrolling.
- Use the distance between fingertips for more reliable clicking.
- Restrict cursor movement to the defined tracking boundary.
- Add a pause/resume gesture and customizable sensitivity.
- Improve multi-hand detection and tracking stability.

## 🤝 Contributing

Contributions and suggestions are welcome!

1. Fork this repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Submit a pull request.

## 📄 License

Choose and add an appropriate open-source license if you intend to allow others to reuse or modify this project.

---

**If you find this project useful, consider giving it a ⭐ on GitHub!**
