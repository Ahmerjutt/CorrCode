from PIL import Image
import sys


x = sys.argv[1]
y = sys.argv[2]

print(x)

im = Image.open("img.jpeg")
print(f"The image size dimensions are: {im.size}")

file_name = 'compressed.jpeg'
picture = Image.open('img.jpeg')
dim = picture.size
print(f"This is the current width and height of the image: {dim}")
picture.save(file_name,optimize=True,quality=35)