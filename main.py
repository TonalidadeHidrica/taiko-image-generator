from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image


def main():
    with Drawing() as draw:
        draw.stroke_color = Color("none")
        draw.fill_color = Color("black")
        draw.rectangle(0, 276, 1920, 539)

        with Image(width=1920, height=1080, pseudo="xc:transparent")as image:
            draw.draw(image)
            image.save(filename="output/test.png")


if __name__ == '__main__':
    main()
