import time
from multiprocessing import Process


def eat():  # 吃东西
    while True:
        print('he eating something')
        time.sleep(2)   # 休息一下再吃


def praise():  # 表杨
    while True:
        print('he is good man')
        time.sleep(3)


if __name__ == '__main__':
    eatProcess = Process(target=eat)
    eatProcess.start()
    praise()