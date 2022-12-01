from time import sleep

import netifaces as ni
from pitop import Pitop
from PIL import Image, ImageDraw, ImageFont


y = 0
pitop = Pitop()

m = pitop.miniscreen
image = Image.new(m.mode,m.size)
canvas = ImageDraw.Draw(image)
m.set_max_fps(2)
x = m.cancel_button

ip = ni.ifaddresses('eth0')[ni.AF_INET6][0]['addr']
half = ip[:len(ip)//2]
half2 = ip[len(ip)//2:]

canvas.text((0,0),half,font=ImageFont.load_default(),fill=1)
canvas.text((0,12),half2,font=ImageFont.load_default(),fill=1)
m.display_image(image)

print(half)
print(half2)

while not x.is_pressed:
    y
