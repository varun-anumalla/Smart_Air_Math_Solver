import cv2
import mediapipe as mp

from mediapipe.tasks.python import vision
from mediapipe.tasks.python import BaseOptions


class HandTracker:

    def __init__(self):

        options = vision.HandLandmarkerOptions(
            base_options=BaseOptions(
                model_asset_path="modules/hand_landmarker.task"
            ),
            num_hands=1
        )

        self.landmarker = vision.HandLandmarker.create_from_options(
            options
        )

    def detect(self, frame):

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        result = self.landmarker.detect(mp_image)

        x = None
        y = None
        is_drawing = False

        if result.hand_landmarks:

            hand = result.hand_landmarks[0]

            index_tip = hand[8]
            thumb_tip = hand[4]

            distance = (
                (index_tip.x - thumb_tip.x) ** 2 +
                (index_tip.y - thumb_tip.y) ** 2
            ) ** 0.5

            is_drawing = distance > 0.08

            h, w, _ = frame.shape

            x = int(index_tip.x * w)
            y = int(index_tip.y * h)

            cv2.circle(
                frame,
                (x, y),
                10,
                (0, 0, 255),
                -1
            )

            status = "DRAW" if is_drawing else "STOP"

            cv2.putText(
                frame,
                status,
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

        return frame, x, y, is_drawing