from kivy.lang import Builder
from kivymd.app import MDApp
import Themes


class DemoApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_theme = Themes.Themes.DARK
        self.theme_cls.theme_style = self.current_theme.main_color()
        self.button_color = self.current_theme.button_color()

    def build(self):
        return Builder.load_file('login.kv')

    def toggle_theme(self):
        self.current_theme = self.current_theme.toggle()
        self.theme_cls.theme_style = self.current_theme.main_color()
        self.button_color = self.current_theme.button_color()
        print(f"Current Theme: {self.theme_cls.theme_style}")


DemoApp().run()