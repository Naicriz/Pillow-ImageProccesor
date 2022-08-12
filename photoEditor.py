# PIL is the Python Imaging Library
from importlib.resources import path
from PIL import Image, ImageEnhance, ImageFilter
# For File Management
import os

path = './src/images/'
pathOut =  './src/editedImages/'

for filename in os.listdir(path):
    """
    Here is the explanation for his function:
    1. The loop starts by importing the Image and ImageEnhance modules.
    2. The loop then goes through all the files in the directory and opens them.
    3. The loop then filters the image and rotates it to make it upright.
    4. The loop then enhances the image and increases the brightness.
    5. The loop then saves the image.
    """
    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN)#.rotate(-90) # this is the filter that is being used and the rotation is used to make the image upright
    
    factor = 1.5 # this is the factor that is being used to increase the brightness of the image
    enhancer = ImageEnhance.Contrast(edit) # can be contrasted, brightness, or sharpness
    edit = enhancer.enhance(factor) # this is the image that is being enhanced

    clean_name = os.path.splitext(filename)[0] # this is the name of the image without the extension which is .jpg and is split into an array
    
    edit.save(f"{pathOut}/{clean_name}_edited.jpg") # this is the name of the image that is being saved with the edited name