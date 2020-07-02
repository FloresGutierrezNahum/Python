from PIL import Image

img = Image.open(r"D:\PyCharmProjects\FiltrosImagenes\image460prime.tif")
data = img.getdata()

# Suppress specific bands (e.g. (255, 120, 65) -> (0, 120, 0) for g)
r = [(d[0], 0, 0) for d in data]
g = [(0, d[1], 0) for d in data]
b = [(0, 0, d[2]) for d in data]

img.show()

img.putdata(r)
img.show()

img.putdata(g)
img.show()

img.putdata(b)
img.show()