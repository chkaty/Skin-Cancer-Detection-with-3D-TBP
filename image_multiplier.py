from PIL import Image, ImageEnhance, ImageOps
import numpy as np
import random

def image_multiplier(img, n):
    variants = []
    for i in range(n):
        tmp = img.copy()
        
        # random rotation
        angle = random.uniform(-30, 30)
        tmp = tmp.rotate(angle, expand = True)
        
        # random brightness, contrast, and color
        brightness = random.uniform(0.5, 1.5)
        contrast = random.uniform(0.5, 1.5)
        color = random.uniform(0.5, 1.5)
        tmp = ImageEnhance.Brightness(tmp).enhance(brightness)
        tmp = ImageEnhance.Contrast(tmp).enhance(contrast)
        tmp = ImageEnhance.Color(tmp).enhance(color)
        
        # random flip
        if random.random() < 0.5:
            tmp = ImageOps.mirror(tmp)
            
        # random shear
        shear = random.uniform(-0.5, 0.5)
        tmp = tmp.transform(tmp.size, Image.AFFINE, (1, shear, 0, 0, 1, 0))
        variants.append(tmp)

    return variants

from IPython.display import display

img = Image.open('ISIC_9996602.jpg')
test = image_multiplier(img, 5)
for i in range(5):
    display(test[i])