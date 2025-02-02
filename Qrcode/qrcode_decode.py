from pyzbar.pyzbar import decode
from PIL import Image
import os

# Path to the QR Code image
image_path = "/home/nathan/NatHan/STUDIES/year3/I Robotics/Term 2/QRCODE/CODES/Qrcode/image.png"

# Check if the image exists
if not os.path.exists(image_path):
    print(f"Error: Image not found at {image_path}")
    exit(1)

# Load the QR Code image
qr_image = Image.open(image_path)

# Decode the QR Code
decoded_data = decode(qr_image)

# Check if any QR codes were found
if decoded_data:
    for obj in decoded_data:
        raw_data = obj.data
        print(f"Raw Data: {raw_data}")  # Print raw byte data
        try:
            # Decode as UTF-8 (Korean characters are supported)
            decoded_text = raw_data.decode("utf-8")
            print(f"Decoded Data (UTF-8): {decoded_text}")
        except UnicodeDecodeError as e:
            print(f"UTF-8 Decode Error: {e}")
else:
    print("No QR codes found in the image.")
