package main

func GetGrade(a, b, c int) rune {
    score := ((a + b + c) / 3) / 10
    switch score {
    case 10, 9:
        return 'A'
    case 8:
        return 'B'
    case 7:
        return 'C'
    case 6:
        return 'D'
    default:
        return 'F'
    }
}
