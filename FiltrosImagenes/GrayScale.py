from PIL import Image, ImageFilter

im0  = Image.open(r"D:\PyCharmProjects\FiltrosImagenes\ruido.jpg")
imG = im0.convert('LA')
imG.show()




