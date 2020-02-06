"""Этот модуль содержит одну функцию запроса сайта"""
import requests


def make_r(website):
    """
    Sends a GET request.

    Args:
        website (str): The first parameter.

    Returns:
        object: The return value.
    """
    r = requests.get(website)
    return r


if __name__ == "__main__":
    inquiry = make_r('https://yandex.ru/')
    print(inquiry.status_code)
