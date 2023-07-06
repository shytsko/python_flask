from pathlib import Path
import requests


def get_url_text_sync(url_list: list[str], path: Path):
    if not path.exists():
        path.mkdir(parents=True)

    for url in url_list:
        try:
            response = requests.get(url)
        except Exception as e:
            print(f"Не удалось загрузить данные {url=}")
        else:
            file = path.joinpath(url.replace('https://', '').replace('.', '_').replace('/', '') + '.html')
            with file.open('w', encoding='utf-8') as f_writer:
                f_writer.write(response.text)
