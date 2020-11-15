package main

import (
    "flag"
    "fmt"
    "math/cmplx"
    "os"
    "strconv"
    "syscall"
    "unsafe"
)

type winsize struct {
    Row    uint16
    Col    uint16
    Xpixel uint16
    Ypixel uint16
}

func julie(z complex128, c complex128) int {
    for n := 0; n < 100; n++ {
        if cmplx.Abs(z) > 2 {
            return n
        }

        z = z * z + c
    }

    return 100
}

func main() {
    flag.Usage = func() {
        fmt.Fprintf(os.Stderr, "Usage of %s: [options] r i\n", os.Args[0])
        flag.PrintDefaults()
    }

    ws := &winsize{}
    retCode, _, _ := syscall.Syscall(
        syscall.SYS_IOCTL,
        uintptr(syscall.Stdin),
        uintptr(syscall.TIOCGWINSZ),
        uintptr(unsafe.Pointer(ws)))

    if int(retCode) != 0 {
        ws.Row = 32
        ws.Col = 64
    }

    w := flag.Int("w", int(ws.Col), "width")
    h := flag.Int("h", int(ws.Row) - 1, "height")
    flag.Parse();

    if flag.NArg() != 2 {
        flag.Usage()
        os.Exit(1)
    }

    a, err := strconv.ParseFloat(flag.Arg(0), 64)
    if err != nil {
        flag.Usage()
        os.Exit(1)
    }

    b, err := strconv.ParseFloat(flag.Arg(1), 64)
    if err != nil {
        flag.Usage()
        os.Exit(1)
    }

    c := complex(a, b)
    for y := 0; y < *h; y++ {
        r := float64(y) / float64(*h - 1) * 3 - 1.5
        for x := 0; x < *w; x++ {
            i := float64(x) / float64(*w - 1) * 2 - 1
            z := complex(r, i)
            n := julie(z, c)

            if n == 100 {
                fmt.Print("#")
            } else if n >= 75 {
                fmt.Print("=")
            } else if n >= 50 {
                fmt.Print("+")
            } else if n >= 25 {
                fmt.Print("-")
            } else {
                fmt.Print(" ")
            }
        }

        fmt.Print("\n")
    }
}
