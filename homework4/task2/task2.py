# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
# Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения
# в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени
# выполнения программы.

from pathlib import Path
from task2_threading import download_img_threading
from task2_multiprocessing import download_img_multiprocessing
from task2_async import download_img_async

if __name__ == '__main__':
    with open('task2_urls.txt', 'r', encoding='utf-8') as f:
        url_list = f.readlines()

    url_list = list(map(str.strip, url_list))

    download_img_threading(url_list, Path.cwd().joinpath('task2_files', 'threading'), 5)
    download_img_multiprocessing(url_list, Path.cwd().joinpath('task2_files', 'multiprocessing'), 5)
    download_img_async(url_list, Path.cwd().joinpath('task2_files', 'async'), 5)
