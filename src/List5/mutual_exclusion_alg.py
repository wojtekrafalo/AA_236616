import random
import logging
import threading
import time

infinity = 5_000


def get_random_time():
    return random.random() / 10.0


class Register:
    def __init__(self, i=None, x=None, left=None):
        self.right = None
        self.i = i
        self.x = x
        if left is not None:
            if type(left) is Register:
                self.left = left
            else:
                raise Exception("Wrong type of neighbour!")

    def set_right(self, right):
        if type(right) is Register:
            self.right = right
        else:
            raise Exception("Wrong type of neighbour!")

    def set_left(self, left):
        if type(left) is Register:
            self.left = left
        else:
            raise Exception("Wrong type of neighbour!")


def generate_random_x_vector(n):
    x_values = [0] * n
    for i in range(n):
        x_values[i] = random.randint(0, n + 1)
    return x_values


def generate_registers(n, x_values):
    registers = [Register()] * n
    registers[0] = Register(1, x_values[0])

    # create with left register - previous in list
    for i in range(1, n):
        registers[i] = Register(i + 1, x_values[i], registers[i - 1])
    registers[0].set_left(registers[n - 1])

    # set right register - next in list
    for i in range(0, n):
        registers[i].set_right(registers[(i + 1) % n])
    return registers


def dijkstra_thread_function(register, n):
    if register.i == 1:
        for i in range(0, infinity):
            if register.x == register.left.x:
                register.x = (register.x + 1) % (n + 1)
            time.sleep(get_random_time())
    else:
        for i in range(0, infinity):
            if register.x != register.left.x:
                register.x = register.left.x
            time.sleep(get_random_time())
    print("Thread: " + str(register.i) + ": " + str(register.x))


def dijkstra_mutual_exclusion(n, x_values):
    if n < 1:
        raise Exception("Not enough registers!")

    if x_values is None:
        x_values = generate_random_x_vector(n)
    registers = generate_registers(n, x_values)

    for reg in registers:
        th = threading.Thread(target=dijkstra_thread_function, args=(reg, n))
        th.start()

    return registers
