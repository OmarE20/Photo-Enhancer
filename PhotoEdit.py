from PIL import Image, ImageEnhance, ImageFilter
import os

path = 'C:\Users\omare\OneDrive\Desktop\Old Images'
pathOut = 'C:\Users\omare\OneDrive\Desktop\New Images'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN)

    cleanName = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{cleanName}_edited.jpg')
