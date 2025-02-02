from pyzbar.pyzbar import decode
import cv2
import numpy as np

# Read the image
image_path = "image.png"
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Unable to load image from '{image_path}'")
else:
    # Decode the barcode
    barcodes = decode(image)
    if not barcodes:
        print("No barcode found in the image.")
    else:
        for barcode in barcodes:
            data = barcode.data.decode("utf-8")
            print(f"Barcode Data: {data}")

            # Draw a rectangle around the barcode
            points = barcode.polygon
            points = [(point.x, point.y) for point in points]
            cv2.polylines(image, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 2)

            # Annotate the decoded data beside the bounding box
            x, y = points[0]  # Take the first point of the bounding box
            cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)  # Green text

        # Save the annotated image
        output_file = "decoded_barcode.png"
        cv2.imwrite(output_file, image)
        print(f"Annotated image saved as '{output_file}'")

    # Close all OpenCV windows if any are open
    cv2.destroyAllWindows()
