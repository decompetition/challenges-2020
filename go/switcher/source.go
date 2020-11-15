package main

import (
  "bytes"
  "os"
  "fmt"
)

func compute(input string) []byte {
  b := []byte(input)
  // fmt.Println(b)

  rot13 := func(r rune) rune {
    switch {
      case r >= 'A' && r <= 'Z':
        return 'A' + (r-'A'+13)%26
      case r >= 'a' && r <= 'z':
        return 'a' + (r-'a'+29)%26
      default:
        return r-10
    }
    return r
  }

  // https://golang.org/pkg/bytes/#example_Map
  return bytes.Map(rot13, b)
}

func main() {
  if len(os.Args) < 2 {
    fmt.Println("method requires an arg")
  } else {
    i  := os.Args[1]
    bs := compute(i);
    fmt.Println(string(bs))
  }
}
