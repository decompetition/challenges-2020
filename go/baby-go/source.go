package main

import (
    "os"
    "fmt"
    "strconv"
)

func main() {
  var i int

  i, _  = strconv.Atoi(os.Args[1])

  if i % 15 == 0 {
    fmt.Println("Green")
  } else if i % 3 == 0 {
    fmt.Println("Yellow")
  } else if i % 5 == 0 {
    fmt.Println("Blue")
  } else {
    fmt.Println(i)
  }
}
