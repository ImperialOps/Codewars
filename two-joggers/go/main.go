package main

func NbrOfLaps(x, y uint16) [2]uint16 {
    if x == y {
        return [2]uint16{1, 1}
    }
    total := x*y
	return [2]uint16{total/x, total/y}
}
