import math
import cv2
import mediapipe as mp
import numpy as np
import pyttsx3
import threading
import queue


def sigmoid(x):
    sig = 1 / (1 + math.exp(-x))
    return sig


# To play audio text-to-speech during execution
class TTSThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.daemon = True
        self.start()

    def run(self):
        tts_engine = pyttsx3.init()
        tts_engine.startLoop(False)
        t_running = True
        while t_running:
            if self.queue.empty():
                tts_engine.iterate()
            else:
                data = self.queue.get()
                if data == "exit":
                    t_running = False
                else:
                    tts_engine.say(data)
        tts_engine.endLoop()


q = queue.Queue()
tts_thread = TTSThread(q)


def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle


def calculate_score(current_angle, target_angle):
    score = (1 / ((abs(abs(round(current_angle, 2)) - target_angle)) + 1)) * 100
    if score > 100:
        score = 100
    return score


def startExercise(exerciseName, target_angle, rep_count):
    if exerciseName == "wrist curl":
        # for pose
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        # for hands
        # mp_hand = mp.solutions.hands
        # hands = mp_hand.Hands(max_num_hands=2)

        cap = cv2.VideoCapture(0)
        # wrist_angle_wrist_curl = 130
        wrist_angle_wrist_curl = target_angle
        # Setup mediapipe instance
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()

                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Extract landmarks
                try:
                    landmarks = results.pose_landmarks.landmark
                    # Get coordinates
                    r_index = [landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].y]
                    l_index = [landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].x,
                               landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].y]

                    r_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                    l_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                               landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]

                    r_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                    l_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                               landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                    r_z_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].z
                    l_z_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].z

                    r_z_index = landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].z
                    l_z_index = landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].z

                    r_z_elbow = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].z
                    l_z_elbow = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].z

                    # the lower this number is the closer user is to the camera
                    averageDis = (r_z_wrist + l_z_wrist + r_z_elbow + l_z_elbow + r_z_index + l_z_index) / 6

                    # Calculate angle
                    angleAtRwrist = calculate_angle(r_elbow, r_wrist, r_index)
                    angleAtLwrist = calculate_angle(l_elbow, l_wrist, l_index)

                    # Visualize angle
                    if (angleAtLwrist == wrist_angle_wrist_curl or angleAtLwrist < wrist_angle_wrist_curl) and \
                            landmarks[
                                mp_pose.PoseLandmark.LEFT_WRIST.value].visibility > .5:
                        q.put("hold it right there you have perfect form")
                        cv2.putText(image, str("hold it right there perfect form"),
                                    tuple(np.multiply(l_wrist, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA
                                    )
                    else:
                        # clear queue of the text
                        with q.mutex:
                            q.queue.clear()
                        cv2.putText(image, str(angleAtLwrist),
                                    tuple(np.multiply(l_wrist, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                    )

                    if (angleAtRwrist == wrist_angle_wrist_curl or angleAtRwrist < wrist_angle_wrist_curl) and \
                            landmarks[
                                mp_pose.PoseLandmark.RIGHT_WRIST.value].visibility > .5:
                        q.put("hold it right there you have perfect form")
                        cv2.putText(image, str("hold it right there perfect form"),
                                    tuple(np.multiply(r_wrist, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA
                                    )
                    else:
                        # clear queue of the text
                        with q.mutex:
                            q.queue.clear()
                        cv2.putText(image, str(angleAtRwrist),
                                    tuple(np.multiply(r_wrist, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                    )
                    if averageDis > -0.7:
                        cv2.putText(image, str("Move closer"),
                                    (100, 50),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                    )
                    # scoring to if the there is no diff between wrist_angle_wrist_curl(ex_angle) then score is 100%
                    score = calculate_score(angleAtRwrist, wrist_angle_wrist_curl)
                    cv2.putText(image, "score: " + str(score),
                                (160, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )
                    print(score)
                    # print(landmarks)
                    print(averageDis)
                    print("angleAtRwrist " + str(angleAtRwrist))
                    print("angleAtLwrist " + str(angleAtLwrist))

                except:
                    pass

                # Render detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                          )
                # Plot Pose landmarks in 3D.
                # mp_drawing.plot_landmarks(results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)

                # for hands
                # if resultshands.multi_hand_landmarks:
                #     for handLms in resultshands.multi_hand_landmarks:
                #         mp_drawing.draw_landmarks(image, handLms, mp_hand.HAND_CONNECTIONS,
                #                                   mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2,
                #                                                          circle_radius=2),
                #                                   mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                #                                   )

                cv2.imshow('Exercise Feed', image)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
            return score * 100
    elif exerciseName == "thumb flex":
        # for pose
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.holistic
        # for hands
        # mp_hand = mp.solutions.hands
        # hands = mp_hand.Hands(max_num_hands=2)

        cap = cv2.VideoCapture(0)
        # angle_thumb_flex = 125
        angle_thumb_flex = target_angle
        # Setup mediapipe instance
        with mp_pose.Holistic(min_tracking_confidence=0.5, min_detection_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()

                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Extract landmarks
                try:
                    # todo do this for left hand too
                    landmarks = results.right_hand_landmarks.landmark
                    # Get coordinates
                    r_thumb_cmc = [landmarks[mp_pose.HandLandmark.THUMB_CMC.value].x,
                                   landmarks[mp_pose.HandLandmark.THUMB_CMC.value].y]

                    r_thumb_mcp = [landmarks[mp_pose.HandLandmark.THUMB_MCP.value].x,
                                   landmarks[mp_pose.HandLandmark.THUMB_MCP.value].y]

                    r_thumb_ip = [landmarks[mp_pose.HandLandmark.THUMB_IP.value].x,
                                  landmarks[mp_pose.HandLandmark.THUMB_IP.value].y]
                    # Calculate angle
                    angleAtRthumbMCP = calculate_angle(r_thumb_cmc, r_thumb_mcp, r_thumb_ip)

                    # r_z_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].z
                    # l_z_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].z
                    #
                    # r_z_index = landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].z
                    # l_z_index = landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].z
                    #
                    # r_z_elbow = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].z
                    # l_z_elbow = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].z
                    #
                    # # the lower this number is the closer user is to the camera
                    # averageDis = (r_z_wrist + l_z_wrist + r_z_elbow + l_z_elbow + r_z_index + l_z_index) / 6
                    #
                    # Visualize angle
                    if angleAtRthumbMCP == angle_thumb_flex or angleAtRthumbMCP < angle_thumb_flex:
                        q.put("hold it right there you have perfect form")
                        cv2.putText(image, str("hold it right there perfect form"),
                                    tuple(np.multiply(r_thumb_mcp, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA
                                    )
                    else:
                        # clear queue of the text
                        with q.mutex:
                            q.queue.clear()
                        cv2.putText(image, str(angleAtRthumbMCP),
                                    tuple(np.multiply(r_thumb_mcp, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                    # if (angleAtRwrist == wrist_angle_wrist_curl or angleAtRwrist < wrist_angle_wrist_curl) and \
                    #         landmarks[
                    #             mp_pose.PoseLandmark.RIGHT_WRIST.value].visibility > .5:
                    #     q.put("hold it right there you have perfect form")
                    #     cv2.putText(image, str("hold it right there perfect form"),
                    #                 tuple(np.multiply(r_wrist, [640, 480]).astype(int)),
                    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA
                    #                 )
                    # else:
                    #     # clear queue of the text
                    #     with q.mutex:
                    #         q.queue.clear()
                    #     cv2.putText(image, str(angleAtRwrist),
                    #                 tuple(np.multiply(r_wrist, [640, 480]).astype(int)),
                    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                    #                 )
                    # if averageDis > -0.7:
                    #     cv2.putText(image, str("Move closer"),
                    #                 (100, 50),
                    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                    #                 )
                    # scoring to if the there is no diff between (ex_angle) and performed ex then score is 100%
                    score = calculate_score(angleAtRthumbMCP, angle_thumb_flex)
                    cv2.putText(image, "score: " + str(score),
                                (160, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )
                    print(score)

                    # print(landmarks)
                    # print(averageDis)
                    print("angleAtRthumbMCP " + str(angleAtRthumbMCP))
                    # print("angleAtLwrist " + str(angleAtLwrist))

                except:
                    pass

                # Render detections
                mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_pose.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                          )
                # Plot Pose landmarks in 3D.
                # mp_drawing.plot_landmarks(results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)

                # for hands
                # if resultshands.multi_hand_landmarks:
                #     for handLms in resultshands.multi_hand_landmarks:
                #         mp_drawing.draw_landmarks(image, handLms, mp_hand.HAND_CONNECTIONS,
                #                                   mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2,
                #                                                          circle_radius=2),
                #                                   mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                #                                   )

                cv2.imshow('Exercise Feed', image)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
            return score * 100
    elif exerciseName == "squat":
        # for pose
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        # for hands
        # mp_hand = mp.solutions.hands
        # hands = mp_hand.Hands(max_num_hands=2)

        cap = cv2.VideoCapture(0)
        # knee_angle_squat = 90
        knee_angle_squat = target_angle
        # Setup mediapipe instance
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()

                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Extract landmarks
                try:
                    landmarks = results.pose_landmarks.landmark
                    # Get coordinates
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
                    # the lower this number is the closer user is to the camera
                    # averageDis = (r_z_wrist + l_z_wrist + r_z_elbow + l_z_elbow + r_z_index + l_z_index) / 6

                    # Calculate angle
                    angleAtRknee = calculate_angle(r_hip, r_knee, r_ankle)
                    angleAtLknee = calculate_angle(l_hip, l_knee, l_ankle)

                    # Visualize angle
                    if (angleAtRknee < knee_angle_squat) and \
                            landmarks[
                                mp_pose.PoseLandmark.RIGHT_KNEE.value].visibility > .5:
                        q.put("hold it right there you have perfect form")
                        cv2.putText(image, str("hold it right there perfect form"),
                                    tuple(np.multiply(r_knee, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA
                                    )
                    else:
                        # clear queue of the text
                        with q.mutex:
                            q.queue.clear()
                        cv2.putText(image, str(angleAtRknee),
                                    tuple(np.multiply(l_knee, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                    )

                    if (angleAtLknee < knee_angle_squat) and \
                            landmarks[
                                mp_pose.PoseLandmark.LEFT_KNEE.value].visibility > .5:
                        q.put("hold it right there you have perfect form")
                        cv2.putText(image, str("hold it right there perfect form"),
                                    tuple(np.multiply(l_knee, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA
                                    )
                    else:
                        # clear queue of the text
                        with q.mutex:
                            q.queue.clear()
                        cv2.putText(image, str(angleAtLknee),
                                    tuple(np.multiply(l_knee, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                    )
                    # if averageDis > -0.7:
                    #     cv2.putText(image, str("Move closer"),
                    #                 (100, 50),
                    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                    #                 )
                    # scoring to if the there is no diff between wrist_angle_wrist_curl(ex_angle) then score is 100%
                    score = calculate_score(angleAtRknee, knee_angle_squat)
                    cv2.putText(image, "score: " + str(score),
                                (160, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )
                    print(score)
                    # print(landmarks)
                    # print(averageDis)
                    print("angleAtRwrist " + str(angleAtRknee))
                    print("angleAtLwrist " + str(angleAtLknee))

                except:
                    pass

                # Render detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                          )

                cv2.imshow('Exercise Feed', image)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
            return score * 100
    elif exerciseName == "arm curl":
        # for pose
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose

        cap = cv2.VideoCapture(0)

        # Curl counter variables
        counter = 0
        stage = None

        # best_angle = 180
        best_angle = target_angle
        # Setup mediapipe instance
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()

                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Extract Landmarks
                try:
                    landmarks = results.pose_landmarks.landmark

                    # Get Coordinates
                    l_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                  landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                    l_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                               landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                    l_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                               landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                    # calculate angle
                    angle = calculate_angle(l_shoulder, l_elbow, l_wrist)
                    # calculate best angle of the session
                    if angle < best_angle:
                        best_angle = angle

                    # visualize angle
                    cv2.putText(image, str(angle), tuple(np.multiply(l_elbow, [640, 480]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                    # Curl counter logic
                    if angle > 150.0:
                        stage = "down"
                    if angle < 40.0 and stage == 'down':
                        stage = "up"
                        counter += 1
                        print(counter)

                except:
                    pass

                # Render Curl Counter
                # Setup status box
                cv2.rectangle(image, (0, 0), (255, 73), (244, 117, 16), -1)

                # Rep data
                cv2.putText(image, 'REPS', (15, 12),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(counter),
                            (10, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

                # Stage data
                cv2.putText(image, 'STAGE', (65, 12),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(stage),
                            (60, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

                # Render Detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))

                cv2.imshow("Exercise Feed", image)
                if (cv2.waitKey(10) & 0xFF == ord('q')) or counter > rep_count:
                    break
            cap.release()
            cv2.destroyAllWindows()
            print("best angle was " + str(best_angle))

    elif exerciseName == "jumping jacks":
        q.put("start doing jumping jacks")
        # target angle for this exercise
        jumping_jacks_target_angle = target_angle
        # for pose
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose

        cap = cv2.VideoCapture(0)
        # Setup mediapipe instance
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()

                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Extract landmarks
                try:
                    landmarks = results.pose_landmarks.landmark
                    # Get coordinates

                    r_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                    l_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                               landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]

                    r_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                  landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                    l_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                  landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]

                    r_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                             landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                    l_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                             landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

                    # Calculate angle
                    angleAtRShoulder = calculate_angle(r_hip, r_elbow, r_shoulder)
                    angleAtLShoulder = calculate_angle(l_hip, l_elbow, l_shoulder)

                    # Visualize angle
                    if angleAtRShoulder > 60:
                        # q.put("do jumping jacks")
                        cv2.putText(image, str("do jumping jacks"),
                                    tuple(np.multiply(r_shoulder, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA
                                    )
                    else:
                        # clear queue of the text
                        with q.mutex:
                            q.queue.clear()
                        cv2.putText(image, str(angleAtRShoulder),
                                    tuple(np.multiply(r_shoulder, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                    )

                    if angleAtLShoulder > 60:
                        # q.put("do jumping jacks")
                        cv2.putText(image, str("do jumping jacks"),
                                    tuple(np.multiply(l_shoulder, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
                    else:
                        # clear queue of the text
                        with q.mutex:
                            q.queue.clear()
                        cv2.putText(image, str(angleAtLShoulder),
                                    tuple(np.multiply(l_shoulder, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                    )
                    # if averageDis > -0.7:
                    #     cv2.putText(image, str("Move closer"),
                    #                 (100, 50),
                    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                    #                 )
                    # scoring to if the there is no diff between wrist_angle_wrist_curl(ex_angle) then score is 100%
                    score = calculate_score(angleAtRShoulder, jumping_jacks_target_angle)
                    cv2.putText(image, "score: " + str(round(score, 2)),
                                (160, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )
                    print(score)
                    # print(averageDis)
                    print("angleAtRwrist " + str(angleAtRShoulder))
                    # print("angleAtLwrist " + str(angleAtLShoulder))

                except:
                    pass

                # Render detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                          )

                cv2.imshow('Exercise Feed', image)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
            score*100
    elif exerciseName == "high knee":
        # for pose
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose

        cap = cv2.VideoCapture(0)
        # Setup mediapipe instance
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()

                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Extract landmarks
                try:
                    landmarks = results.pose_landmarks.landmark
                    # Get coordinates

                    r_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                             landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                    l_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                             landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

                    r_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                              landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                    l_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]

                    if r_knee[1] > r_hip[1] and l_knee[1] > l_hip[1]:
                        q.put("Raise either right or left leg")
                        cv2.putText(image, str("Raise either right or left leg"),
                                    tuple(np.multiply(r_hip, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
                    else:
                        # clear queue of the text
                        with q.mutex:
                            q.queue.clear()

                    if r_knee[1] < r_hip[1] or l_knee[1] < l_hip[1]:
                        q.put("Good job!")
                        cv2.putText(image, str("Good job!"),
                                    tuple(np.multiply(r_hip, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
                        cv2.putText(image, str("Good job!"),
                                    tuple(np.multiply(l_hip, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
                    else:
                        # clear queue of the text
                        with q.mutex:
                            q.queue.clear()

                    score = 0
                    if r_knee[1] < r_hip[1]:
                        score = (r_hip[1] - r_knee[1]) / 0.001
                    if l_knee[1] < l_hip[1]:
                        score = (l_hip[1] - l_knee[1]) / 0.001
                    if score > 100:
                        score = 100
                    cv2.putText(image, "score: " + str(score), (160, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2, cv2.LINE_AA
                                )
                    print(score)

                except:
                    pass

                # Render detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                          )

                cv2.imshow('Exercise Feed', image)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
            score*100
    elif exerciseName == "shoulder shrug":
        # for pose
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose

        cap = cv2.VideoCapture(0)
        # Setup mediapipe instance
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()

                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Extract landmarks
                try:
                    landmarks = results.pose_landmarks.landmark
                    # Get coordinates
                    # todo wrong landmarks
                    nose = [landmarks[mp_pose.PoseLandmark.NOSE.value].x,
                            landmarks[mp_pose.PoseLandmark.NOSE.value].y]
                    print("Nose:", landmarks[mp_pose.PoseLandmark.NOSE.value].z)
                    r_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                  landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                    l_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                  landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]

                    angle = calculate_angle(r_shoulder, nose, l_shoulder)

                    if angle < 13.6:
                        q.put("Raise both shoulders")
                        cv2.putText(image, str("Raise both shoulders"),
                                    tuple(np.multiply(r_shoulder, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
                    else:
                        # clear queue of the text
                        with q.mutex:
                            q.queue.clear()

                    if angle >= 13.6:
                        q.put("Good job! Now bring them back down.")
                        cv2.putText(image, str("Good job! Now bring them back down."),
                                    tuple(np.multiply(r_shoulder, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
                    else:
                        # clear queue of the text
                        with q.mutex:
                            q.queue.clear()

                    score = angle
                    if score > 100:
                        score = 100
                    cv2.putText(image, "score: " + str(score), (160, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2, cv2.LINE_AA
                                )
                    print(score)

                except:
                    pass

                # Render detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                          )

                cv2.imshow('Exercise Feed', image)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
            return score * 100
    elif exerciseName == "lateral raises":
        # for pose
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        # lateral_raises_target_angle = 80
        lateral_raises_target_angle = target_angle
        cap = cv2.VideoCapture(0)
        # Setup mediapipe instance
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()

                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Extract landmarks
                try:
                    landmarks = results.pose_landmarks.landmark
                    # Get coordinates

                    r_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                    l_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                               landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]

                    r_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                  landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                    l_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                  landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]

                    r_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                             landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                    l_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                             landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

                    # Calculate angle
                    angleAtRShoulder = calculate_angle(r_hip, r_elbow, r_shoulder)
                    angleAtLShoulder = calculate_angle(l_hip, l_elbow, l_shoulder)

                    # Visualize angle
                    if angleAtRShoulder > 80 or angleAtLShoulder > 80:
                        q.put("Raise both arms to the shoulders")
                        cv2.putText(image, str("Raise both arms to the shoulders"),
                                    tuple(np.multiply(r_shoulder, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA
                                    )
                    else:
                        # clear queue of the text
                        with q.mutex:
                            q.queue.clear()

                    if angleAtRShoulder <= 80 and angleAtLShoulder <= 80:
                        q.put("Good job! Now bring both arms down.")
                        cv2.putText(image, str("Good job! Now bring both arms down."),
                                    tuple(np.multiply(r_shoulder, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA
                                    )
                    else:
                        # clear queue of the text
                        with q.mutex:
                            q.queue.clear()
                    # todo change this scoring method it does not work after testing
                    score = calculate_score(angleAtRShoulder, lateral_raises_target_angle)
                    cv2.putText(image, "score: " + str(score),
                                (160, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA
                                )
                    print(score)


                except:
                    pass

                # Render detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                          )

                cv2.imshow('Exercise Feed', image)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
            return score * 100
    elif exerciseName == "quad stretch":
        # for pose
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        # for hands
        # mp_hand = mp.solutions.hands
        # hands = mp_hand.Hands(max_num_hands=2)

        cap = cv2.VideoCapture(0)
        # Setup mediapipe instance
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()

                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Extract landmarks
                try:
                    landmarks = results.pose_landmarks.landmark
                    # Get coordinates

                    r_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                    l_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                               landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                    r_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
                    l_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                               landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

                    print("Right: " + str(sum([r_wrist[0] - r_ankle[0], r_wrist[1] - r_ankle[1]])))
                    print("Left: " + str(sum([l_wrist[0] - l_ankle[0], l_wrist[1] - l_ankle[1]])))

                    # Visualize angle
                    if (abs(sum([r_wrist[0] - r_ankle[0], r_wrist[1] - r_ankle[1]])) < 0.2 or abs(
                            sum([l_wrist[0] - l_ankle[0], l_wrist[1] - l_ankle[1]])) < 0.2):
                        q.put("Hold it right there, you have perfect form")
                        cv2.putText(image, str("Hold it right there, you have perfect form"),
                                    tuple(np.multiply(r_wrist, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA
                                    )
                    else:
                        # clear queue of the text
                        with q.mutex:
                            q.queue.clear()
                    if (abs(sum([r_wrist[0] - r_ankle[0], r_wrist[1] - r_ankle[1]])) > 0.2 and abs(
                            sum([l_wrist[0] - l_ankle[0], l_wrist[1] - l_ankle[1]])) > 0.2):
                        q.put("Bring your ankle to your wrist")
                        cv2.putText(image, str("Bring your ankle to your wrist"),
                                    tuple(np.multiply(r_wrist, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA
                                    )
                    else:
                        # clear queue of the text
                        with q.mutex:
                            q.queue.clear()

                    score = round(10 / abs(sum([r_wrist[0] - r_ankle[0], r_wrist[1] - r_ankle[1]])) + 10 / abs(
                        sum([l_wrist[0] - l_ankle[0], l_wrist[1] - l_ankle[1]])), 1)
                    if score > 100:
                        score = 100
                    cv2.putText(image, "score: " + str(score),
                                (160, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )


                except:
                    pass

                # Render detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                          )

                cv2.imshow('Exercise Feed', image)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
            return score*100
    return exerciseName


def distanceBetweenTwoLandmarks(mark1, mark2):
    dist = math.sqrt((mark2[0] - mark1[0]) ** 2 + (mark2[1] - mark1[1]) ** 2)
    return dist


def sessionExercise(exerciseName):
    # todo add scoring for thumb touch
    if exerciseName == "thumb touch":
        # for pose
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.holistic
        noOfFrames = 0
        distance_between_r_thumb_r_index = 0
        distance_between_r_thumb_r_middle = 0
        distance_between_r_thumb_r_ring = 0
        distance_between_r_thumb_r_pinky = 0
        cap = cv2.VideoCapture(0)
        # Setup mediapipe instance
        with mp_pose.Holistic(min_tracking_confidence=0.5, min_detection_confidence=0.5, ) as pose:
            while cap.isOpened():
                ret, frame = cap.read()
                h, w, c = frame.shape
                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                noOfFrames = noOfFrames + 1
                # Extract landmarks
                try:
                    # todo do this for left hand too
                    landmarks = results.right_hand_landmarks.landmark
                    # todo move this to if statement if we get low frames per second
                    # Get coordinates
                    r_thumb_tip = [landmarks[mp_pose.HandLandmark.THUMB_TIP.value].x,
                                   landmarks[mp_pose.HandLandmark.THUMB_TIP.value].y]

                    r_index_tip = [landmarks[mp_pose.HandLandmark.INDEX_FINGER_TIP.value].x,
                                   landmarks[mp_pose.HandLandmark.INDEX_FINGER_TIP.value].y]

                    r_middle_tip = [landmarks[mp_pose.HandLandmark.MIDDLE_FINGER_TIP.value].x,
                                    landmarks[mp_pose.HandLandmark.MIDDLE_FINGER_TIP.value].y]
                    r_ring_tip = [landmarks[mp_pose.HandLandmark.RING_FINGER_TIP.value].x,
                                  landmarks[mp_pose.HandLandmark.RING_FINGER_TIP.value].y]
                    r_pinky_tip = [landmarks[mp_pose.HandLandmark.PINKY_TIP.value].x,
                                   landmarks[mp_pose.HandLandmark.PINKY_TIP.value].y]

                    # for first 100 frames user will do index and thumb and then move to other finger
                    if noOfFrames < 100:
                        # convert normalized landmarks to pixel coordinates
                        none_normalized_r_index_tip = mp_drawing._normalized_to_pixel_coordinates(image_width=w,
                                                                                                  image_height=h,
                                                                                                  normalized_x=
                                                                                                  r_index_tip[
                                                                                                      0],
                                                                                                  normalized_y=
                                                                                                  r_index_tip[
                                                                                                      1])
                        none_normalized_r_thumb_tip = mp_drawing._normalized_to_pixel_coordinates(image_width=w,
                                                                                                  image_height=h,
                                                                                                  normalized_x=
                                                                                                  r_thumb_tip[
                                                                                                      0],
                                                                                                  normalized_y=
                                                                                                  r_thumb_tip[
                                                                                                      1])
                        distance_between_r_thumb_r_index = distanceBetweenTwoLandmarks(
                            none_normalized_r_index_tip,
                            none_normalized_r_thumb_tip)

                        image = cv2.line(image, none_normalized_r_index_tip,
                                         none_normalized_r_thumb_tip,
                                         thickness=2, color=(0, 255, 0))
                        cv2.putText(image, str(distance_between_r_thumb_r_index),
                                    tuple(np.multiply(r_index_tip, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA
                                    )
                    elif noOfFrames < 200:
                        none_normalized_r_middle_tip = mp_drawing._normalized_to_pixel_coordinates(image_width=w,
                                                                                                   image_height=h,
                                                                                                   normalized_x=
                                                                                                   r_middle_tip[
                                                                                                       0],
                                                                                                   normalized_y=
                                                                                                   r_middle_tip[
                                                                                                       1])
                        none_normalized_r_thumb_tip = mp_drawing._normalized_to_pixel_coordinates(image_width=w,
                                                                                                  image_height=h,
                                                                                                  normalized_x=
                                                                                                  r_thumb_tip[
                                                                                                      0],
                                                                                                  normalized_y=
                                                                                                  r_thumb_tip[
                                                                                                      1])
                        distance_between_r_thumb_r_middle = distanceBetweenTwoLandmarks(
                            none_normalized_r_middle_tip,
                            none_normalized_r_thumb_tip)

                        image = cv2.line(image, none_normalized_r_middle_tip,
                                         none_normalized_r_thumb_tip,
                                         thickness=2, color=(0, 255, 0))
                        cv2.putText(image, str(distance_between_r_thumb_r_middle),
                                    tuple(np.multiply(r_middle_tip, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA
                                    )
                    elif noOfFrames < 300:
                        none_normalized_r_ring_tip = mp_drawing._normalized_to_pixel_coordinates(image_width=w,
                                                                                                 image_height=h,
                                                                                                 normalized_x=
                                                                                                 r_ring_tip[
                                                                                                     0],
                                                                                                 normalized_y=
                                                                                                 r_ring_tip[
                                                                                                     1])
                        none_normalized_r_thumb_tip = mp_drawing._normalized_to_pixel_coordinates(image_width=w,
                                                                                                  image_height=h,
                                                                                                  normalized_x=
                                                                                                  r_thumb_tip[
                                                                                                      0],
                                                                                                  normalized_y=
                                                                                                  r_thumb_tip[
                                                                                                      1])
                        distance_between_r_thumb_r_ring = distanceBetweenTwoLandmarks(
                            none_normalized_r_ring_tip,
                            none_normalized_r_thumb_tip)

                        image = cv2.line(image, none_normalized_r_ring_tip,
                                         none_normalized_r_thumb_tip,
                                         thickness=2, color=(0, 255, 0))
                        cv2.putText(image, str(distance_between_r_thumb_r_ring),
                                    tuple(np.multiply(r_ring_tip, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA
                                    )
                    elif noOfFrames < 400:
                        none_normalized_r_pinky_tip = mp_drawing._normalized_to_pixel_coordinates(image_width=w,
                                                                                                  image_height=h,
                                                                                                  normalized_x=
                                                                                                  r_pinky_tip[
                                                                                                      0],
                                                                                                  normalized_y=
                                                                                                  r_pinky_tip[
                                                                                                      1])
                        none_normalized_r_thumb_tip = mp_drawing._normalized_to_pixel_coordinates(image_width=w,
                                                                                                  image_height=h,
                                                                                                  normalized_x=
                                                                                                  r_thumb_tip[
                                                                                                      0],
                                                                                                  normalized_y=
                                                                                                  r_thumb_tip[
                                                                                                      1])
                        distance_between_r_thumb_r_pinky = distanceBetweenTwoLandmarks(
                            none_normalized_r_pinky_tip,
                            none_normalized_r_thumb_tip)

                        image = cv2.line(image, none_normalized_r_pinky_tip,
                                         none_normalized_r_thumb_tip,
                                         thickness=2, color=(0, 255, 0))
                        cv2.putText(image, str(distance_between_r_thumb_r_pinky),
                                    tuple(np.multiply(r_pinky_tip, [640, 480]).astype(int)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA
                                    )
                except:
                    pass

                # Render detections
                mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_pose.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                          )
                cv2.imshow('Exercise Feed', image)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
            print(noOfFrames)
            print("distances")
            print(distance_between_r_thumb_r_index)
            print(distance_between_r_thumb_r_middle)
            print(distance_between_r_thumb_r_ring)
            print(distance_between_r_thumb_r_pinky)

# exerciseNames = ["wrist curl", "thumb flex", "squat", "arm curl", "jumping jacks", "high knee", "shoulder shrug",
# "lateral raises", "quad stretch"]
# name = startExercise(str(exerciseNames[6]))
# print(name)
# sessionExercise("thumb touch")
