import asyncio


async def print_number():
    for i in range(10):
        print(i)
        await asyncio.sleep(1)


async def print_letter():
    for letter in 'abcdefg':
        print(letter)
        await asyncio.sleep(0.6)


async def main():
    task1 = asyncio.create_task(print_number())
    task2 = asyncio.create_task(print_letter())
    await task1
    await task2


if __name__ == '__main__':
    asyncio.run(main())
