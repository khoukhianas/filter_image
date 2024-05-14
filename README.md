##ImageManipulator

ImageManipulator is a simple image manipulation tool built using Python and tkinter. It allows you to load an image, apply a color filter, and 
save the modified image.

##Features
Load an image from your file system.

Adjust the red, green, and blue color channels using sliders.

Apply a color filter to the image based on the selected RGB values.

Preview the modified image in real-time.

Save the modified image to your file system.

##Prerequisites

Python 3.x installed on your system.

Required Python packages: opencv-python, Pillow (PIL), tkinter (usually included with Python).

###Installation

Clone the repository:

bash

Copy code

git clone https://github.com/khoukhianas/ImageManipulator.git

Navigate to the project directory:

bash

Copy code

cd ImageManipulator

#Install the required Python packages:

bash

Copy code

pip install opencv-python Pillow

Usage

Run the application:

bash

Copy code

python image_manipulator.py

#Use the following controls:

@Load Image: Click to select an image file from your system.

@Red Slider: Adjust the red color channel (-255 to 255).

@Green Slider: Adjust the green color channel (-255 to 255).

@Blue Slider: Adjust the blue color channel (-255 to 255).

@Save Image: Save the modified image with the applied color filter.
