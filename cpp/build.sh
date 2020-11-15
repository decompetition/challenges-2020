#! /bin/sh
set -e

if [ $# -lt 2 ]; then
  echo "USAGE: $0 source binary [options]"
  exit 1
fi

source="$1"
binary="$2"
shift 2

if grep -v include "$source" |
   g++  -E -nostdinc -undef -o - - |
   grep -qF "__asm" ;
then
  echo "Nice try."
  exit 1
fi

g++ "$@" -fno-asm -std=c++17 -g -o "$binary" "$source"
