# Importing Image and ImageFilter module from PIL package
# Pip install pillow
import cv2
from PIL import Image, ImageFilter


# creating a image object  
im0 = Image.open(r"D:\PyCharmProjects\FiltrosImagenes\lena.png")

# applying the Gaussian Blur filter  
im1 = im0.filter(ImageFilter.GaussianBlur(radius=1))
im2 = im0.filter(ImageFilter.GaussianBlur(radius=2))
im3 = im0.filter(ImageFilter.GaussianBlur(radius=3))
im4 = im0.filter(ImageFilter.GaussianBlur(radius=4))
im5 = im0.filter(ImageFilter.GaussianBlur(radius=5))

im0.show()
im1.show()
im2.show()
im3.show()
im4.show()
im5.show()


