package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestNbrOfLaps(t *testing.T) {
	tests := []struct {
		given  [2]uint16
		expect [2]uint16
	}{
		{[2]uint16{5, 3}, [2]uint16{3, 5}},
		{[2]uint16{4, 6}, [2]uint16{3, 2}},
		{[2]uint16{5, 5}, [2]uint16{1, 1}},
	}
	for _, test := range tests {
		got := NbrOfLaps(test.given[0], test.given[1])
		assert.Equal(t, got, test.expect, "got %v, expected %v", got, test.expect)
	}
}
