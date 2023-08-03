#!/usr/bin/env python3

import pytest
from .main import get_grade

def test_get_value():
    tests = [
        (90, 96, 93, 'A'),
        (70, 70 , 100, 'B'),
        (75, 70, 79, 'C'),
        (60, 59, 64, 'D'),
        (44, 55, 52, 'F'),
    ]
    for test in tests:
        got = get_grade(test[0], test[1], test[2])
        assert got == test[3], f"got {got}, expected {test[3]}"
    
