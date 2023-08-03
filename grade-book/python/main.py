#!/usr/bin/env python3

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
