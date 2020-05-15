import math
from scipy.special import binom
from random import random


def nakamoto_prob(n, q):
    p = 1 - q
    lam = n * (q / p)
    prob = 1.0
    for k in range(n):
        prob -= math.e ** (-lam) * ((lam ** k) / math.factorial(k)) * (1 - (q / p) ** (n - k))
    return prob


def grunspan_prob(n, q):
    p = 1 - q
    prob = 1.0
    for k in range(n):
        prob -= (p ** n * q ** k - q ** n * p ** k) * binom(k + n - 1, k)
    return prob


def simulate(n, q):
    time_limit = 1000
    p = 1 - q
    adversary_blocks = 0
    users_blocks = 0
    while adversary_blocks < n and users_blocks < n:
        if random() < q:
            adversary_blocks += 1
        if random() < p:
            users_blocks += 1

    for i in range(time_limit):
        if adversary_blocks >= users_blocks:
            return 1
        if random() < q:
            adversary_blocks += 1
        if random() < p:
            users_blocks += 1
    return 0


def experimental_prob(n, q):
    all_tries = 1000
    no_wins = 0
    for i in range(all_tries):
        no_wins += simulate(n, q)
    return no_wins / all_tries
