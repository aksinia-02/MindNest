from kivy.factory import Factory
from kivy.graphics import Color, Line
from kivy.lang import Builder
from kivy.properties import BooleanProperty, StringProperty
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton, MDFlatButton
import Themes

class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


# Register the custom widget
Factory.register('ClickableTextFieldRound', cls=ClickableTextFieldRound)


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

    def toggle_password_visibility(self, button):
        pass


DemoApp().run()