# Engineering Projects: Computer Vision & Logic 🚀

A collection of Python implementations focusing on image processing algorithms and discrete mathematics, developed as part of my Computer Engineering studies at UPIICSA.

---

## 🛣️ 1. Road Lane Detection (Sobel Operator)
This project implements an image processing pipeline to detect lane markings on highways using gradient-based edge detection.

### Technical Workflow:
1. **Grayscale Conversion:** Simplifies data for faster processing.
2. **Gaussian Blur:** Reduces high-frequency noise for cleaner edge detection.
3. **Sobel Operators:** Calculates the horizontal (X) and vertical (Y) derivatives.
4. **Gradient Magnitude:** Combines Sobel outputs to highlight distinct lane boundaries.

**Tech Stack:** Python, OpenCV (cv2), NumPy, Matplotlib.

---

## 🔢 2. Set Theory Operations Tool
A CLI-based application designed to perform standard mathematical operations on data sets.

### Key Operations:
* **Union (Join):** Merges two data sets (K and L).
* **Set Difference:** Calculates relative complements (K - L and L - K).
* **Logical Combination:** Implements a mathematical union without duplicates using Python's Set logic.

**Tech Stack:** Python (List Comprehensions, Set data structures).

---

## ⚙️ Setup and Installation
1. Clone this repository.
2. Ensure you have the required libraries installed:
   ```bash
   pip install opencv-python numpy matplotlib
