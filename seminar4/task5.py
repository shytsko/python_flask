from pathlib import Path
import multiprocessing


def words_counter(path: Path):
    with path.open('r', encoding='utf-8') as file:
        count_words = len(file.read().split())
        print(f'In file {path.name} {count_words} words')


def main():
    path = Path('files')
    processes = []
    for file in path.iterdir():
        if file.is_file():
            new_process = multiprocessing.Process(target=words_counter, args=(file,))
            processes.append(new_process)
            new_process.start()

    for process in processes:
        process.join()


if __name__ == '__main__':
    main()
