import cv2
from pyzxing import BarCodeReader

# Path to the input image
image_path = '/home/nathan/NatHan/STUDIES/year3/I Robotics/Term 2/QRCODE/CODES/Aztec_Code/image.png'

# Read the image
image = cv2.imread(image_path)

# Check if the image is loaded correctly
if image is None:
    print(f"Error: Unable to load the image '{image_path}'.")
    exit(1)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to make the barcode stand out (optional)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Decode with pyzxing without saving the processed image
reader = BarCodeReader()
results = reader.decode(thresh)

# Check if results were found and display the raw data
if results:
    decoded_data = results[0].get('raw', 'No raw data found')
    print(f"Decoded Data: {decoded_data}")
else:
    print("No Aztec code detected in the image.")
