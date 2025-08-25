CV2 Projects Repository

This repository contains two projects built using OpenCV (cv2) and NumPy. Both projects demonstrate the application of computer vision techniques for real-time tasks.

📌 Projects
Project 1: Drawing Colors with Object Color Detection

This project allows you to draw on the screen using objects of specific colors detected by the webcam.

Concepts Used:

HSV color space for color detection

Contour detection to find object position

Real-time video processing with OpenCV

How It Works:

The webcam detects objects of predefined colors.

Each detected color is assigned a specific drawing color (BGR format).

The position of the detected object is tracked, and a circle is drawn at its coordinates, creating a "virtual paintbrush."

Project 2: Document Scanner

This project simulates a document scanner using perspective transformation.

Concepts Used:

Image preprocessing (grayscale, blur, edge detection, dilation, erosion)

Contour detection to identify the largest quadrilateral (document)

Reordering points and applying perspective warp for scanning effect

How It Works:

The webcam captures an image and preprocesses it to highlight edges.

Contours are analyzed to find the largest 4-point shape (document).

A perspective transform is applied to give a top-down scanned view of the document.

⚙️ Requirements

Make sure you have the following installed:

pip install opencv-python numpy

▶️ How to Run

Clone the repository:

git clone https://github.com/yourusername/your-repo.git


Navigate into the project folder.

Run the scripts:

python project1.py   # For Drawing Colors
python project2.py   # For Document Scanner


Press q to exit the webcam window.


🚀 Future Improvements

Add GUI controls to select custom colors.

Save scanned documents as PDF or image files.

Multi-color brush and eraser functionality for Project 1.
