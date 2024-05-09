import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

class ImageManipulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ImageManipulator")
        self.root.geometry("900x600")
        self.image = None
        self.root.configure(bg="lightgrey")
        self.image_label = tk.Label(root, bg="white")
        self.image_label.pack()
        self.red_scale = tk.Scale(root, label="Red", from_=-255, to=255, orient=tk.HORIZONTAL, command=self.update_image, bg="lightgrey")
        self.red_scale.set(0)
        self.red_scale.pack()
        self.green_scale = tk.Scale(root, label="Green", from_=-255, to=255, orient=tk.HORIZONTAL, command=self.update_image, bg="lightgrey")
        self.green_scale.set(0)
        self.green_scale.pack()
        self.blue_scale = tk.Scale(root, label="Blue", from_=-255, to=255, orient=tk.HORIZONTAL, command=self.update_image, bg="lightgrey")
        self.blue_scale.set(0)
        self.blue_scale.pack()
        self.load_button = tk.Button(root, text="Load Image", command=self.load_image, bg="lightblue")
        self.load_button.pack()
        self.save_button = tk.Button(root, text="Save Image", command=self.save_image, bg="lightgreen")
        self.save_button.pack()
    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = cv2.imread(file_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            self.image = Image.fromarray(image)
            self.update_image()
    def update_image(self, event=None):
        if self.image:
            red = self.red_scale.get()
            green = self.green_scale.get()
            blue = self.blue_scale.get()
            alpha = (abs(red) + abs(green) + abs(blue)) / (3 * 255)
            if red == 0 and green == 0 and blue == 0:
                filtered_image = Image.new('RGB', self.image.size, (0, 0, 0))
            else:
                filtered_image = Image.new('RGB', self.image.size, (int(red), int(green), int(blue)))
            blended_image = Image.blend(self.image, filtered_image, alpha)
            photo = ImageTk.PhotoImage(blended_image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
    def save_image(self):
        if self.image:
            file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
            if file_path:
                red = self.red_scale.get()
                green = self.green_scale.get()
                blue = self.blue_scale.get()
                alpha = (abs(red) + abs(green) + abs(blue)) / (3 * 255)
                if red == 0 and green == 0 and blue == 0:
                    filtered_image = Image.new('RGB', self.image.size, (0, 0, 0))
                else:
                    filtered_image = Image.new('RGB', self.image.size, (int(red), int(green), int(blue)))
                blended_image = Image.blend(self.image, filtered_image, alpha)
                blended_image.save(file_path)
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageManipulatorApp(root)
    root.mainloop()
