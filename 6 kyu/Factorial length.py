from math import pi, e, log, ceil


def count(n):
    return int(ceil(log(2 * pi * n, 10) / 2 + n * log(n / e, 10)))
