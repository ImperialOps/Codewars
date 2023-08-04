#!/usr/bin/env python3

import pytest
from .main import count_by

def test_count_by():
    tests = [
        [1, 0, []],
        [1, 5, [1, 2, 3, 4, 5]],
        [2, 5, [2, 4, 6, 8, 10]],
        [3, 6, [3, 6, 9, 12, 15, 18]],
        [50, 5, [50, 100, 150, 200, 250]],
        [100, 5, [100, 200, 300, 400, 500]]
    ]
    for test in tests:
        got = count_by(test[0], test[1])
        assert got == test[2], f"got {got}, expected {test[2]}"

