import re


def check_username(username: str) -> bool:
    if 3 < len(username) <= 30:
        pattern = re.compile(r'\D\w+\S')
        match = pattern.fullmatch(username)
        if match is not None:
            return True
    return False


def check_password(password: str) -> bool:
    if 3 < len(password) <= 100:
        pattern = re.compile(r'\w+\S')
        match = pattern.fullmatch(password)
        if match is not None:
            return True
    return False


def check_search(string: str) -> bool:
    if 0 < len(string) <= 50:
        pattern = re.compile(r'[a-zA-Z- ]+')
        match = pattern.fullmatch(string)
        if match is not None:
            return True
    return False


def check_count(string: str, upper_limit: int) -> bool:
    if 0 < len(string) <= upper_limit:
        pattern = re.compile(r'\d+')
        match = pattern.fullmatch(string)
        if match is not None:
            return True
    return False


if __name__ == '__main__':
    print(check_username('1abaob1'))
    print(check_password('a' * 100))
    print(check_search('BMW b'))
