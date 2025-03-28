from PIL import Image, ImageEnhance, ImageOps
import numpy as np
import random

def image_multiplier(img, n):
    variants = []
    
    for _ in range(n):
        tmp = img.copy()
        
        # random rotation
        angle = random.choice([90, 180, 270])
        tmp = tmp.rotate(angle, expand = True)
        
        # random brightness, contrast, and color
        brightness = random.uniform(0.3, 2)
        contrast = random.uniform(0.3, 2)
        color = random.uniform(0.3, 2)
        tmp = ImageEnhance.Brightness(tmp).enhance(brightness)
        tmp = ImageEnhance.Contrast(tmp).enhance(contrast)
        tmp = ImageEnhance.Color(tmp).enhance(color)
        
        # random orientation
        c = random.choice(['none', 'mirror', 'flip', 'mirror_flip'])
        if c == 'mirror':
            tmp = ImageOps.mirror(tmp)
        elif c == 'flip':
            tmp = ImageOps.flip(tmp)
        elif c == 'mirror_flip':
            tmp = ImageOps.mirror(tmp)
            tmp = ImageOps.flip(tmp)
            
        # random shear 
        #shear = random.uniform(-0.5, 0.5)
        #tmp = tmp.transform(tmp.size, Image.AFFINE, (1, shear, 0, 0, 1, 0))
        #variants.append(tmp)

        # random zoom
        scale = random.uniform(0.3, 2)
        tmpsize = (int(tmp.width * scale), int(tmp.height * scale))
        tmp = tmp.resize(tmpsize, Image.BICUBIC)

        variants.append(tmp)

    return variants

from IPython.display import display

img = Image.open('ISIC_9996602.jpg')
test = image_multiplier(img, 5)
display(img) # original image
for i in range(5):
    display(test[i])
