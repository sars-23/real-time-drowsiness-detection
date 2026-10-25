# Real-Time Drowsiness Detection

An experimental computer-vision prototype that uses a webcam and MediaPipe Face Mesh landmarks to display visual `DROWSY!` and `YAWNING!` messages. It is a learning project, not a validated driver-safety system and must not be relied on to make driving decisions.

## How it works

For one detected face, the application calculates:

- Eye Aspect Ratio (EAR) from six landmarks around each eye, then averages both eyes. When the value is below the configured threshold, it draws `DROWSY!`.
- Mouth Aspect Ratio (MAR) from six mouth landmarks. When the value is above the configured threshold, it draws `YAWNING!`.

The default thresholds are `0.25` for EAR and `0.5` for MAR. Each frame is evaluated independently; there is no blink counter, temporal smoothing, audio alert, or model calibration.

## Setup and run

Requirements: Python 3.11, a supported webcam, and a graphical desktop session.

```bash
git clone https://github.com/sars-23/real-time-drowsiness-detection.git
cd real-time-drowsiness-detection
python -m venv .venv
```

Activate the environment (`.venv\\Scripts\\activate` on Windows, or `source .venv/bin/activate` on macOS/Linux), then install and run:

```bash
python -m pip install -r requirements.txt
python main.py
```

Press `q` in the video window to quit. Choose a different webcam or thresholds if needed:

```bash
python main.py --camera 1 --ear-threshold 0.25 --mar-threshold 0.5
```

## Development checks

The reusable measurement functions are in `geometry.py`; importing them does not open a camera or GUI.

```bash
python -m py_compile main.py geometry.py
python -m unittest -v
```

## Limitations

Landmark quality depends on lighting, pose, camera quality, obstructions, and the fitted face. The thresholds are not calibrated per person or environment. The project only displays on-screen messages and does not detect every form of fatigue, distraction, or impairment.
