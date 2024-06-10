WhatsApp Volume Automator

Overview
The WhatsApp Volume Automator is a simple Python script designed to automate the adjustment of system volume whenever the WhatsApp Desktop application is opened.

Functionality
The script continuously monitors active audio sessions and detects when the WhatsApp Desktop application is running. When WhatsApp Desktop is detected, the script adjusts the system volume to the desired level.

Requirements
Python 3.x
pycaw module (can be installed via pip install pycaw)
Usage
Ensure Python 3.x is installed on your system.
Install the required pycaw module using pip install pycaw.
Run the main.py script using pythonw to execute it in the background.
bash
Copy code
pythonw main.py
The script will now continuously monitor the system for the WhatsApp Desktop application and adjust the volume when it is detected.
Notes
This script relies on detecting the WhatsApp Desktop application process. Make sure you have the WhatsApp Desktop application installed and running for the script to function properly.
The script runs continuously in the background. To stop it, terminate the pythonw.exe process associated with the script.
Author
[implaymo]