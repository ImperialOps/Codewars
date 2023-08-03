package main

import (
    "testing"

    "github.com/stretchr/testify/assert"
)

func TestGetGrade(t *testing.T) {
    tests := []struct {
        a, b, c int
        expected rune
    }{
        {90, 96, 93, 'A'},
        {70, 70, 100, 'B'},
        {75, 70, 79, 'C'},
        {60, 59, 64, 'D'},
        {44, 55, 52, 'F'},
    }
    for _, test := range tests {
        got := GetGrade(test.a, test.b, test.c)
        assert.Equal(t, got, test.expected, "got %v, expected %v", string(got), string(test.expected))
    }
}
