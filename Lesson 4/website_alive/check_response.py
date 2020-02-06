"""This module contains one function to check the website"""
import website_alive.make_request


def check_r(url: str):

    """
    Checks whether the site is alive

    Args:
        url: The first parameter.

    Returns:
        object: The return value. True - Yes. False - site is dead
    """

    r = website_alive.make_request.make_r(url)
    if r.status_code == 200:
        return True
    else:
        return False


if __name__ == "__main__":
    inquiry = check_r('https://yandex.ru/')
    print(inquiry)