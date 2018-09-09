import sys
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from random import *

tvp_list = ["pusty_pasek.png"]


def main():
    font = ImageFont.truetype("font.ttf", 35)

    imie = input("Tekst: ")
    podpis = input("Podpis: ")

    imageFile = choice(tvp_list)
    im1 = Image.open(imageFile)

    W1, H1 = (250, 1500)

    draw = ImageDraw.Draw(im1)
    w1, h1 = draw.textsize(imie, font)
    w2, h2 = draw.textsize(podpis, font)
    draw.text((250+(1250-w1)/2, 103), imie, (0, 0, 0), font=font)
    draw.text((250+(1250-w2)/2, 153), podpis, (255, 255, 255), font=font)
    draw = ImageDraw.Draw(im1)

    im1.save("pasek.png")


if __name__ == '__main__':
    main()
