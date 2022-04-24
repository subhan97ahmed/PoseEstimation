import cv2
import mediapipe as mp
import numpy as np
import pyttsx3
import threading
import queue


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


def scoreExercise(name):
    # for wrist curl
    if name == "wrist curl":
        # for pose
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        # for hands
        mp_hand = mp.solutions.hands
        hands = mp_hand.Hands(max_num_hands=2)

        cap = cv2.VideoCapture(0)
        wrist_angle_wrist_curl = 130
        ## Setup mediapipe instance
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
                    score = (1 / ((abs(abs(round(angleAtRwrist, 2)) - wrist_angle_wrist_curl)) + 1)) * 100
                    if score > 100:
                        score = 100
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

                cv2.imshow('Mediapipe Feed', image)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
    elif name == "thumb flex":
        # for pose
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.holistic
        # for hands
        # mp_hand = mp.solutions.hands
        # hands = mp_hand.Hands(max_num_hands=2)

        cap = cv2.VideoCapture(0)
        angle_thumb_flex = 135
        ## Setup mediapipe instance
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
                    score = (1 / ((abs(abs(round(angleAtRthumbMCP, 2)) - angle_thumb_flex)) + 1)) * 100
                    if score > 100:
                        score = 100
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

                cv2.imshow('Mediapipe Feed', image)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
    elif name == "squat":
        # for pose
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        # for hands
        mp_hand = mp.solutions.hands
        hands = mp_hand.Hands(max_num_hands=2)

        cap = cv2.VideoCapture(0)
        knee_angle_squat = 90
        ## Setup mediapipe instance
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
                    score = (1 / ((abs(abs(round(angleAtRknee, 2)) - knee_angle_squat)) + 1)) * 100
                    if score > 100:
                        score = 100
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

                cv2.imshow('Mediapipe Feed', image)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()

    elif name == "arm curl":
        # for pose
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose

        cap = cv2.VideoCapture(0)

        # Curl counter variables
        counter = 0
        stage = None

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

                    # visualize angle

                    cv2.putText(image, str(angle), tuple(np.multiply(l_elbow, [640, 480]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                    print(str(angle))
                    print(type(angle))
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

                cv2.imshow("Mediapipe Feed", image)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()


exerciseNames = ["wrist curl", "thumb flex", "squat", "arm curl"]
scoreExercise(str(exerciseNames[3]))
