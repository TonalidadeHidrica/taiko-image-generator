from math import pi
from pathlib import Path

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
    colors = Colors()

    output_dir = Path("output")

    # draw_background(colors, draw, output_dir / "game_bg.png")
    for is_don in (False, True):
        for is_large in (False, True):
            draw_note(colors,
                      output_dir / f"note_"
                                   f"{'don' if is_don else 'ka'}"
                                   f"{'_large' if is_large else ''}.png",
                      is_don, is_large)


def draw_background(colors: Colors, output_file: Path):
    with Drawing() as draw:
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
            image.save(filename=output_file)


def draw_note(colors: Colors, output_file: Path, is_don: bool, is_large: bool):
    with Drawing() as draw:
        draw.affine([1, 0, 0, 1, 97.5, 97.5])

        draw.stroke_width = 3
        draw.stroke_color = colors.black
        draw.fill_color = colors.get_color("#f7eedb")
        draw.circle((0, 0), (77 if is_large else 50, 0))

        draw.stroke_color = colors.none
        draw.fill_color = colors.get_color("#f84828" if is_don else "#68c0c0")
        draw.circle((0, 0), (60 if is_large else 39, 0))

        draw.stroke_color = colors.black
        draw.stroke_width = 2
        draw.fill_color = colors.none
        for i in (1, -1):
            origin = (i * 13, 15) if is_large else (i * 9.52, 10)
            radius = (12.75, 10.95) if is_large else (8.5, 7.3)
            delta = 0.3 * 180 / pi
            rotation = (delta, 180) if i == 1 else (0, 180 - delta)
            draw.ellipse(origin, radius, rotation)

        draw.stroke_width = 2.8
        draw.fill_color = colors.black
        for i in (1, -1):
            if is_large:
                degree = (-10, 230) if i == -1 else (-50, 190)
                draw.arc((i * 24, -16.5), (i * 46, 6), degree)
            else:
                draw.ellipse((i * 22, -4), (6.56, 7))

        if is_large:
            draw.stroke_width = 2
            draw.stroke_color = colors.black
            for i in (1, -1):
                draw.line((i * 20, -14), (i * 27, -27))

        with Image(width=195, height=195, pseudo="xc:transparent") as image:
            draw.draw(image)

            with image.clone() as shadow_layer:
                shadow_layer.background_color = colors.black
                shadow_layer.shadow(80, 2, 2, 2)

                shadow_layer.composite(image)
                shadow_layer.crop(width=195, height=195, left=0, top=0)
                shadow_layer.save(filename=output_file)


if __name__ == '__main__':
    main()
