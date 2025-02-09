from bcrypt import hashpw, gensalt, checkpw
from database import get_password_from_database, save_user_in_database
import os

class User:

    def __init__(self):
        self.user_name = None
        self.hashed_password = None

    def new_user(self):
        return self.load_current_user() is None

    def save_new_password(self, password):
        self.hashed_password = hashpw(password.encode(), gensalt())

    def save_new_user(self, name, password_1, password_2):
        if password_1 == password_2:
            self.user_name = name
            self.hashed_password = hashpw(password_1.encode(), gensalt()).decode()
            save_user_in_database(self.user_name, self.hashed_password)
            self.save_current_session_in_file()
            return True
        return False

    def check_user_name(self, name):
        if self.new_user():
            return False
        return self.user_name == name

    def check_password(self, password):
        if self.new_user():
            return False
        stored_hashed_password = get_password_from_database(self.user_name)
        if stored_hashed_password:
            return checkpw(password.encode(), stored_hashed_password.encode())
        return False

    def save_current_session_in_file(self):
        """Saves the current username to a file for persistence."""
        with open("current_user.txt", "w") as file:
            file.write(self.user_name)

    def load_current_user(self):
        """Loads the last logged-in user from the file."""
        if os.path.exists("current_user.txt"):
            with open("current_user.txt", "r") as file:
                return file.read().strip()
        return None

