import cv2
import numpy as np


class Canvas:

    def __init__(self):

        self.canvas = np.zeros(
            (480, 640, 3),
            dtype=np.uint8
        )

        self.prev_x = None
        self.prev_y = None

        self.color = (0, 0, 255)

        self.thickness = 3

    def set_color(self, color):

        self.color = color
        self.thickness = 3

    def set_eraser(self):

        self.color = (0, 0, 0)
        self.thickness = 20

    def draw(self, x, y):

        if self.prev_x is None:

            self.prev_x = x
            self.prev_y = y
            return

        cv2.line(
            self.canvas,
            (self.prev_x, self.prev_y),
            (x, y),
            self.color,
            self.thickness
        )

        self.prev_x = x
        self.prev_y = y

    def get_canvas(self):

        return self.canvas

    def lift_pen(self):

        self.prev_x = None
        self.prev_y = None

    def clear(self):

        self.canvas[:] = 0

        self.prev_x = None
        self.prev_y = None