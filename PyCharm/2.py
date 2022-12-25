#!/usr/bin/env python3
# -*- coding: utf-8 -*

def sred_garmoni(*args):
    if args:
        values = [float(arg) for arg in args]
        n = len(values)
        a = 0
        for i in values:
            a = a + (1 / i)
        return n / a
    else:
        return None


if __name__ == "__main__":
    print(sred_garmoni())
    print(sred_garmoni(4, 7, 13, 21))
