#!/usr/bin/env python3

import itertools

def alternate(*args):
    iter_functions = [arg() for arg in args]
    while True:
        for iter_function in iter_functions:
            yield next(iter_function)
