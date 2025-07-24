#!/bin/bash

cd ./train/

if ! command -v yolo >/dev/null 2>&1
then
    echo "yolo could not be found. make sure you have installed all required dependencies."
    exit 1
fi

yolo classify train data=./ model=yolo11n-cls.pt epochs=100 imgsz=64

# Fix: Check for file, not directory
if [ -f "runs/classify/train/weights/best.pt" ]; then
    echo "Training completed successfully. The model and results are saved in the 'runs' directory."
    cp runs/classify/train/weights/best.pt ../rpsapi/model/rockpaperscissors.pt
else
    echo "Training failed or no results were generated."
fi

cd