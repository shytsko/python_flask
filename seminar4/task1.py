import threading
import requests

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]


def get_url(url: str):
    response = requests.get(url)
    file_name = 'files/data_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(response.text)


if __name__ == '__main__':
    threads = []
    for url in urls:
        new_thread = threading.Thread(target=get_url, args=(url, ))
        threads.append(new_thread)
        new_thread.start()

    for thread in threads:
        thread.join()
