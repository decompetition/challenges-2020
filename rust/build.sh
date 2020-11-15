#! /bin/sh
set -e

if [ $# -lt 2 ]; then
  echo "USAGE: $0 source binary [options]"
  exit 1
fi

source="$1"
binary="$2"
shift 2

rustc "$@" -o "$binary" "$source"
