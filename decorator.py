import time

def timing(f):
    t1 = time.time()
    f
    t2 = time.time()
    return t2 - t1


@timing
def sum():
    list = []
    for i in range(0, 10000):
        list.append(i)

a = sum
print a