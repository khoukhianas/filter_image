import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

class ImageManipulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Manipulator")
        self.root.geometry("900x600")
        self.image = None

        self.image_label = tk.Label(root)
        self.image_label.pack()
        
        self.red_scale = tk.Scale(root, label="Red", from_=0, to=255, orient=tk.HORIZONTAL, command=self.update_image)
        self.red_scale.pack()

        self.green_scale = tk.Scale(root, label="Green", from_=0, to=255, orient=tk.HORIZONTAL, command=self.update_image)
        self.green_scale.pack()

        self.blue_scale = tk.Scale(root, label="Blue", from_=0, to=255, orient=tk.HORIZONTAL, command=self.update_image)
        self.blue_scale.pack()

        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.save_button = tk.Button(root, text="Save Image", command=self.save_image)
        self.save_button.pack()

        

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = cv2.imread(file_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
            self.image = Image.fromarray(image)

            # Calculate average values of red, green, and blue channels
            red_avg = int(image[:, :, 0].mean())
            green_avg = int(image[:, :, 1].mean())
            blue_avg = int(image[:, :, 2].mean())

            # Set default values for scrollbars
            self.red_scale.set(red_avg)
            self.green_scale.set(green_avg)
            self.blue_scale.set(blue_avg)

            self.update_image()

    def update_image(self, event=None):
        if self.image:
            red = self.red_scale.get()
            green = self.green_scale.get()
            blue = self.blue_scale.get()
            image_with_color = self.image.copy()
            image_with_color = Image.blend(image_with_color, Image.new('RGB', image_with_color.size, (red, green, blue)), alpha=0.5)
            photo = ImageTk.PhotoImage(image_with_color)
            self.image_label.config(image=photo)
            self.image_label.image = photo

    def save_image(self):
        if self.image:
            file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
            if file_path:
                image_with_color = self.image.copy()
                red = self.red_scale.get()
                green = self.green_scale.get()
                blue = self.blue_scale.get()
                image_with_color = Image.blend(image_with_color, Image.new('RGB', image_with_color.size, (red, green, blue)), alpha=0.5)
                image_with_color.save(file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageManipulatorApp(root)
    root.mainloop()
