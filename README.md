# QR Code Detection, Cropping, and OCR with EasyOCR and PaddleOCR
These Python scripts detect a QR code in an image, crop the area around it, and extract text from the cropped region using OCR (Optical Character Recognition). There are two versions available: one using EasyOCR and another using PaddleOCR.

## Dependencies
The scripts require the following libraries:

    -OpenCV (cv2)
    -EasyOCR (for the EasyOCR script)
    -PaddlePaddleOCR (for the PaddleOCR script)
    -NumPy
    -Matplotlib
    -PIL (Pillow)
You can install them with:

pip install opencv-python-headless easyocr numpy matplotlib paddleocr pillow
## Usage
Choose the script you want to use (EasyOCR or PaddleOCR version).
Replace 'test.png' in the cv2.imread() function with the path to your input image containing a QR code.
Run the script to detect and crop the QR code, and then extract text from the cropped region.
The script will display the original image, the cropped region, and the detected text.
## Code Overview
Both scripts follow a similar structure:

    -Import the required libraries.
    -Load the input image and convert it to RGB format.
    -Display the original image using Matplotlib.
    -Detect the QR code using the OpenCV QRCodeDetector.
    -Use the QR code's bounding box coordinates to crop the image with additional padding.
    -Use either EasyOCR or PaddleOCR to extract text from the cropped region.
    -Display the extracted text and the cropped image with the detected text.

## Examples
After running either script with the provided sample code, you should see:
    -The original image with the QR code.
    -The cropped region with the detected text.    
## License
This project is licensed under the Apache License 2.0. For more information, please refer to the [LICENSE](LICENSE) file in the root of this repository.
Apache License 2.0
Copyright (c) 2023 Alejandro Olivo
