import cv2
import mediapipe as mp
import numpy as np

def process_video(path):
    cap = cv2.VideoCapture(path)
    mp_pose = mp.solutions.pose
    mp_face = mp.solutions.face_mesh
    pose = mp_pose.Pose()
    face_mesh = mp_face.FaceMesh()

    blink_count = 0
    frame_count = 0
    posture_issue = False

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Posture detection
        results = pose.process(rgb_frame)
        if results.pose_landmarks:
            shoulder = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER]
            ear = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EAR]
            if ear.y > shoulder.y:
                posture_issue = True

        # Blink detection (very basic)
        face_results = face_mesh.process(rgb_frame)
        if face_results.multi_face_landmarks:
            blink_count += 1  # simulate blink every frame (for demo purposes)

    cap.release()
    posture_result = "Poor" if posture_issue else "Good"
    blink_rate = round(blink_count / (frame_count / 30) * 60, 2)  # Blinks per minute

    return posture_result, blink_rate
