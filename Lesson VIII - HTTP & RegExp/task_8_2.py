"""
2. Напишите функцию, которая принимает три аргумента
  1)число, количество денег в исходной валюте, float;
  2)исходная валюта, трехсимвольная строка, str;
  3)целевая валюта, трехсимвольная строка, str;
  и возвращает количество денег в целевой валюте (тип float).
  Для получения курса валют воспользуйтесь https://api.exchangerate-api.com .
"""
import requests

def converter(value: float, current_cur: str, needed_cur: str):
    url = "https://api.exchangerate-api.com/v4/latest/" + current_cur
    response = requests.get(url)
    data = response.json()
    rates = data["rates"]
    rate = rates[needed_cur]
    out_cur = rate * value
    return out_cur


#
# A = converter(1.0, "USD", "AUD")
# print(A)
