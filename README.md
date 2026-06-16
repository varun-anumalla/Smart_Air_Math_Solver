# Smart Air Math Solver

## Overview

Smart Air Math Solver is a computer vision based application that allows users to write mathematical equations in the air using hand gestures and instantly solve them.

The project uses real-time hand tracking to create a virtual drawing experience. Users can draw equations in the air, and the application recognizes the handwritten expression using OCR (Optical Character Recognition) and calculates the result automatically.

This project was built to explore Computer Vision, OCR, Hand Tracking, and Python-based real-time applications.

---

## Features

* Real-time hand tracking using MediaPipe
* Air drawing using finger gestures
* Multiple drawing colors
* Eraser functionality
* Canvas clear option
* OCR-based equation recognition
* Automatic mathematical expression evaluation
* Live webcam interface
* Save drawing functionality
* Real-time equation and answer display

---

## Technologies Used

### Programming Language

* Python

### Libraries

* OpenCV
* MediaPipe
* EasyOCR
* NumPy

### Concepts

* Computer Vision
* Hand Tracking
* Optical Character Recognition (OCR)
* Image Processing
* Real-Time Video Processing

---

## Project Structure

```text
Smart_Air_Math_Solver/
│
├── modules/
│   ├── canvas.py
│   ├── display.py
│   ├── hand_tracker.py
│   ├── math_evaluator.py
│   └── ocr_engine.py
│
├── screenshots/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## How It Works

1. The webcam captures live video.
2. MediaPipe tracks the user's hand and finger position.
3. Finger movements are converted into drawing strokes on a virtual canvas.
4. The user writes a mathematical equation in the air.
5. The equation is captured and processed using EasyOCR.
6. The recognized expression is evaluated.
7. The result is displayed on the screen in real time.

---

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

Move into the project folder:

```bash
cd Smart_Air_Math_Solver
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

## Screenshots

### Air Drawing Interface

[soon i will update]

### Equation Recognition

[soon i will update]

### Result Display

[soon i will update]

---

## Project Demo Video

YouTube Demo:

[coming very soon]

---

## Future Improvements

* Improved OCR accuracy
* Support for complex mathematical expressions
* Auto-solve without button click
* Equation history tracking
* Better UI and visualization
* Support for additional mathematical operators

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Computer Vision
* Hand Tracking
* OCR Integration
* Real-Time Video Processing
* Python Application Development
* Git and GitHub Workflow

---

## Author

Varun Anumalla

LinkedIn:
[Varun Anumalla]
