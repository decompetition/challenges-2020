package main

import (
	"container/list"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var index int

	index, _ = strconv.Atoi(os.Args[1])

	l := list.New()
	l.PushFront(0)
	l.PushFront(1)

	for i := 0; i < index; i++ {
		first := l.Front()
		second := first.Next()

		firstValue := first.Value.(int)
		secondValue := second.Value.(int)

		newValue := firstValue + secondValue
		l.PushFront(newValue)
	}

	fmt.Println(l.Front().Value)
}
