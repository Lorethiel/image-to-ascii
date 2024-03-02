from PIL import Image
from tkinter import filedialog
import tkinter as tk
import os


def main():
    root = tk.Tk()
    root.withdraw() 

    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])  # opens windows file selection window

    if file_path:
        img = Image.open(file_path)
        filename, _ = os.path.splitext(os.path.basename(file_path))
        process(img,filename)
    else:
        print("No file selected.\n")


def process(img,filename):
    img_extension = img.format
    resized_img, width, height = downscale_img(img)  # returns resized image itself, width and height in this order.
    pixel = resized_img.load()
  

    file = open(f"{filename}.txt", "w")

    for y in range(height):                 
        for x in range(width):
            rgb_values = resized_img.getpixel((x, y))
            red = rgb_values[0]
            green = rgb_values[1]
            blue = rgb_values[2]

            br = 0.2126 * red + 0.7152 * green + 0.0722 * blue  # brightness calculating formula. "br" stands for brightness.

            if 0 <= br <= 51:
                file.write('@')
            elif 52 <= br <= 102:
                file.write('#')
            elif 103 <= br <= 153:      
                file.write('x')
            elif 153 <= br <= 204:
                file.write('-')
            elif 204 <= br <= 255:
                file.write(' ')

        file.write('\n')

    file.close()


def downscale_img(img, down_scale=3):
    height, width = img.size
    resized_img = img.resize((height // down_scale, width // down_scale))
    height, width = resized_img.size
    return resized_img, height, width


if __name__ == "__main__":
    main()
