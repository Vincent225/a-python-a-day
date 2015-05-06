#!/usr/bin/python
#encoding=utf-8

import os
from PIL import Image

# iphone5 1136x640
IPHONE_W = 1136
IPHONE_H = 640

def get_resized_file_name(file_name):
    return "%s_thumb.jpg" % file_name[:-4]

def resize_image(file_name):
    img = Image.open(file_name)
    w, h = img.size
    img_resize = None

    if w > IPHONE_W:
        new_h = int(max((h * IPHONE_W / w), 1))
        print  (IPHONE_w, new_h)
        img_resize = img.resize((IPHONE_W, new_h))
    elif h > IPHONE_H:
        new_w = int(max((w * IPHONE_H / h), 1))
        print  (IPHONE_H, new_w)
        img_resize = img.resize((IPHONE_H, new_w))
    
    if img_resize:
        file_resized_name = get_resized_file_name(file_name)
        print 'resize file %s' % file_resized_name
        img_resize.save(file_resized_name, "JPEG")

def walk_dir(image_path):
    for dirpath, dirnames, files in os.walk(image_path):
        for f in files: 
            if f.lower().endswith('jpg') and not f.lower().endswith('_thumb.jpg'):
                full_path = os.path.join(dirpath, f)
                resize_image(full_path)

if __name__ == '__main__':
    walk_dir("images")
