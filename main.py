from kivy.lang import Builder
from kivymd.app import MDApp

import Pages
import Themes
from domain import User
from kivy.uix.screenmanager import ScreenManager, SlideTransition


class WindowManager(ScreenManager):
    pass


class DemoApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user = User()
        self.current_page = Pages.Pages.START
        self.current_theme = Themes.Themes.DARK
        self.theme_cls.theme_style = self.current_theme.main_color()
        self.button_color = self.current_theme.button_color()

    def build(self):
        Builder.load_file("frontend/kv_files/start.kv")
        Builder.load_file("frontend/kv_files/login.kv")
        Builder.load_file("frontend/kv_files/registration.kv")
        Builder.load_file("frontend/kv_files/windowmanager.kv")
        Builder.load_file("frontend/kv_files/home.kv")

        wm = WindowManager()
        if self.user.new_user():
            wm.current = "start"
        else:
            wm.current = "login"
            self.current_page = Pages.Pages.LOGIN
            print("login")

        return wm

    def toggle_theme(self):
        self.current_theme = self.current_theme.toggle()
        self.theme_cls.theme_style = self.current_theme.main_color()
        self.button_color = self.current_theme.button_color()

    def define_direction_switch_page(self, new_page):
        direction, new_page_type = self.current_page.direction_and_new_page(new_page)
        self.root.transition = SlideTransition(direction=direction)
        self.root.current = new_page
        self.current_page = new_page_type

    def save_new_user(self):
        start_screen = self.root.get_screen('start')

        name = start_screen.ids.user_name.text
        password_1 = start_screen.ids.password_1.text
        password_2 = start_screen.ids.password_2.text

        if self.check_passwords_match(password_1, password_2) and self.check_name(name):
            if self.user.save_new_user(name, password_1, password_2):
                self.define_direction_switch_page("login")

    def check_passwords_match(self, password_1, password_2):
        start_screen = self.root.get_screen('start')
        error_text_field = start_screen.ids.password_2
        if password_1 != password_2 and password_2 != "":
            error_text_field.error = True
            error_text_field.helper_text = "Passwords don't match"
            return False
        else:
            return True

    def check_name(self, name):
        start_screen = self.root.get_screen('start')
        error_text_field = start_screen.ids.user_name
        if name == "":
            error_text_field.error = True
            error_text_field.helper_text = "Name is required"
            return False
        return True

    def log_in(self):
        log_in_screen = self.root.get_screen('login')
        name = log_in_screen.ids.user_name.text
        password = log_in_screen.ids.password.text
        if self.check_name_password(name, password):
            self.define_direction_switch_page("home")

    def check_name_password(self, name, password):
        log_in_screen = self.root.get_screen('login')
        error_text_field_name = log_in_screen.ids.user_name
        error_text_field_password = log_in_screen.ids.password
        if not self.user.check_user_name(name):
            error_text_field_name.error = True
            error_text_field_name.helper_text = "User does not exist"
            error_text_field_password.error = True
            return False
        if not self.user.check_password(password):
            error_text_field_password.error = True
            error_text_field_password.helper_text = "Password is incorrect"
            return False
        return True


DemoApp().run()