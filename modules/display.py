import cv2


class Display:

    def show_info(
        self,
        frame,
        expression,
        answer
    ):

        height = frame.shape[0]
        width = frame.shape[1]

        panel_height = 70

        cv2.rectangle(
            frame,
            (0, height - panel_height),
            (width, height),
            (30, 30, 30),
            -1
        )

        title = "Smart Air Math Solver"

        title_size = cv2.getTextSize(
            title,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            2
        )[0]

        title_x = (
            width - title_size[0]
        ) // 2

        cv2.putText(
            frame,
            title,
            (title_x, height - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            f"Equation: {expression}",
            (40, height - 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

        answer_text = f"Answer: {answer}"

        answer_size = cv2.getTextSize(
            answer_text,
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            2
        )[0]

        cv2.putText(
            frame,
            answer_text,
            (
                width - answer_size[0] - 15,
                height - 40
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        return frame