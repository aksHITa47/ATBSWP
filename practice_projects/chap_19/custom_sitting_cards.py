import os
from PIL import Image,ImageDraw
from PIL import ImageFont
file=open('guests.txt')
os.makedirs('CustomCards', exist_ok=True)
flowerImg = Image.open('flower.png')  # open template 
for Name in file.readlines():
    card = Image.new('RGBA', (288, 360), 'white') # create image
    flowerImg = flowerImg.resize((360,288))
    card.paste(flowerImg, (0, 0)) # paste the flower template
    border = Image.new('RGBA', (291, 363), 'black') 
    border.paste(card, (3,3))
    draw_obj = ImageDraw.Draw(border)
    card_font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 24)
    draw_obj.text((120, 100), Name, fill='darkviolet', font=card_font)
    imageName = '{}_card.png'.format(Name)
    border.save(os.path.join('CustomCards', imageName))


    