# Rock Paper Scissors: Machine Learning edition

### Overview
This is a project that uses a [dataset](https://www.kaggle.com/datasets/glushko/rock-paper-scissors-dataset), trained on Rock, Paper, and Scissors hand signs, to play a game of real rock paper scissors with the computer. There are two options for playing, cli (availible through `rpscli.py`) and webapp, but both will not be availible until after setup has been completed. This project has been designed for running on the Nvidia Jetson Orin Nano, running Jetpack 6.x. On the backend, it implements a python api through the form of `rpsapi`, designed for handling both gameplay and fetching of hand signs. The webapp uses tailwindcss for the frontend, and implements flask in the backend.

### Setup 
To start with setting up, first clone the repository. You must be on linux to make use of this repository, there is no plan for windows support at this time.
```
git clone https://github.com/milesmuehlbach/rockpaperscissors-ml.git
```
After you've done that, enter the directory and install the dependencies.
```
cd rockpaperscissors-ml && scripts/installdependencies.sh
```
If it throws an error, then follow what the error tells you to do.

At this step, we'll be training the model, as I don't provide pre-trained models. This will take 30+ minutes, so make sure you're prepared.
```
scripts/trainmodel.sh
```
After the model is trained, you should be good to start using the app! Follow the instructions under Running to proceed.

### Running
#### Running CLI
(assuming you're in root directory of project)
```
python3 ./rpscli.py
```
#### Running Webapp
(assuming you're in root directory of project)
```
python3 -m webapp.app
```
> [!NOTE]  
> While the dev server for the webapp is configured to be availible over the network, most browsers do not allow webcam perms for non-localhost or non-https requests. You may need to set special flags in your browser of choice or configure https.
