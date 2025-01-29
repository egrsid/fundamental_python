import cv2
from pyzbar.pyzbar import decode


def read_qr_code(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: Unable to open image '{image_path}'.")
        return None

    # Decode the QR code
    decoded_objects = decode(image)

    if not decoded_objects:
        print("No QR code found in the image.")
        return None

    # Extract the data from the first decoded object
    qr_data = decoded_objects[0].data.decode('utf-8')

    return qr_data


if __name__ == "__main__":
    image_path = fr'C:\projects\Python\fundamental_python\DATA_BASES\qr_codes\Apple.png'  # Replace with your image path
    result = read_qr_code(image_path)

    if result:
        print(f"QR Code data: {result}")