import asyncio
import aiohttp
from pathlib import Path


async def words_counter(path: Path):
    with path.open('r', encoding='utf-8') as file:
        count_words = len(file.read().split())
        print(f'In file {path.name} {count_words} words')


async def main():
    path = Path('files')
    tasks = []
    for file in path.iterdir():
        if file.is_file():
            task = asyncio.create_task(words_counter(file))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
