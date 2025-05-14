from PIL import Image
im = Image.open("abcd.jpg")
im.show()
print(im.format, im.size, im.mode)
