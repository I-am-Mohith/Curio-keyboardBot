from tkinter import Image
import cv2
import time
import pyautogui
from PIL import Image
import pytesseract
import numpy as np
from pynput.keyboard import Controller

time.sleep(5)
keyboard = Controller()

pytesseract.tesseract_cmd = r"/usr/local/Cellar/tesseract/5.2.0/bin"

image = pyautogui.screenshot(region=(153, 349, 812, 96))
image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)

cv2.imwrite("image1.png", image)

path_to_image = 'image1.png'
img = Image.open(path_to_image)
text = pytesseract.image_to_string(img)

for i in text:
    keyboard.press(i)
    keyboard.release(i)
    time.sleep(0.05)
