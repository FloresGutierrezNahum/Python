# Importing Image and ImageFilter module from PIL package
# Pip install pillow
import cv2
from PIL import Image, ImageFilter

im = Image.open(r"D:\PyCharmProjects\FiltrosImagenes\lena.png")

def GaussianBlurFn(im, radio):
    im1 = im.filter(ImageFilter.GaussianBlur(radius=radio))
    #im1.show()

    return im1

GaussianBlurFn(im,1).show()