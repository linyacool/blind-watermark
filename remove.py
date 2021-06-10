import sys
from PIL import Image, ImageFilter

r, g, b = Image.open(sys.argv[1]).convert("RGB").split()
b = b.filter(ImageFilter.MedianFilter())
Image.merge("RGB", (r, g, b)).save("cleaned.png")
