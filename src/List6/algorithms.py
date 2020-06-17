from random import random

counted_calls_f = [0]


def recursive_f(n):
    if n == 0:
        return 1
    s = 0
    for i in range(0, n):
        s += recursive_f(i)
    return s


def fun_2_n_minus(n):
    return pow(2, n) - 1


def fun_2_n_plus(n):
    return pow(2, n+1)


def count_lines_f_recursive(n):
    if n == 0:
        return 0
    s = 0
    for i in range(0, n):
        s += count_lines_f_recursive(i)
        s += 1
    return s


def count_lines_f_iterative(n):
    for i in range(len(counted_calls_f), n + 1):
        s = 0
        for j in range(0, i):
            s += counted_calls_f[j]
            s += 1
        counted_calls_f.append(s)
    return counted_calls_f[n]


def compare_funs(fun_p, fun_f, times):
    i = 0
    while i < times:
        if fun_f(i) != fun_p(i):
            return False
        i += 1
    return True


def compare_funs_arr(fun_p, fun_f, times, delta):
    i = 0
    while i < times:
        exact = fun_f(i)
        rounded = fun_p(i)
        if exact < rounded - delta or exact > rounded + delta:
            return False
        i += 1
    return True


def fun_arr_recursive(arr):
    n = len(arr)
    s = 1
    if n < 2:
        # raise Exception("n too small. Should be at least 2!")
        return 0
    for k in range(1, n):
        prob = random()
        if prob >= 0.5:
            # get random subarray of size k.
            sub_arr = arr[:k]
            s += fun_arr_recursive(sub_arr)
    return s


def fun_arr_in_situ(n):
    s = 1
    if n < 2:
        return 1
    for k in range(1, n + 1):
        prob = random()
        if prob >= 0.5:
            s += fun_arr_in_situ(k)
    return s


def test_avg_fun_arr(times, n):
    arr = fill_arr(n)
    avg = 0
    for i in range(0, times):
        # avg += fun_arr_recursive(arr)
        avg += fun_arr_in_situ(n)
    avg /= times
    return avg


def fill_arr(n):
    arr = []
    for i in range(0, n):
        arr.append(0)
    return arr
