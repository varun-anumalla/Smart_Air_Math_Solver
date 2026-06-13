import cv2

from modules.hand_tracker import HandTracker
from modules.canvas import Canvas

cap = cv2.VideoCapture(0)

tracker = HandTracker()
canvas = Canvas()

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    frame, x, y, is_drawing = tracker.detect(frame)

    if x is not None and is_drawing:
        canvas.draw(x, y)
    else:
        canvas.lift_pen()

    drawing = canvas.get_canvas()

    frame = cv2.add(frame, drawing)

    cv2.imshow(
        "Smart Air Math Solver",
        frame
    )

    key = cv2.waitKey(1)

    if key & 0xFF == ord('q'):
        break

    if key & 0xFF == ord('c'):
        canvas.clear()

cap.release()
cv2.destroyAllWindows()