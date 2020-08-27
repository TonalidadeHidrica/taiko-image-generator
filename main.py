from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image


class Colors:
    def __init__(self):
        self.name_to_colors = {}
        self.none = self.get_color("none")
        self.black = self.get_color("black")

    def get_color(self, name: str) -> Color:
        ret = self.name_to_colors.get(name)
        if ret is None:
            self.name_to_colors[name] = (ret := Color(name).__enter__())
        return ret


def main():
    draw = Drawing().__enter__()
    colors = Colors()

    draw.stroke_color = colors.none
    draw.fill_color = colors.black
    draw.rectangle(0, 276, 1920, 539)

    draw.fill_color = colors.get_color("#b30000")
    draw.rectangle(0, 288, 491, 527)  # 492, 528

    draw.fill_color = colors.get_color("#282828")
    draw.rectangle(498, 288, 1920, 482)  # 483

    draw.fill_color = colors.get_color("#848484")
    draw.rectangle(498, 489, 1920, 527)  # 528

    draw.stroke_width = 4
    draw.stroke_color = colors.get_color("#646464")
    draw.fill_color = colors.none
    draw.circle((617.5, 385.5), (617.5, 462.5))

    draw.stroke_width = 4
    draw.stroke_color = colors.get_color("#8C8C8C")
    draw.fill_color = colors.none
    draw.circle((617.5, 385.5), (617.5, 435.5))

    draw.stroke_color = colors.none
    draw.fill_color = colors.get_color("#525252")
    draw.circle((617.5, 385.5), (617.5, 424.5))

    with Image(width=1920, height=1080, pseudo="xc:transparent") as image:
        draw.draw(image)
        image.save(filename="output/game_bg.png")


if __name__ == '__main__':
    main()
