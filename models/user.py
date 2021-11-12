class User:
    def __init__(self, username, id, is_staff=False):
        self.id = id
        self.username = username
        self.is_staff = is_staff
