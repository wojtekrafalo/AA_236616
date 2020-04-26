import math
from enum import Enum
from hashlib import sha3_256, md5, sha256, sha224
import random

infinity = 1_000_000_000
infinity_f = float(1_000_000_000)
unique_ratio = 0.05
chance_of_duplicate = 50


def unique_sum(multi_set, hash_function, m):
    M = [infinity] * m
    for v in multi_set:
        for k in range(1, m + 1):
            u = hash_function(str(v.idx) + str(k))
            frac = (-1) * math.log(u) / v.lam
            if frac < M[k - 1]:
                M[k - 1] = frac
    sigma = 0
    for k in range(0, m):
        sigma += M[k]
    return (m - 1) / sigma


class Scenario(Enum):
    EQUAL = 0
    LINEAR = 1
    SIMILAR = 2


def get_multi_set(n, has_duplicates=False, kind_of_set=Scenario.EQUAL, a=1, b=1):
    multiset = []
    multiply = 10
    if a <= b:
        base_element = random.randint(a, b)
    else:
        base_element = a

    for i in range(1, n + 1):
        idx_str = int(n * (n - 1) / 2 + i)
        idx = "{0:b}".format(idx_str)

        if kind_of_set == Scenario.EQUAL:
            lam = base_element
        elif kind_of_set == Scenario.LINEAR:
            lam = random.randint(a, b)
        elif kind_of_set == Scenario.SIMILAR:
            if random.randint(0, 100) >= (unique_ratio * 100):
                lam = random.randint(b - a, b + a)
            else:
                lam = random.randint(a + multiply * b, infinity)
        else:
            lam = base_element

        obj = Element(idx, lam)
        multiset.append(obj)
        if has_duplicates:
            rand = random.randint(0, 100)
            if rand <= chance_of_duplicate:
                j = random.randint(0, len(multiset) - 1)
                duplicate = multiset.__getitem__(j)
                multiset.append(duplicate)
    return multiset


def default_hash(x):
    h = hash(x)
    base = 10_000_000_000
    if h < 0:
        h += base
    return float(h / base)


def sha224_hash(x):
    return int(sha224(x.encode("utf-8")).hexdigest(), 16) / (2 ** 256)


def sha3_256_hash(x):
    return int(sha3_256(x.encode("utf-8")).hexdigest(), 16) / (2 ** 256)


def sha_256_hash(x):
    return int(sha256(x.encode("utf-8")).hexdigest(), 16) / (2 ** 256)


def md5_hash(x):
    return int(md5(x.encode("utf-8")).hexdigest(), 16) / (2 ** 128)


def simple_hash(x):
    base = 60
    h = 0
    idx = 0
    for c in x:
        h = h * base + ord(c)
        idx += 1
    return float(h / (base ** idx))


class Element:
    def __init__(self, idx, lam):
        self.idx = idx
        self.lam = lam

    def __str__(self):
        return "(" + str(self.idx) + ", " + str(self.lam) + ")"


def print_multiset(m):
    print("Multiset: [", end='')
    for v in m:
        print("(" + str(v.idx) + ", " + str(v.lam) + "), ", end='')
    print(" ]")


def simple_sum(multi_set):
    all_sum = 0
    for v in multi_set:
        all_sum += v.lam
    return all_sum


def unique_real_sum(multi_set):
    real_sum, _ = count_real_sum(multi_set)
    return real_sum


def unique_real_avg(multi_set):
    real_sum, n = count_real_sum(multi_set)
    return float(real_sum / n)


def count_real_sum(multi_set):
    s = set()
    all_sum = 0
    for v in multi_set:
        if v.idx not in s:
            s.add(v.idx)
            all_sum += v.lam
    return all_sum, len(s)


def unique_avg(multi_set, hash_function, m):
    m_sum = [infinity] * m
    m_avg = [infinity_f] * m
    for v in multi_set:
        for k in range(1, m + 1):
            u = hash_function(str(v.idx) + str(k))
            log = (-1) * math.log(u) / 1.0
            frac_sum = log / v.lam
            if frac_sum < m_sum[k - 1]:
                m_sum[k - 1] = frac_sum
            if log < m_avg[k - 1]:
                m_avg[k - 1] = log
    sigma = 0
    for k in range(0, m):
        sigma += m_sum[k]
    est_sum = float((m - 1) / sigma)
    sigma = 0
    for k in range(0, m):
        sigma += m_avg[k]
    est_avg = float((m - 1) / sigma)
    return float(est_sum / est_avg)
