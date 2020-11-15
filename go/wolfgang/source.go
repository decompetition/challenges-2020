package main

import (
	"fmt"
	"os"
	"strconv"
)

// https://mathworld.wolfram.com/ElementaryCellularAutomaton.html
func step(line string, rule int) string {
	bits := uint(0)
	line += " "
	next := ""

	for i, char := range line {
		bits = (bits << 1) & 7
		if char == '#' {
			bits |= 1
		}

		if i == 0 {
			continue
		} else if rule & (1 << bits) != 0 {
			next += "#"
		} else {
			next += " "
		}
	}

	return next
}

func main() {
	line := "               #               "
	rule, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Println("USAGE: ./wolfgang [rule]")
		os.Exit(1)
	}

	for i := 0; i < 16; i += 1 {
		fmt.Println(line)
		line = step(line, rule)
	}
}
