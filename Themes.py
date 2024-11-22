from enum import Enum
from kivy.utils import get_color_from_hex

class Themes(Enum):
    LIGHT = 1
    DARK = 2

    def toggle(self):
        return Themes.DARK if self == Themes.LIGHT else Themes.LIGHT

    def main_color(self):
        return "Light" if self == Themes.LIGHT else "Dark"

    def button_color(self):
        return get_color_from_hex('#B3C8CF') if self == Themes.LIGHT else get_color_from_hex('#89A8B2')