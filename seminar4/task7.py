# Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами от 1 до 100.
# � При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения вычислений.
import random
import threading
import multiprocessing
import time
import asyncio


def my_sum(arr):
    result = 0
    for i in arr:
        result += i
    return result


def sum_threading(arr):
    result = 0

    def my_sum_th(arr, start, end):
        nonlocal result
        local_result = 0
        for i in range(start, end):
            local_result += arr[i]
        result += local_result

    step_index = len(arr) // 4
    thread1 = threading.Thread(target=my_sum_th, args=(arr, 0, step_index * 1))
    thread2 = threading.Thread(target=my_sum_th, args=(arr, step_index * 1, step_index * 2))
    thread3 = threading.Thread(target=my_sum_th, args=(arr, step_index * 2, step_index * 3))
    thread4 = threading.Thread(target=my_sum_th, args=(arr, step_index * 3, step_index * 4))
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    return result


def _my_sum_pr(arr, start, end, res):
    local_result = 0
    for i in range(start, end):
        local_result += arr[i]
    with res.get_lock():
        res.value += local_result


def sum_multiproccesing(arr):
    result = multiprocessing.Value('q', 0)

    step_index = len(arr) // 4
    process1 = multiprocessing.Process(target=_my_sum_pr, args=(arr, 0, step_index * 1, result))
    process2 = multiprocessing.Process(target=_my_sum_pr, args=(arr, step_index * 1, step_index * 2, result))
    process3 = multiprocessing.Process(target=_my_sum_pr, args=(arr, step_index * 2, step_index * 3, result))
    process4 = multiprocessing.Process(target=_my_sum_pr, args=(arr, step_index * 3, step_index * 4, result))
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process1.join()
    process2.join()
    process3.join()
    process4.join()

    return result.value


def sum_async(arr):
    result = 0

    async def my_sum_async(arr, start, end):
        print(f"Start {start=}")
        local_result = 0
        for i in range(start, end):
            local_result += arr[i]
        print(f"End {start=}")
        return local_result

    async def sum_main(arr):
        nonlocal result
        step_index = len(arr) // 4
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(my_sum_async(arr, 0, step_index * 1))
            task2 = tg.create_task(my_sum_async(arr, step_index * 1, step_index * 2))
            task3 = tg.create_task(my_sum_async(arr, step_index * 2, step_index * 3))
            task4 = tg.create_task(my_sum_async(arr, step_index * 3, step_index * 4))

        result += task1.result()
        result += task2.result()
        result += task3.result()
        result += task4.result()

        return result

    return asyncio.run(sum_main(arr))


if __name__ == '__main__':
    arr = [random.randint(1, 100) for _ in range(1000000)]

    start = time.time()
    sum1 = my_sum(arr)
    print(f"Подсчет синхронный {sum1=}:  {time.time() - start} sec")
    start = time.time()
    sum2 = sum_threading(arr)
    print(f"Подсчет многопоточный {sum2=}:  {time.time() - start} sec")
    start = time.time()
    sum3 = sum_multiproccesing(arr)
    print(f"Подсчет многопроцессорный {sum3=}:  {time.time() - start} sec")
    start = time.time()
    sum4 = sum_async(arr)
    print(f"Подсчет асинхронный {sum4=}:  {time.time() - start} sec")
