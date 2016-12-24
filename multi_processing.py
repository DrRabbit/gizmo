from threading import Thread
import time
from multiprocessing import Process

def print_time(threadName, v):
    t1 = time.time()
    count = 0
    while count < v:
        count += 1
    t2 = time.time()
    print('finished', threadName, count, t2 - t1)


if __name__ == '__main__':

    t1 = time.time()

    pro = []
    for i in range(7):
        pro.append(Process(target=print_time, args=(str(i + 1), 100000000, )))
        pro[i].start()

    for p in pro:
        p.join()

    t2 = time.time()
    print(t2 - t1)



