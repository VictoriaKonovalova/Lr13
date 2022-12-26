#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sred_geometr(*args):
    if args:
        values = [float(arg) for arg in args]
        values.sort()
        a = 1
        n = len(values)
        for i in values:
            a = a * pow(i, (1 / n))
        return a
    else:
        return None


if __name__ == "__main__":
    print(sred_geometr(3, 6, 12, 18))
    print(sred_geometr())
    
    
