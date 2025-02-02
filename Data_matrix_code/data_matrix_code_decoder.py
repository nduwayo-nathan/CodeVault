from pylibdmtx.pylibdmtx import decode
from PIL import Image
import os

# Path to the Data Matrix image
image_path = "/home/nathan/NatHan/STUDIES/year3/I Robotics/Term 2/QRCODE/CODES/Data_matrix_code/image.png"

# Check if the image exists at the specified path
if not os.path.exists(image_path):
    print(f"Error: Image not found at {image_path}")
    exit(1)

# Load the ECC 200 Data Matrix image
image = Image.open(image_path)

# Decode the ECC 200 Data Matrix
decoded = decode(image)

if decoded:
    print("Decoded Data:", decoded[0].data.decode('utf-8'))
else:
    print("No Data Matrix found.")
