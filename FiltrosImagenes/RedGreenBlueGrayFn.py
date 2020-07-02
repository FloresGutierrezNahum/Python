from PIL import Image

img0 = Image.open(r"D:\PyCharmProjects\FiltrosImagenes\ruido.jpg")

def getRGB(img, marca):

    #Canales RGB
    data = img.getdata()

    r = [(d[0], 0, 0) for d in data]
    g = [(0, d[1], 0) for d in data]
    b = [(0, 0, d[2]) for d in data]

    if marca == "red":
        img.putdata(r)
    elif marca == "green":
        img.putdata(g)
    elif marca == "blue":
        img.putdata(b)
    elif marca == "gray":
        img = img.convert('LA')
    return img


getRGB(img0, "red").convert('LA').show()