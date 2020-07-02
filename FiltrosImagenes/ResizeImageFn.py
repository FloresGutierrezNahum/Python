from PIL import Image

im = Image.open(r"D:\PyCharmProjects\FiltrosImagenes\ruido.jpg")

def ResizeImgFn(im, porcentaje):
    width, height = im.size

    newWidth = int(width * porcentaje)
    newHeight = int(height * porcentaje)

    newsize = (newWidth, newHeight)

    #print(width, height)
    #print(newWidth, newHeight)

    im = im.resize(newsize)

    return im

ResizeImgFn(im,1).show()