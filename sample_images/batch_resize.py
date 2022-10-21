import cv2
import os

for file in os.listdir():
    if ('jpg' not in file):
        continue

    img = cv2.imread(file, 0)
    resized_image = cv2.resize(img, (100, 100))
    cv2.imwrite(f'resized_{file}', resized_image)
