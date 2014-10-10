import itertools


def grouper(iterable, n, fillvalue=None):
    """grouper('ASD', 2, 'X') -> [('A', 'S'), ('D', 'X')]"""
    args = [iter(iterable)] * n
    return itertools.izip_longest(*args, fillvalue=fillvalue)


def rotate(l):
    """rotate('ASD') -> 'SDA'"""
    return l[1:] + [l[0]]