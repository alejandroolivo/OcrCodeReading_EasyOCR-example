# QR Code Detection, Cropping, and OCR with EasyOCR
This Python script detects a QR code in an image, crops the area around it, and extracts text from the cropped region using OCR (Optical Character Recognition).

## Dependencies
The script requires the following libraries:

OpenCV (cv2)
EasyOCR
NumPy
Matplotlib
You can install them with:

pip install opencv-python-headless easyocr numpy matplotlib

## Usage
Replace 'test.png' in the cv2.imread() function with the path to your input image containing a QR code.
Run the script to detect and crop the QR code, and then extract text from the cropped region.
The script will display the original image, the cropped region, and the detected text.

## Code Overview
The script starts by importing the required libraries.
The input image is loaded and converted to RGB format.
The original image is displayed using Matplotlib.
The QR code is detected using the OpenCV QRCodeDetector.
The QR code's bounding box coordinates are used to crop the image with additional padding.
EasyOCR is used to extract text from the cropped region.
The script sorts the OCR results based on the y-coordinate and displays the last result.
The cropped image is displayed with a bounding box around the last OCR result and the extracted text.

## Example
After running the script with the provided sample code, you should see:

The original image with the QR code.
The cropped region with the detected text and bounding box.