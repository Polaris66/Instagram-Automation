import os
from os import system
import random
import cv2
import requests

def get_caption():
    lines = open('captions.text').read().splitlines()
    caption = random.choice(lines)
    words = caption.split()
    caption = words[0]
    return caption

def get_image(file_name):
    img = cv2.imread(os.path.join('photos',file_name))
    return img

def add_text(img, text):
    FONT_SCALE = 4e-3
    width = img.shape[0]
    height = img.shape[1]
    fontScale = min(width, height)* FONT_SCALE
    cv2.putText(img, text, (0,int(height/2)),cv2.FONT_HERSHEY_TRIPLEX,fontScale,  (255, 0, 0))
    return img
    

def get_random_name():
    return random.choice(os.listdir('photos'))

def make_image():
    caption = get_caption()
    file_name = get_random_name()
    img = get_image(file_name)
    img = add_text(img, caption)
    
    height, width, _ = img.shape

    desired_width = int(height*9/16)
    desired_height = int(width*16/9)
    if width > desired_width:
        padding_height = max(0, desired_height - height)
        padding_top = padding_height // 2
        padding_bottom = padding_height - padding_top
        img = cv2.copyMakeBorder(img, padding_top, padding_bottom, 0,0, cv2.BORDER_CONSTANT, value=(0,0,0))
    else:
        padding_width = max(0, desired_width - width)
        padding_left = padding_width // 2
        padding_right = padding_width - padding_left
        img = cv2.copyMakeBorder(img, 0, 0, padding_left, padding_right, cv2.BORDER_CONSTANT, value=(0,0,0))

    file_output = f'result/{caption}.png'
    cv2.imwrite(file_output, img)
    return file_output

def upload_image():
    file_name = make_image()
    image_key = os.environ['IMAGE_KEY']
    expiration = '86400'
    url = 'https://api.imgbb.com/1/upload'
    params = {
        'expiration' : {expiration},
        'key' : {image_key}
    }
    data = {
        'image': open(file_name, 'rb')
    }

    try:
        res = requests.post(
          url,
          params=params,
          files=data
        ).json()
        url = res['data']['url']
        os.remove(file_name)
        return url
    except requests.exceptions.HTTPError as e:
        pass
