import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe components
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# Function to compute Eye Aspect Ratio (EAR)
def calculate_ear(eye):
    A = np.linalg.norm(eye[1] - eye[5])  # distance between vertical eye landmarks
    B = np.linalg.norm(eye[2] - eye[4])  # distance between horizontal eye landmarks
    ear = A / B
    return ear

# Function to compute Mouth Aspect Ratio (MAR)
def calculate_mar(mouth):
    A = np.linalg.norm(mouth[2] - mouth[10])  # distance between top and bottom lip
    B = np.linalg.norm(mouth[3] - mouth[9])  # distance between left and right lip
    mar = A / B
    return mar

# Start capturing video
cap = cv2.VideoCapture(0)

# Set thresholds
EAR_THRESHOLD = 0.25
MAR_THRESHOLD = 0.5

with mp_face_mesh.FaceMesh(static_image_mode=False,
                            max_num_faces=1,
                            min_detection_confidence=0.5,
                            min_tracking_confidence=0.5) as face_mesh:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the BGR image to RGB
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(img_rgb)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(frame, face_landmarks, mp_face_mesh.FACE_CONNECTIONS)
                # Get landmarks for eyes and mouth
                left_eye = np.array([face_landmarks.landmark[33].x, face_landmarks.landmark[33].y], dtype='float32')
                right_eye = np.array([face_landmarks.landmark[159].x, face_landmarks.landmark[159].y], dtype='float32')
                mouth = np.array([[face_landmarks.landmark[i].x, face_landmarks.landmark[i].y] for i in [61, 291, 146, 84, 62, 291, 429, 62, 84, 146, 310]], dtype='float32')
                ear = calculate_ear([left_eye, right_eye])
                mar = calculate_mar(mouth)
                
                # Check for drowsiness
                if ear < EAR_THRESHOLD:
                    cv2.putText(frame, 'DROWSY!', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                
                # Check for yawning
                if mar > MAR_THRESHOLD:
                    cv2.putText(frame, 'YAWNING!', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Show the frame
        cv2.imshow('Drowsiness Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release video capture
cap.release()
cv2.destroyAllWindows()