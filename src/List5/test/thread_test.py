import threading
import time
import random

infinity = 500


class Object:
    def __init__(self, i=None, neigh=None):
        self.i = i
        self.x = 0
        self.neigh = neigh
        self.lock = threading.Lock()

    def print_and_set_values(self, x):
        with self.lock:
            self.x = x
            print(str(self.i) + ": " + str(self.neigh.x))
            # time.sleep(get_random_time())


def get_random_time():
    return random.random()


def thread_function(obj):
    for x in range(0, infinity):
        obj.print_and_set_values(x)


def test_thread():
    obj1 = Object(1)
    obj2 = Object(2, obj1)
    obj1.neigh = obj2

    th1 = threading.Thread(target=thread_function, args=(obj1,))
    th2 = threading.Thread(target=thread_function, args=(obj2,))
    th1.start()
    th2.start()


test_thread()

