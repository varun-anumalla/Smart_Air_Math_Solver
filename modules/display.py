import cv2


class Display:

    def show_answer(
        self,
        frame,
        answer
    ):

        cv2.rectangle(
            frame,
            (0, 50),
            (300, 100),
            (0, 0, 0),
            -1
        )

        cv2.putText(
            frame,
            f"Answer: {answer}",
            (10, 85),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        return frame