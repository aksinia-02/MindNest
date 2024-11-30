from bcrypt import hashpw, gensalt, checkpw


class User:

    def __init__(self):
        self.user_name = None
        self.hashed_password = None

    def new_user(self):
        return self.hashed_password is None and self.user_name is None

    def save_new_password(self, password):
        self.hashed_password = hashpw(password.encode(), gensalt())

    def save_new_user(self, name, password_1, password_2):
        if password_1 == password_2:
            self.user_name = name
            self.hashed_password = hashpw(password_1.encode(), gensalt())
            return True
        return False

    def check_user_name(self, name):
        if self.new_user():
            return False
        return self.user_name == name

    def check_password(self, password):
        if self.new_user():
            return False
        return checkpw(password.encode(), self.hashed_password)
