from PIL import Image

# Opens a image in RGB mode
im = Image.open(r"D:\PyCharmProjects\FiltrosImagenes\ruido.jpg")
width, height = im.size

newWidth = int(width*0.1)
newHeight = int(height*0.1)

newsize = (newWidth, newHeight)
im = im.resize(newsize)

im.show()