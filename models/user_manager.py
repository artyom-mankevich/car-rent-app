import hashlib

from models.database import Database
from extensions.singleton import Singleton


class UserManager(metaclass=Singleton):
    user = None

    def login(self, username, password):
        self.user = Database().login_user(username, password)

    def create_user(self, username, password):
        Database().create_user(username, password)

    def logout(self):
        self.user = None

    def get_hashed_string(self, string):
        return hashlib.sha256(string.encode('utf-8')).hexdigest()
