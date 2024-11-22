from kivy.lang import Builder
from kivymd.app import MDApp
import Themes
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition


class LoginWindow(Screen):
    pass


class RegistryWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class DemoApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_theme = Themes.Themes.DARK
        self.theme_cls.theme_style = self.current_theme.main_color()
        self.button_color = self.current_theme.button_color()

    def build(self):
        Builder.load_file("login.kv")
        Builder.load_file("registry.kv")
        Builder.load_file("windowmanager.kv")
        return Builder.load_file("windowmanager.kv")

    def toggle_theme(self):
        self.current_theme = self.current_theme.toggle()
        self.theme_cls.theme_style = self.current_theme.main_color()
        self.button_color = self.current_theme.button_color()
        print(f"Current Theme: {self.theme_cls.theme_style}")

    def switch_to_registry(self):
        self.root.transition = SlideTransition(direction="left")
        self.root.current = "registry"

    def switch_to_login(self):
        self.root.transition = SlideTransition(direction="right")
        self.root.current = "login"


DemoApp().run()