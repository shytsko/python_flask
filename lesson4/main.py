import random
from threading import Thread
from multiprocessing import Process
from time import sleep


def fun(num, sec):
    print(f"Старт задачи {num}, время работы {sec}")
    sleep(sec)
    print(f"Стоп задачи {num}")


if __name__ == '__main__':
    # threades = []
    #
    # for i in range(5):
    #     t = Thread(target=fun, args=(i, random.randint(5, 10)))
    #     threades.append(t)
    #     t.start()
    #
    # for t in threades:
    #     t.join()

    processes = []
    for i in range(5):
        p = Process(target=fun, args=(i, random.randint(5, 10)))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
