"""Experimental webcam prototype using MediaPipe face landmarks."""
import argparse

from geometry import calculate_ear, calculate_mar

LEFT_EYE = (33, 160, 158, 133, 153, 144)
RIGHT_EYE = (362, 385, 387, 263, 373, 380)
MOUTH = (13, 14, 82, 87, 78, 308)


def landmarks_at(face_landmarks, indices):
    return [(face_landmarks.landmark[index].x, face_landmarks.landmark[index].y) for index in indices]


def run(camera_index, ear_threshold, mar_threshold):
    import cv2
    import mediapipe as mp

    capture = cv2.VideoCapture(camera_index)
    if not capture.isOpened():
        capture.release()
        raise RuntimeError(f"Could not open camera {camera_index}.")

    face_mesh_module = mp.solutions.face_mesh
    drawing = mp.solutions.drawing_utils
    try:
        with face_mesh_module.FaceMesh(
            static_image_mode=False, max_num_faces=1,
            min_detection_confidence=0.5, min_tracking_confidence=0.5,
        ) as face_mesh:
            while True:
                ok, frame = capture.read()
                if not ok:
                    break
                results = face_mesh.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                if results.multi_face_landmarks:
                    face = results.multi_face_landmarks[0]
                    drawing.draw_landmarks(frame, face, face_mesh_module.FACEMESH_TESSELATION)
                    ear = (calculate_ear(landmarks_at(face, LEFT_EYE)) + calculate_ear(landmarks_at(face, RIGHT_EYE))) / 2
                    mar = calculate_mar(landmarks_at(face, MOUTH))
                    if ear < ear_threshold:
                        cv2.putText(frame, "DROWSY!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    if mar > mar_threshold:
                        cv2.putText(frame, "YAWNING!", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                cv2.imshow("Drowsiness Detection", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
    finally:
        capture.release()
        cv2.destroyAllWindows()


def main():
    parser = argparse.ArgumentParser(description="Experimental MediaPipe drowsiness prototype")
    parser.add_argument("--camera", type=int, default=0, help="webcam index (default: 0)")
    parser.add_argument("--ear-threshold", type=float, default=0.25)
    parser.add_argument("--mar-threshold", type=float, default=0.5)
    args = parser.parse_args()
    run(args.camera, args.ear_threshold, args.mar_threshold)


if __name__ == "__main__":
    main()
