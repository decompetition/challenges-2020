#! /bin/sh -e

if [ $# -lt 2 ]; then
  echo "USAGE: $0 source binary"
  exit 1
fi

go build -o "$2" "$1"
