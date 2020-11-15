# Decompetition 2020 Challenges

This is the full set of challenges used for Decompetition 2020 - the very first one!

Challenges are grouped by language.  Inside each challenge folder you'll find:

- `binary.out` is the binary itself.  Debug symbols are removed.
- `bnil.yml` contains Binary Ninja Intermediate Language for the functions we care about.
- `deco.py` is a symlink to the test helper.  The real file is in the root of the repo.
- `disasm.yml` contains disassembly for all the functions we care about.
- `source.xxx` is the original source code for the binary.
- `starter.xxx` is the starting source code that was provided to the players.
- `test.py` contains the secret test cases that were used to check functionality.


## The C Challenges

### `baby-c`

The `foo()` function implements a very inefficient version of the [Euclidean
Algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm) for finding the
greatest common divisor of two numbers, using subtraction instead of modulo.
If you give it any negative numbers it'll go into a near-infinite loop.

### `bitesize`

This one is exploitable! The `sum()` function uses an `unsigned char` to store
the input length, so you can trick it into overflowing the input buffer by
giving it a size greater than 255.  Note that this one has a custom build script
that disables security measures - one of the tests makes sure that it is really
exploitable.

### `prime`

This is a simple but efficient primality check.  It special-cases a few low
primes, and then loops in steps of six, checking possible factors.  It stops
when it reaches the square root of the number being tested.

### `rootkit`

This one reads in a "process list" and stores it in a linked list.  It then
iterates over the list looking for evil process 1337.  The heart of the
challenge is reversing the data structure that's being used.


## The C++ Challenges

### `baby-cpp`

This one takes two strings as arguments: a "hand" and a "word", like in the
game [Scrabble](https://en.wikipedia.org/wiki/Scrabble).  If you can make `word`
using only the letters in `hand` then it calculates your score (`word` doesn't
have to be a real word).

### `lambic`

A brewery simulator!  Also a vast patchwork of C++ lambda functions.

### `pedigree`

This one reads a family tree from standard input, one person at a time.  It then
finds the person named in the command line arguments and prints their ancestors
and descendants.  The `Person::ALL` map needs a seed entry for this one to work
properly - this initialization code wasn't diffed, and caught a lot of people
off guard.

### `streamy`

An equation converter.  It reads standard input (or a file) as a series of
[reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)
expressions and prints (or writes) their infix equivalents - and it uses a
whole bunch of C++ stream types to do it.  There's also a bit of inheritance
and some virtual functions.

### `unfair`

This one encrypts its input with a [Playfair cipher](https://en.wikipedia.org/wiki/Playfair_cipher).
Any non-alphabetical characters are discarded.  Note that it doesn't add
separators between repeated characters as in the original cipher.


## The Go Challenges

### `baby-go`

It's FizzBuzz!  Except the output has been changed to make it slightly less
obvious that it's FizzBuzz!

### `batsounds`

This one starts a TCP echo server listening on port 20080. If no one connects
within 100 milliseconds it gives up and exits.

### `carshop`

This one reads in a list of cars, and then sees if a car like the one requested
on the command line is available.  It's another type recovery challenge, with
some enums thrown in for good measure.

### `fabulous`

Originally named `fibl`, this one got renamed to make it a little less clear
what it was implementing: a linked list storing the first N [Fibonacci
numbers](https://en.wikipedia.org/wiki/Fibonacci_number).

### `julie`

This one uses a syscall to find the dimensions of the current console, and then
uses `complex128`s to create a [Julia set](https://en.wikipedia.org/wiki/Julia_set)
in ASCII art.  This is the only challenge that was never fully solved.

### `switcher`

Sort-of-ROT-13-ish encryption!  It uses a switch to treat capital letters,
lowercase letters, and non-letters all differently.

### `wolfgang`

An [elementary cellular automaton](https://mathworld.wolfram.com/ElementaryCellularAutomaton.html)
simulator.  You provide the rule number on the command line and it'll output
the first twentyish steps, starting from a single centered seed.


## The Rust Challenges

### `baby-rust`

Is that string a number?  This one uses string parsing and match-based result
unwrapping to help you find out.

### `habidasher`

This one computes a few [simple but lesser-known hashes](http://www.cse.yorku.ca/~oz/hash.html)
of its command line argument and prints the results.

### `s2ring`

This one takes a random seed, a starting string, and a list of possible
string substitutions.  It then performs up to N random substitutions.  This is
essentially evaluating an [unrestricted grammar](https://en.wikipedia.org/wiki/Unrestricted_grammar),
which is equivalent to a Turing machine - hence the name.

### `toobz`

A series of tubes - like the internet!  This one pipes its standard input to its
standard output through an arbitrarily complex series of TCP connections.  Port
numbers are read from the command line.


## The Swift Challenges

### `baby-swift`

What is that thing you have there?  Is it HOTDOG or is it NOT HOTDOG?  This
disruptive cloud service uses blockchain and artificial intelligence to help
you find out.

### `bandate`

This one does date parsing.  It also knows the birthdays of all the Beatles.

### `cardigan`

This one expects a credit card number to pay for your many, many sweaters.  If
you give it one, it'll run a [Luhn check](https://en.wikipedia.org/wiki/Luhn_algorithm)
to validate it, and if the check is successful it'll print the card's issuer.
The [IIN](https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_%40IIN%41)
database is "encrypted" to make it a little less obvious what's happening.
