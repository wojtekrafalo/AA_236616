import math
from hashlib import sha3_256, md5, sha256, sha224
import random


def min_count(k, hash_function, multi_set):
    m = [1.0] * k
    for v in multi_set:
        h = hash_function(v)
        if h < m[k - 1] and h not in m:
            m[k - 1] = h
            m.sort()
    if m[k - 1] == 1:
        s = 0
        for n in m:
            if n != 1.0:
                s = s + 1
        return s
    return (k - 1) / m[k - 1]


def get_multi_set(n, has_duplicates):
    multiset = []
    duplicates = []
    for i in range(1, n + 1):
        multiset.append(str(int(n * (n - 1) / 2 + i)))

    if has_duplicates:
        for _ in range(n):
            duplicates.append(multiset[random.randint(0, n - 1)])
        multiset += duplicates
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

