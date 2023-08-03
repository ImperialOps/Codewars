#!/usr/bin/env python3

import pytest

def get_grade(s1: int, s2: int, s3: int) -> str:
    score = (s1 + s2 + s3) / 3
    if score < 60:
        return 'F'
    elif score < 70:
        return 'D'
    elif score < 80:
        return 'C'
    elif score < 90:
        return 'B'
    return 'A'

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
    
