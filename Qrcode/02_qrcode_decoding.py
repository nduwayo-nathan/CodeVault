import cv2
import numpy as np

# Initialize QR code detector
detector = cv2.QRCodeDetector()

# Read the image
image_path = "image.png"
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Unable to load image from '{image_path}'")
else:
    # Detect and decode the QR code
    data, points, _ = detector.detectAndDecode(image)

    if data:
        print(f"QR Code Data: {data}")
        # Draw a polygon around the detected QR code
        if points is not None:
            points = points[0].astype(int)  # Flatten the points array
            cv2.polylines(image, [points], True, (0, 255, 0), 2)

            # Annotate the decoded data near the QR code
            x, y = points[0]  # First point for positioning the text
            cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Save the annotated image
        output_file = "decoded_qrcode.png"
        cv2.imwrite(output_file, image)
        print(f"Annotated image saved as '{output_file}'")
    else:
        print("No QR code detected.")
