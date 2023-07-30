import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from io import BytesIO

def create_pencil_sketch(input_image):
    gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    return pencil_sketch

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        image = cv2.imread(file_path)
        pencil_sketch = create_pencil_sketch(image)
        show_pencil_sketch(pencil_sketch)

def show_pencil_sketch(pencil_sketch):
    sketch_img = Image.fromarray(pencil_sketch)
    sketch_photo = ImageTk.PhotoImage(image=sketch_img)
    result_label.config(image=sketch_photo)
    result_label.image = sketch_photo

root = tk.Tk()
root.title("Pencil Sketch Generator")

file_button = tk.Button(root, text="Select Image", command=select_image)
file_button.pack(pady=10)

result_label = tk.Label(root)
result_label.pack()

root.mainloop()
