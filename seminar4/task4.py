from pathlib import Path
import threading


def words_counter(path: Path):
    with path.open('r', encoding='utf-8') as file:
        count_words = len(file.read().split())
        print(f'In file {path.name} {count_words} words')


def main():
    path = Path('files')
    threads = []
    for file in path.iterdir():
        if file.is_file():
            new_thread = threading.Thread(target=words_counter, args=(file,))
            threads.append(new_thread)
            new_thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()
