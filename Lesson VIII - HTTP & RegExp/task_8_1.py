"""
Напишите функцию, которая возвращает размер HTML документа по адресу https://google.com.
  Т.е. нужно получить страницу и вернуть ее размер (количество символов).
"""

import requests


def size_of_http(url: str):
    response = requests.get(url)
    return len(response.text)


TEST = requests.get("https://google.com")
