# Real-Time Drowsiness Detection System

## Project Overview
The Real-Time Drowsiness Detection System is designed to monitor the alertness of a driver by analyzing their facial features using machine learning and computer vision techniques. With increasing road traffic and associated accidents due to driver fatigue, this system aims to provide a solution that enhances road safety by alerting drowsy drivers in real-time.

## Key Features
- **Face Detection**: Uses MediaPipe to detect the driver's face in real-time.
- **Eye Tracking**: Monitors eye openness and blink frequency to determine drowsiness levels.
- **Yawn Detection**: Detects yawning as an indicator of drowsiness.
- **Real-Time Alerts**: Provides immediate visual alerts when drowsiness is detected.
- **Webcam Integration**: Works with standard webcams for easy deployment.

## Technologies Used
- Python 3.8+
- OpenCV
- MediaPipe
- NumPy
- SciPy

## Installation Instructions

### Prerequisites
- Python 3.8 or higher
- Webcam connected to your system

### Step 1: Clone the Repository
```bash
git clone https://github.com/sars-23/real-time-drowsiness-detection.git
cd real-time-drowsiness-detection
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Required Packages
```bash
pip install -r requirements.txt
```

## Usage

### Running the Application
```bash
python main.py
```

The application will:
1. Open your webcam feed
2. Detect your face in real-time
3. Monitor eye closure and yawning patterns
4. Display alerts when drowsiness is detected
5. Press 'q' to quit the application

### Customizing Detection Parameters
You can adjust the following parameters in `main.py`:
- `EAR_THRESHOLD`: Eye Aspect Ratio threshold for detecting closed eyes
- `CONSECUTIVE_FRAMES`: Number of frames to confirm drowsiness
- `YAWN_THRESHOLD`: Mouth Aspect Ratio threshold for yawn detection

## How It Works

### Eye Aspect Ratio (EAR)
The system calculates the Eye Aspect Ratio using the distance between eyelids and the distance between eye corners. When this ratio drops below a threshold, it indicates the eyes are closed.

### Mouth Aspect Ratio (MAR)
The system monitors the Mouth Aspect Ratio to detect yawning, which is another indicator of drowsiness.

### Alert System
When drowsiness is detected (either through extended eye closure or yawning), the system displays a visual alert on the video feed.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any features, bug fixes, or improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer
This system is designed as an assistive tool and should not be relied upon as the sole method for preventing drowsy driving. Always prioritize road safety and take appropriate breaks during long drives.