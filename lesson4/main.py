import random
from threading import Thread
from time import sleep


def fun(num, sec):
    print(f"Старт потока {num}, время работы {sec}")
    sleep(sec)
    print(f"Стоп потока {num}")


if __name__ == '__main__':
    threades = []

    for i in range(5):
        t = Thread(target=fun, args=(i, random.randint(5, 10)))
        threades.append(t)
        t.start()

    for t in threades:
        t.join()
