from multiprocessing import Pool
import time

def print_time(threadName, v):
    t1 = time.time()
    count = 0
    while count < v:
        count += 1
    t2 = time.time()
    print ('finished', threadName, count, t2 - t1)
    return count

if __name__ == '__main__':

    t1 = time.time()

    array = ('1', 1000)
    p = Pool()
    result = p.map(print_time('1', 10000), array)

    t2 = time.time()
    print(result)
    print(t2 - t1)
