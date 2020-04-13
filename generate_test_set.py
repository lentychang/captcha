from captcha_solver import CaptchaSolver
import cv2
import numpy as np
from modules.captcha.captcha.image import ImageCaptcha
from PIL import ImageFilter
import random

def setup_training_set(no_training_set=2000):
    image = ImageCaptcha(width=140,height=50,
                        fonts=['/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'],
                        font_sizes=(28,30,32))
    

    test_cases = np.rint(np.random.rand(no_training_set)*1000000).astype(int)
    print(test_cases)

    for name in test_cases:
        
        bcolor = (random.randint(200,250),random.randint(175,255),random.randint(175,255))
        randRed = random.randint(220,255)
        im = image.create_captcha_image(chars=f"{name:0>6d}",color=(randRed,0,0),background=bcolor,enable_warping=False,enable_rotate=False)
        color = (random.randint(randRed,255),random.randint(0,100),random.randint(0,100))
        im = image.create_noise_line(im, color=color,len_based_on_width=False,len_ratios=(0.1,0.35),n_lines=10)

        # im = im.filter(ImageFilter.SMOOTH)
        im.save("imgs/"+f"{name:0>6d}"+".png",format="png")

setup_training_set(no_training_set=1)

