import cv2
import os

from modules.hand_tracker import HandTracker
from modules.canvas import Canvas
from modules.ocr_engine import OCREngine
from modules.math_evaluator import MathEvaluator
from modules.display import Display

cap = cv2.VideoCapture(0)

tracker = HandTracker()
canvas = Canvas()
ocr = OCREngine()
evaluator = MathEvaluator()
display = Display()

expression = ""
answer = ""

os.makedirs("saved_drawings", exist_ok=True)

save_count = 1

TOOLBAR_HEIGHT = 40

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    # ======================
    # TOOLBAR
    # ======================

    buttons = [
        ("SOLVE", (150, 150, 150)),
        ("CLEAR", (50, 50, 50)),
        ("ERASER", (100, 100, 100)),
        ("WHITE", (255, 255, 255)),
        ("YELLOW", (0, 255, 255)),
        ("BLUE", (255, 0, 0)),
        ("GREEN", (0, 255, 0)),
        ("RED", (0, 0, 255))
    ]

    button_width = 80

    for i, (name, color) in enumerate(buttons):

        x1 = i * button_width
        x2 = x1 + button_width

        cv2.rectangle(
            frame,
            (x1, 0),
            (x2, TOOLBAR_HEIGHT),
            color,
            -1
        )

        text_color = (0, 0, 0)

        if name in [
            "RED",
            "GREEN",
            "BLUE",
            "CLEAR"
        ]:
            text_color = (255, 255, 255)

        cv2.putText(
            frame,
            name,
            (x1 + 5, 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            text_color,
            1
        )

    # ======================
    # HAND TRACKING
    # ======================

    frame, x, y, is_drawing = tracker.detect(
        frame
    )

    # ======================
    # BUTTON SELECTION
    # ======================

    if x is not None and y is not None:

        if y < TOOLBAR_HEIGHT:

            section = x // button_width

            # SAVE
            if section == 0:

                drawing = canvas.get_canvas()

                final_image = cv2.addWeighted(
                    frame,
                    1,
                    drawing,
                    1,
                    0
                )

                filename = (
                    f"saved_drawings/drawing_{save_count}.png"
                )

                cv2.imwrite(
                    filename,
                    final_image
                )

                canvas_filename = (
                    f"saved_drawings/drawing_{save_count}_canvas.png"
                )

                cv2.imwrite(
                    canvas_filename,
                    drawing
                )

                print(
                    print(f"Solved: {expression}")
                )

                try:

                    expression = (
                        ocr.read_equation(
                            canvas_filename
                        )
                    )

                    print(
                        f"Detected: {expression}"
                    )

                    answer = (
                        evaluator.solve(
                            expression
                        )
                    )

                    print(
                        f"Answer: {answer}"
                    )

                except Exception as e:

                    print(e)

                    answer = "OCR Error"

                save_count += 1

            # CLEAR
            elif section == 1:

                canvas.clear()

                expression = ""
                answer = ""

            # ERASER
            elif section == 2:

                canvas.set_eraser()

            # WHITE
            elif section == 3:

                canvas.set_color(
                    (255, 255, 255)
                )

            # YELLOW
            elif section == 4:

                canvas.set_color(
                    (0, 255, 255)
                )

            # BLUE
            elif section == 5:

                canvas.set_color(
                    (255, 0, 0)
                )

            # GREEN
            elif section == 6:

                canvas.set_color(
                    (0, 255, 0)
                )

            # RED
            elif section == 7:

                canvas.set_color(
                    (0, 0, 255)
                )

            canvas.lift_pen()

    # ======================
    # DRAWING
    # ======================

    if (
        x is not None and
        is_drawing and
        y > TOOLBAR_HEIGHT
    ):

        canvas.draw(
            x,
            y
        )

    else:

        canvas.lift_pen()

    # ======================
    # MERGE CANVAS
    # ======================

    drawing = canvas.get_canvas()

    frame = cv2.addWeighted(
        frame,
        1,
        drawing,
        1,
        0
    )

    # ======================
    # INFO PANEL
    # ======================

    frame = display.show_info(
        frame,
        expression,
        answer
    )

    # ======================
    # WINDOW TITLE
    # ======================

    cv2.imshow(
        "Smart Air Canvas & Math Solver",
        frame
    )

    key = cv2.waitKey(1)

    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()