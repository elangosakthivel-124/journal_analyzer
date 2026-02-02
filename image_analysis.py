from PIL import Image
import numpy as np
import cv2

class ImageAnalyzer:
    def analyze(self, image_path: str) -> dict:
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Invalid image path")

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        brightness = round(float(np.mean(gray)), 2)

        (B, G, R) = cv2.split(image.astype("float"))
        rg = np.absolute(R - G)
        yb = np.absolute(0.5 * (R + G) - B)

        colorfulness = round(
            np.sqrt(np.mean(rg) ** 2 + np.mean(yb) ** 2), 2
        )

        return {
            "brightness": brightness,
            "colorfulness": colorfulness
        }
