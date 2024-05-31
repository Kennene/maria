## Overview
The Maria program is a voice recognition application that listens to what you say and converts it into text. It uses Google's service to do this. If it has trouble understanding what you said or if Google's service is not available, it will let you know. It also has the ability to adjust to the noise level in your environment.

## Installation
Installing the software is rather simple. To install the program, you must have Python version 3.11.2.
First, create a Python virtual environment in the program directory with the command:
```
python3 -m venv venv
```

Activate the virtual environment with the command:
```
source venv/bin/activate
```

Next, install the necessary dependencies with the command:
```
pip3 install -r requirements.txt
```

For the program to work correctly, you need to add your OpenAI key to the .env file. The easiest way to create this file is to rename env.example to .env.
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

After completing the above steps, you can run the program with the command:
```
python3 maria.py
```
