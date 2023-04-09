import cv2
import easyocr
import numpy as np
import matplotlib.pyplot as plt

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


# load reader
reader = easyocr.Reader(['en'])

# read text
result = reader.readtext(crop_img)

# show result
print(result)

#sort results by y coordinate
result.sort(key=lambda x: x[0][1])

# show last result
print(result[-1])

fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(crop_img)

top_left = tuple([int(val) for val in result[-1][0][0]])
bottom_right = tuple([int(val) for val in result[-1][0][2]])
data = result[-1][1] 
# ax.add_patch(plt.Rectangle(top_left, bottom_right[0] - top_left[0], bottom_right[1] - top_left[1], fill=False, edgecolor='red', linewidth=2))

#delete chars that are not numbers in "data"
data = data.replace(" ", "")
data = data.replace("/", "")

# add text filtered for only numbers
ax.text(top_left[0]+50, top_left[1] - 2 + 50, data, bbox=dict(facecolor='red', alpha=0.5), fontsize=14, color='white')

plt.show()
