import cv2
import mediapipe as mp
import numpy as np
import json

# for pose
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.holistic
# for hands
mp_hand = mp.solutions.hands
hands = mp_hand.Hands(max_num_hands=2)


def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle


makeJson = False
name = "thumb flex"
exercise_info = {}

cap = cv2.imread(name + ".jpeg")
## Setup mediapipe instance
with mp_pose.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5, static_image_mode=True, ) as pose:
    frame = cap

    # Recolor image to RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False

    # Make detection
    results = pose.process(image)
    resultshands = hands.process(image)

    # Recolor back to BGR
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Extract landmarks
    try:
        landmarks = results.pose_landmarks.landmark
        # Get coordinates
        r_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                      landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
        l_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                      landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]

        r_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                   landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
        l_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                   landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]

        r_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                   landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
        l_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                   landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

        r_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                 landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
        l_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                 landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

        r_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                  landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
        l_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                  landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]

        r_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                   landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
        l_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                   landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

        r_foot_index = [landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].x,
                        landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].y]
        l_foot_index = [landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].y]

        # # Calculate angle
        angleAtRelbow = calculate_angle(r_shoulder, r_elbow, r_wrist)
        angleAtLelbow = calculate_angle(l_shoulder, l_elbow, l_wrist)

        angleAtRshoulder = calculate_angle(r_hip, r_shoulder, l_elbow)
        angleAtLshoulder = calculate_angle(l_hip, l_shoulder, l_elbow)

        angleAtRhip = calculate_angle(r_shoulder, r_hip, r_knee)
        angleAtLhip = calculate_angle(l_shoulder, l_hip, l_knee)

        angleAtRknee = calculate_angle(r_hip, r_knee, r_ankle)
        angleAtLknee = calculate_angle(l_hip, l_knee, l_ankle)

        angleAtRankle = calculate_angle(r_knee, r_ankle, r_foot_index)
        angleAtLankle = calculate_angle(l_knee, l_ankle, l_foot_index)

        # making dic to save exercise as json
        exercise_info[name] = {
            "angleAtRelbow": angleAtRelbow,
            "angleAtLelbow": angleAtLelbow,

            "angleAtRshoulder": angleAtRshoulder,
            "angleAtLshoulder": angleAtLshoulder,

            "angleAtRhip": angleAtRhip,
            "angleAtLhip": angleAtLhip,

            "angleAtRknee": angleAtRknee,
            "angleAtLknee": angleAtLknee,

            "angleAtRankle": angleAtRankle,
            "angleAtLankle": angleAtLankle,

        }
        # angle3 = calculate_angle(r_hip, r_shoulder, r_elbow)

        # Visualize angle
        # cv2.putText(image, str(angle),
        #             tuple(np.multiply(elbow, [640, 480]).astype(int)),
        #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
        #             )
        # Visualize angle
        # cv2.putText(image, str(angle2),
        #             tuple(np.multiply(r_elbow, [640, 480]).astype(int)),
        #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
        #             )
        # Visualize angle
        # cv2.putText(image, str(angle3),
        #             tuple(np.multiply(r_shoulder, [640, 480]).astype(int)),
        #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
        #             )
        print(landmarks)
        print("angleAtRelbow " + str(angleAtRelbow))
        print("angleAtLelbow " + str(angleAtLelbow))

        print("angleAtRshoulder " + str(angleAtRshoulder))
        print("angleAtLshoulder " + str(angleAtLshoulder))

        print("angleAtRhip " + str(angleAtRhip))
        print("angleAtLhip " + str(angleAtLhip))

        print("angleAtRknee " + str(angleAtRknee))
        print("angleAtLknee " + str(angleAtLknee))

        print("angleAtRankle " + str(angleAtRankle))
        print("angleAtLankle " + str(angleAtLankle))

        if makeJson:
            with open(name + '.json', 'w') as f:
                json.dump(exercise_info, f)
    except:
        pass

    # Render detections
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                              mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                              mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                              )
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_pose.HAND_CONNECTIONS,
                              mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                              mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                              )
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_pose.HAND_CONNECTIONS,
                              mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                              mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                              )
    # for hands
    if resultshands.multi_hand_landmarks:
        for handLms in resultshands.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, handLms, mp_hand.HAND_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                      )

while True:
    cv2.imshow('Mediapipe Feed', image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
#     cap.release()
#     cv2.destroyAllWindows()
