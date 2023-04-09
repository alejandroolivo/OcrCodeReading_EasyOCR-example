from PaddlePaddleOCR import PaddleOCR, draw_ocr
import numpy as np
import matplotlib.pyplot as plt
import cv2

# load image
img = cv2.imread('test.png')

# convert image to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# show image
plt.imshow(img)
plt.show()

# find qrcode
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img)

# Get the minimum and maximum x and y coordinates
min_x, min_y = np.min(bbox[:, 0]), np.min(bbox[:, 1])
max_x, max_y = np.max(bbox[:, 0]), np.max(bbox[:, 1])

# Define the padding around the QR code
padding = 200

# Crop the image using the coordinates and padding
crop_img = img[int(min_y): int(max_y + padding), int(min_x): int(max_x + padding)]

# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`to switch the language model in order.
ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory
img_path = './test.png'
result = ocr.ocr(img_path, cls=True)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)


# draw result
from PIL import Image
result = result[0]
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')

# read text from image using PaddlePaddleOCR
result = ocr.ocr(crop_img, cls=True)

# show result
print(result)

# show image
plt.imshow(crop_img)
plt.show()

