from PIL import Image, ImageFilter


# creating a image object
im0 = Image.open(r"D:\PyCharmProjects\FiltrosImagenes\lena.png")

# applying the Gaussian Blur filter
im1 = im0.filter(ImageFilter.MedianFilter(size=3))

im0.show()
im1.show()
