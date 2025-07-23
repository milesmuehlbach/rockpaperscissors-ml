from ultralytics import YOLO
import os
import sys
import cv2
import numpy as np

def fetch():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Error: Could not open camera.")
        sys.exit(1)

    ret, frame = camera.read()
    camera.release()

    if not ret:
        print("Error: Could not read frame from camera.")
        sys.exit(1)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    model_path = os.path.join(os.path.dirname(__file__), "model", "rockpaperscissors.pt")
    if not os.path.exists(model_path):
        print(f"Error: Model file not found at {model_path}")
        sys.exit(1)
    model = YOLO(model_path)
    results = model(frame_rgb)
    probs = results[0].probs
    if probs is None:
        print("Error: No classification probabilities returned.")
        sys.exit(1)
    class_index = int(probs.top1)
    confidence = float(probs.top1conf) 
    class_name = model.names[class_index]

    if confidence < 0.5:
        print("We were unable to determine your sign. Please try again.")
        class_name = "unknown"

    return class_name

def process_image(image_data):
    np_arr = np.frombuffer(image_data, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    if frame is None:
        print("Error: Could not decode image data.")
        return "unknown"
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    model_path = os.path.join(os.path.dirname(__file__), "model", "rockpaperscissors.pt")
    if not os.path.exists(model_path):
        print(f"Error: Model file not found at {model_path}")
        return "unknown"
    model = YOLO(model_path)
    results = model(frame_rgb)
    probs = results[0].probs
    if probs is None:
        print("Error: No classification probabilities returned.")
        return "unknown"
    class_index = int(probs.top1)
    confidence = float(probs.top1conf)
    class_name = model.names[class_index]

    if confidence < 0.5:
        print("We were unable to determine your sign. Please try again.")
        class_name = "unknown"

    return class_name