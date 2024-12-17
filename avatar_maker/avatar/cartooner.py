import cv2
import numpy as np

class Cartoonizer:
    def render(self, img_path):
        """
        Converts a given image into a cartoon-style image.
        """
        # Step 1: Read the image
        img = cv2.imread(img_path)
        img = cv2.resize(img, (600, 600))  # Resize for consistency

        # Step 2: Edge detection for creating a cartoon effect
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        gray_blur = cv2.medianBlur(gray, 7)          # Reduce noise
        edges = cv2.adaptiveThreshold(
            gray_blur, 255,
            cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY, 9, 10
        )

        # Step 3: Smoothen colors using bilateral filtering
        color = cv2.bilateralFilter(img, 9, 300, 300)

        # Step 4: Combine edges with the smoothened image
        edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)  # Convert edges to 3-channel
        cartoon = cv2.bitwise_and(color, edges)

        return cartoon

# Example Usage
# cartoonizer = Cartoonizer()
# output = cartoonizer.render('input_image.jpg')

# cv2.imshow("Cartoon Effect", output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
