# Image Editor Desktop Application  
**HIT137 – Group Assignment 3**

## Project Overview
This project is a **desktop-based Image Editor application** developed using **Python**, **Tkinter**, and **OpenCV**.  
It demonstrates the use of **Object-Oriented Programming (OOP)** concepts, **Graphical User Interface (GUI)** design, and **image processing techniques**.

The application allows users to load an image and apply various image processing operations through an interactive graphical interface.

---

## Objectives
- Demonstrate understanding of **OOP principles**
- Build a functional **Tkinter GUI**
- Apply **image processing operations using OpenCV**
- Design a user-friendly and interactive desktop application

---

## Technologies Used
- **Python 3**
- **Tkinter** – GUI development
- **OpenCV (cv2)** – Image processing
- **Pillow (PIL)** – Image rendering in Tkinter

---

## 📸 Features Implemented

### Image Processing Features (OpenCV)
- ✅ Grayscale Conversion
- ✅ Gaussian Blur (Adjustable Intensity)
- ✅ Edge Detection (Canny Algorithm)
- ✅ Brightness Adjustment (Slider)
- ✅ Contrast Adjustment (Slider)
- ✅ Image Rotation (90°, 180°, 270°)
- ✅ Image Flip (Horizontal & Vertical)
- ✅ Resize / Scale Image (Slider)
- ✅ Restore Original Image

---

### GUI Features (Tkinter)
- Main application window
- Scrollable control panel
- Image display area
- Menu bar (File → Open, Save As, Exit)
- Buttons and sliders for image effects
- Status bar for user feedback
- File dialogs for opening and saving images
- Error handling using message boxes

---

## Object-Oriented Programming (OOP)
The project uses multiple classes to demonstrate OOP concepts:

| Concept | Implementation |
|------|----------------|
| Encapsulation | Image processing logic inside `ImageProcessor` |
| Constructor | Used in all classes (`__init__`) |
| Methods | Image operations like blur, rotate, resize |
| Class Interaction | GUI interacts with ImageProcessor |
| Modularity | Separate files for GUI, processing, utilities |

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install opencv-python pillow

### How to run application
```bash
python main.py

