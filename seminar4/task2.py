# import threading
import multiprocessing
import requests

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]


def get_url(url: str):
    response = requests.get(url)
    file_name = 'files/data2_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(response.text)


if __name__ == '__main__':
    processes = []
    for url in urls:
        new_process = multiprocessing.Process(target=get_url, args=(url, ))
        processes.append(new_process)
        new_process.start()

    for process in processes:
        process.join()
