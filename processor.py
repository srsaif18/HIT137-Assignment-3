import cv2
import numpy as np


class ImageProcessor:
    def __init__(self):
        self.original = None
        self.image = None

    def load_image(self, path):
        self.original = cv2.imread(path)
        self.image = self.original.copy()
        return self.image

    def reset(self):
        self.image = self.original.copy()
        return self.image

    def grayscale(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_GRAY2BGR)
        return self.image

    def blur(self, intensity):
        if self.original is None or intensity <= 0:
            self.image = self.original.copy()
            return self.image

        base = self.original.copy()
        ksize = intensity * 2 + 1  # always odd
        self.image = cv2.GaussianBlur(base, (ksize, ksize), 0)
        return self.image


    def edge_detection(self):
        edges = cv2.Canny(self.image, 100, 200)
        self.image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        return self.image

    def adjust_brightness(self, value):
        self.image = cv2.convertScaleAbs(self.image, alpha=1, beta=value)
        return self.image

    def adjust_contrast(self, value):
        self.image = cv2.convertScaleAbs(self.image, alpha=value, beta=0)
        return self.image

    def rotate(self, angle):
        if angle == 90:
            self.image = cv2.rotate(self.image, cv2.ROTATE_90_CLOCKWISE)
        elif angle == 180:
            self.image = cv2.rotate(self.image, cv2.ROTATE_180)
        elif angle == 270:
            self.image = cv2.rotate(self.image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        return self.image

    def flip(self, mode):
        self.image = cv2.flip(self.image, mode)
        return self.image

    def resize(self, scale):
        width = int(self.image.shape[1] * scale)
        height = int(self.image.shape[0] * scale)
        self.image = cv2.resize(self.image, (width, height))
        return self.image
