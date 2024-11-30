from enum import Enum


class Pages(Enum):
    START = "start"
    LOGIN = "login"
    REGISTRATION = "registration"
    HOME = "home"

    def direction_and_new_page(self, page):
        new_page = Pages(page.lower())
        direction = "left" if self in {Pages.START, Pages.LOGIN, Pages.HOME} else "right"
        return direction, new_page
