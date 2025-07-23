# Rock Paper Scissors: Machine Learning Edition

## Overview

This project uses a [Rock Paper Scissors hand sign dataset](https://www.kaggle.com/datasets/glushko/rock-paper-scissors-dataset) and a custom-trained machine learning model to let you play real-time Rock Paper Scissors against your computer.  
You can play either via the command line (`rpscli.py`) or a modern web interface.  
The project is designed for the Nvidia Jetson Orin Nano running JetPack 6.x, but may work on other Linux systems with compatible dependencies.

- Backend: Python (Flask), custom API (`rpsapi`)
- Frontend: TailwindCSS, HTML, JavaScript
- Model: YOLO, trained on hand sign images

## Setup

> [!IMPORTANT]  
> This project is designed for Linux. Windows is not supported.

### 1. Clone the Repository

```sh
git clone https://github.com/milesmuehlbach/rockpaperscissors-ml.git
cd rockpaperscissors-ml
```

### 2. Install Dependencies

```sh
scripts/installdependencies.sh
```

> [!TIP]
> If you encounter errors during installation, carefully read the error messages and install any missing system packages as instructed.

### 3. Train the Model

> [!WARNING] 
> No pre-trained model is provided.  
> Training will take 30+ minutes and requires a CUDA-capable GPU (Jetson recommended).

```sh
scripts/trainmodel.sh
```

After the model is trained, you should be good to start using the app. Follow the instructions under Running to proceed.

## Running

### Command Line Interface (CLI)

(Assuming you're in the root directory of the project)

```sh
python3 ./rpscli.py
```

### Web Application

(Assuming you're in the root directory of the project)

```sh
python3 -m webapp.app
```
The server should now be running on port 5000. If you want to access it from localhost, you can visit it at `http://localhost:5000` in your browser.

> [!NOTE]
> The development server is accessible over the network, but most browsers block webcam access for non-HTTPS or non-`localhost` sites.  
> For best results, run the webapp on `localhost` or configure HTTPS.  
> You may need to set special flags in your browser to allow webcam access on local network addresses.

## Project Structure

```
rockpaperscissors-ml/
├── rpscli.py           # Command-line interface
├── webapp/             # Flask web application
│   ├── app.py
│   ├── templates/
│   └── static/
├── rpsapi/             # API and ML model logic
│   ├── fetchsign.py
│   └── rps.py
├── scripts/            # Setup and training scripts
│   ├── installdependencies.sh
│   ├── trainmodel.sh
│   └── runtailwinddev.sh
└── README.md
```

## Troubleshooting

- **Webcam not working?**
  - Make sure you are using `localhost` or HTTPS.
  - Check browser permissions for camera access.
  - See browser console for errors.

- **Model not found?**
  - Ensure you have run `scripts/trainmodel.sh` and the model file exists in `rpsapi/model/`.

- **Other issues?**
  - Check the Issues section on GitHub or open a new issue with details.

> [!TIP]
> Contributions, suggestions, and feedback are welcome!  
> Please open an issue or submit a pull request on GitHub.
