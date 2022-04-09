from tkinter import *

import cv2
from PIL import Image, ImageTk
import threading
# import imageio
import  mediapipe as mp
# create instance for window
root = Tk()
# set window title
root.title('Video Player')
# read video
# video = imageio.get_reader('snake_game.mp4')
cap = cv2.VideoCapture(0)
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


def display_video(label):
    # iterate through video data
    while cap.isOpened():
        # convert array into image
        ret, frame = cap.read()

        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                # cv2image = cv2.cvtColor(cv2image, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                  )

        img = Image.fromarray(image)
        # Convert image to PhotoImage
        image_frame = ImageTk.PhotoImage(image=img)
        # configure video to the label
        label.config(image=image_frame)
        label.image = image_frame


# create label for video
video_label = Label(root)
video_label.pack()
# create and start thread
thread = threading.Thread(target=display_video, args=(video_label,))
thread.start()
root.mainloop()


# # Import required Libraries
# from tkinter import *
# from PIL import Image, ImageTk
# import cv2
# import mediapipe as mp
#
# # Create an instance of TKinter Window or frame
# win = Tk()
#
# # Set the size of the window
# win.geometry("700x350")
#
# # Create a Label to capture the Video frames
# label = Label(win)
# label.grid(row=0, column=0)
# cap = cv2.VideoCapture(0)
# mp_drawing = mp.solutions.drawing_utils
# mp_pose = mp.solutions.pose
#
#
# # Define function to show frame
# def show_frames():
#     # Get the latest frame and convert into Image
#     cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
#
#     with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
#         # Recolor image to RGB
#         # image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         cv2image.flags.writeable = False
#
#         # Make detection
#         results = pose.process(cv2image)
#
#         # Recolor back to BGR
#         # cv2image.flags.writeable = True
#         # cv2image = cv2.cvtColor(cv2image, cv2.COLOR_RGB2BGR)
#         mp_drawing.draw_landmarks(cv2image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
#                                   mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
#                                   mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
#                                   )
#     img = Image.fromarray(cv2image)
#     # Convert image to PhotoImage
#     imgtk = ImageTk.PhotoImage(image=img)
#     label.imgtk = imgtk
#     label.configure(image=imgtk)
#     # Repeat after an interval to capture continiously
#     label.after(20, show_frames)
#
#
# show_frames()
# win.mainloop()
