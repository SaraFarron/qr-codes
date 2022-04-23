import qrcode


with open('index.html', 'r') as f:
    text = f.read()
data = """

"""

img = qrcode.make(text)
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")
