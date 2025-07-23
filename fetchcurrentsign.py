#!/usr/bin/python3

import cv2
import numpy as np
import os
import sys
from ultralytics import YOLO

# Open camera
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Error: Could not open camera.")
    sys.exit(1)

ret, frame = camera.read()
camera.release()

if not ret:
    print("Error: Could not read frame from camera.")
    sys.exit(1)

# Convert BGR to RGB
frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

model_path = "model/rockpaperscissors.pt"
if not os.path.exists(model_path):
    print(f"Error: Model file not found at {model_path}")
    sys.exit(1)

# Load model and run inference
model = YOLO(model_path)
results = model(frame_rgb)

# Extract classification predictions
probs = results[0].probs  # probabilities for each class
if probs is None:
    print("Error: No classification probabilities returned.")
    sys.exit(1)

class_index = int(probs.top1)  # index of top prediction
confidence = float(probs.top1conf)  # confidence of top prediction
class_name = model.names[class_index]

print(f"{class_name} {confidence * 100:.0f}%")
