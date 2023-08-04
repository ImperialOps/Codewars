#!/usr/bin/env python3

def count_by(x: int, y: int) -> list:
    result = []
    for i in range(y):
        result.append((i+1)*x)
    return result
