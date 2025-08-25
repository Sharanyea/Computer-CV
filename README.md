# 🖼️ Computer CV Projects Repository

Welcome to the **Computer CV** repository! Here you'll find two exciting projects built with **OpenCV (cv2)** and **NumPy**, showcasing real-time computer vision techniques. Whether you're a beginner or a seasoned developer, these projects are a great way to dive into the world of image processing and computer vision.

---

## 📦 Projects Overview

### 🎨 Project 1: Drawing Colors with Object Color Detection

Create digital art by simply moving colored objects in front of your webcam!

**Key Concepts:**
- **HSV Color Space:** Robust color detection across lighting conditions
- **Contour Detection:** Pinpointing object position in real-time
- **OpenCV Video Processing:** Instant feedback and drawing

**How It Works:**
1. The webcam detects objects of predefined colors.
2. Each color is mapped to a specific drawing color (BGR format).
3. The object’s position is tracked, turning it into a "virtual paintbrush" that draws on the screen.

---

### 📄 Project 2: Document Scanner

Turn your webcam into a handy document scanner using perspective transformation!

**Key Concepts:**
- **Image Preprocessing:** Grayscale conversion, blurring, edge detection, dilation, and erosion
- **Contour Detection:** Locating the largest quadrilateral (your document)
- **Perspective Warp:** Transforming your document for a crisp, top-down scanned effect

**How It Works:**
1. The webcam captures and preprocesses the image to highlight edges.
2. The largest 4-point contour (assumed to be the document) is detected.
3. A perspective transform gives a scanned, top-down view of your document.

---

## ⚙️ Requirements

Before you begin, ensure you have the following dependencies installed:

```bash
pip install opencv-python numpy
```

---

## ▶️ Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Sharanyea/Computer-CV.git
    ```
2. **Navigate to the project folder:**
    ```bash
    cd Computer-CV
    ```
3. **Run the scripts:**
    ```bash
    python project1.py   # Drawing Colors with Object Detection
    python project2.py   # Document Scanner
    ```

> **Tip:** Press `q` in the webcam window to exit.

---

## 🚀 Future Improvements

- [ ] Add GUI controls for custom color selection
- [ ] Save scanned documents as PDF or image files
- [ ] Multi-color brush and eraser functionality for Project 1

---


**Happy Coding! 👩‍💻👨‍💻**
