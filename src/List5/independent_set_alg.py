import random
import logging
import threading
import time

infinity = 1_000


def get_random_time():
    return random.random() / 10.0


class Node:
    def __init__(self, i):
        self.right = None
        self.i = i
        self.is_independent = False
        self.neighs = None

    def set_neighs(self, neighs):
        if not isinstance(neighs, (list,)):
            raise Exception("Neighbours should be given in list!")
        self.neighs = neighs


def find_maximal_independent(graph):

    for node in graph:
        th = threading.Thread(target=independent_thread_function, args=(node,))
        th.start()

    independent_set = []
    for node in graph:
        if node.is_independent:
            independent_set.append(node)

    return independent_set


def independent_thread_function(node):

    if not node.is_independent:
        to_independent = True
        for neigh in node.neighs:
            if neigh.is_independent:
                to_independent = False
        node.is_independent = to_independent

    if node.is_independent:
        for neigh in node.neighs:
            if neigh.is_independent:
                node.is_independent = False

