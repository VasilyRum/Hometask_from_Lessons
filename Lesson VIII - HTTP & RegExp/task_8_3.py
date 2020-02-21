"""
3. Напишите функцию, которая получает два аргумента
  1)путь к файлу изображения jpeg на компьютере (строка);
  2)имя целевого файла (строка)
  отправляет файл HTTP POST запросом на https://postman-echo.com/post .
  В ответе будет получен файл изображения jpeg, в виде octet-stream, который нужно раскодировать и
  сохранить на компьютере под целевым именем, переданным в аргументе.
  Функция должна вернуть размер сохраненного файла.
"""
import requests


def post(directory: str, name: str):
    with open('second_bg.jpg', 'rb') as f:
        files = {'photo': open(directory, 'rb')}
        response = requests.post('https://postman-echo.com/post', files=files)
        res = response.content
        filename = f'E:\{name}'
        with open(filename, 'wb') as f:
            f.write(res)
            size = len(res)

    return size


print(post('E:\second_bg.jpg', 'test.jpeg'))
