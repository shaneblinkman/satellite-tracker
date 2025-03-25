# ISS Location Tracker

A simple web application that tracks the International Space Station's (ISS) location in real-time using the Open Notify API.

## Features

- Real-time ISS location tracking
- Updates every 5 seconds
- Clean and responsive user interface
- Displays latitude, longitude, and last update time

## Setup

1. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Technologies Used

- Flask
- Python Requests
- HTML/CSS/JavaScript
- Open Notify API
