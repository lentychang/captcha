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
    
    # generating names of each test set
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

def setup_training_set_single_char(no_training_set_per_char=2000):
    image = ImageCaptcha(width=23,height=50,
                        fonts=['/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'],
                        font_sizes=(30,35,38))
    
    # generating names of each test set
    char_cases = [0,1,2,3,4,5,6,7,8,9]
    for char in char_cases:
        for i in range(no_training_set_per_char):
            # assign background color        
            bg_color = (random.randint(200,250),random.randint(175,255),random.randint(175,255))
            # assign char color
            char_color = (random.randint(220,255),0,0)
            im = image.create_captcha_image(chars=f"{char:0>1d}",color=char_color,background=bg_color,enable_warping=False,enable_rotate=False)
            line_color_r = random.randint(100,255)
            line_color_g = random.randint(0,line_color_r//2)
            line_color_b = random.randint(0,line_color_r//2)
            line_color = (line_color_r,line_color_g,line_color_b)
            im = image.create_noise_line(im, color=line_color,len_based_on_width=False,len_ratios=(0.05,0.35),n_lines=random.randint(4,20))

            # im = im.filter(ImageFilter.SMOOTH)
            im.save(f"imgs/{char:0>1d}_{i}.png",format="png")


if __name__ =="__main__":
    # setup_training_set(no_training_set=1)
    setup_training_set_single_char(no_training_set_per_char=1)

