# HIT137 Group Assignment 3

## Python Image Editor using Tkinter & OpenCV

---

### Unit

**HIT137 – Object-Oriented Programming**

### Assignment

**Group Assignment 3 (30%)**

### Institution

**Charles Darwin University**

---

## Group Members

| Name                  | Student ID |
| --------------------- | ---------- |
| Mou Rani Biswas       | 398778     |
| MD Saifur Rahman      | 398921     |
| Nahid Hasan Sangram   | 395231     |
| Mohammed Rifatul Alam | 399533     |

---

## Project Overview

This project is a **desktop-based image editing application** developed in Python as part of **HIT137 Group Assignment 3**.  
The application demonstrates practical understanding of:

- **Object-Oriented Programming (OOP) principles**
- **GUI development using Tkinter**
- **Image processing using OpenCV**
- **Collaborative development using GitHub**

The system allows users to open, edit, preview, undo/redo, and save images using a clean and user-friendly graphical interface.

---

## Key Learning Outcomes Demonstrated

- Proper application of **encapsulation, constructors, methods, and class interaction**
- Use of **multiple well-structured classes**
- Integration of **OpenCV image processing** within a Tkinter GUI
- Implementation of **Undo/Redo functionality**
- Effective **GitHub collaboration with commit history from all group members**

---

## Application Features

### File Management

- Open image files (JPG, PNG, BMP)
- Save image
- Save image as a new file
- Exit confirmation dialog

### Edit Features

- Undo last operation
- Redo previously undone operation

### Image Processing (OpenCV – All Required Filters)

1. Grayscale conversion
2. Gaussian blur (adjustable intensity)
3. Edge detection using Canny algorithm
4. Brightness adjustment
5. Contrast adjustment
6. Image rotation (90°, 180°, 270°)
7. Image flip (horizontal and vertical)
8. Image resize / scaling

### GUI Components

- Main application window with title
- Menu bar (File & Edit menus)
- Image display area (canvas)
- Control panel with buttons and sliders
- Status bar displaying image information (filename and dimensions)
- Message boxes for errors and confirmations

---

## Object-Oriented Design

The application follows a **clear OOP architecture** using multiple interacting classes:

### Main Classes

- **ImageEditorGUI**  
  Handles the Tkinter user interface, user interactions, and event handling.

- **ImageProcessor**  
  Implements all OpenCV-based image processing operations.

- **ImageIO**  
  Manages image loading and saving using file dialogs.

- **HistoryManager**  
  Maintains undo and redo stacks for non-destructive editing.

This structure ensures **modularity, readability, maintainability, and scalability**.

---

## Project Structure
