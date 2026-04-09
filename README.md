# Lane Detection Segmentation 🛣️

## Overview
This project processes highway images to assist in lane detection. It takes a raw road image and decomposes it into 4 strategic segments to focus on lane markings and reduce computational noise.

## 🛠️ Technologies
* **Python** 
* **OpenCV** (Computer Vision)
* **NumPy** (Image processing as arrays)

## 📸 Results
| Original Image | Segmented Output (4 Quadrants) |
|---|---|
| ![Original](input_images/road_sample.jpg) | ![Result](output_samples/processed_grid.jpg) |

## 🚀 Future Roadmap
* Implement **Canny Edge Detection** on each segment.
* Apply **Hough Transform** for line drawing.
* Real-time video processing.
