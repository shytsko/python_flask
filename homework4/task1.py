# � Напишите программу, которая будет скачивать страницы из списка URL-адресов и сохранять их в
#   отдельные файлы на диске.
# � В списке может быть несколько сотен URL-адресов.
# � При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# � Представьте три варианта решения.

import csv


def get_url_text(url: str):


if __name__ == '__main__':
    with open('task1_urls.csv', 'r', newline='', encoding='utf-8') as f:
        csv_reader = csv.DictReader(f, dialect='excel-tab', delimiter=';')
        for line in csv_reader:
            print(line['URL'])
