# Object Detection & Tracking System

A powerful, real-time object detection and tracking application built with **FastAPI**, **YOLOv8**, and **OpenCV**. This system allows users to upload images or stream videos (via webcam or file) to detect, track, and analyze common objects with high accuracy.

## Features

- **Real-time Video Streaming**: Stream from a webcam or uploaded video files with live detection and tracking.
- **Image Analysis**: Upload images for high-precision detection with a generated PDF/JSON report.
- **Adaptive AI Pipeline**:
  - **Dynamic Image Sizing**: Automatically adjusts resolution to maintain detail for high-res images and reduce noise for low-res images.
  - **Auto-Adaptive Thresholding**: Heuristically adjusts confidence levels based on image contrast to reduce False Positives and False Negatives.
  - **Lighting Enhancement**: Uses CLAHE (Contrast Limited Adaptive Histogram Equalization) to improve detection in poor lighting or overexposed conditions.
- **Hardware Acceleration**: Auto-detects and utilizes NVIDIA CUDA GPUs for significantly faster inference.
- **Detailed Reporting**: Generates comprehensive PDF reports including object counts, confidence scores, and bounding box coordinates.

##  Tech Stack

- **Backend**: FastAPI
- **AI Model**: YOLOv8 (Ultralytics)
- **Computer Vision**: OpenCV
- **Processing**: NumPy, Torch
- **Reporting**: ReportLab (PDF generation)

##  Installation

### Prerequisites
- Python 3.10+
- NVIDIA GPU (Optional, for CUDA acceleration)

### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd object-detection-tracking
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python -m app.main
   ```

## API Endpoints

### Video API
- `GET /api/video/stream`: Stream video detections.
  - Params: `source` (webcam/upload), `filename` (for uploads), `tracking` (true/false).
- `POST /api/video/upload`: Upload a video file for processing.

### Image API
- `POST /api/video/image/analyze`: Upload an image for analysis.
- `GET /api/video/report/{report_id}`: Download the analysis report in `pdf` or `json` format.

## Performance & Generalization
This system is designed to handle diverse environments:
- **Low Light**: Enhanced via CLAHE preprocessing.
- **High Res**: Handled via dynamic `imgsz` scaling (up to 1280px).
- **Noisy Images**: Managed by adaptive confidence thresholds based on image entropy.

## Project Structure
- `app/`: Main application logic.
  - `routes/`: FastAPI endpoints.
  - `services/`: Core AI logic (Detector, Tracker, Video Processor).
  - `utils/`: Configuration and image processing utilities.
- `runs/`: Trained model weights.
- `uploads/`: Temporary storage for uploaded media.
- `outputs/`: Generated annotations and reports.
- `tests/`: Test suites for the detection pipeline.
