#!/usr/bin/env python3
from PIL import Image

def fill_image(image):
  width,height = image.size
  new_length = 0
  if width > height:  
    new_length = width 
  else:
    new_length = height
  imageNew = Image.new(image.mode,(new_length,new_length),color='white')
#  if width > height:
   #imageNew.paste(image,(0,int((new_length-height)/2)))
#  else:
   #imageNew.paste(image,(int((new_length-width)/2,0))
  imageNew.paste(image,(0,int((new_length-height)/2)))
  return imageNew

def cut_image(image):
  width, height = image.size
  item_width = int(width/3)
  box_list = []
  image_list = []
  for i in range(0,3):
    for j in range(0,3):
      box = (j*item_width, i*item_width,(j+1)*item_width, (i+1)*item_width)
      box_list.append(box) 
  for box in box_list:
    image_list.append(image.crop(box))
  return image_list

def save_images(image_list):
  index=1
  for image in image_list:
    image.save('./result/python'+str(index)+'.png','PNG')
    index += 1

if __name__=='__main__':
  file_path='python.JPG'
  image=Image.open(file_path)
  new_image=fill_image(image)
  image_list=cut_image(new_image)
  save_images(image_list)
