import pyzxing

# Initialize ZXing reader
reader = pyzxing.BarCodeReader()

# Absolute path to the image
image_path = r'/home/nathan/NatHan/STUDIES/year3/I Robotics/Term 2/QRCODE/CODES/data_matrix_code/image.png'

# Decode the image
barcode = reader.decode(image_path)
if barcode:
    print("Decoded Data:", barcode[0]['raw'])
else:
    print("No Data Matrix code found.")
