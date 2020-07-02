from PIL import Image, ImageFilter

im = Image.open(r"D:\PyCharmProjects\FiltrosImagenes\lena.png")

def MedianFilterFn(im, size):
    im1 = im.filter(ImageFilter.MedianFilter(size=size))
    #im1.show()

    return im1

MedianFilterFn(im,9).show()