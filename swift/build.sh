#! /bin/bash
set -e

if [ $# -lt 2 ]; then
  echo "USAGE: $0 source binary [options]"
  exit 1
fi

source="$1"
binary="$2"
shift 2

# Stupid path hack 'cause Docker isn't running /etc/bash.bashrc:
if [ -f "/opt/swift/usr/bin/swiftc" ]; then
  /opt/swift/usr/bin/swiftc "$@" -g -o "$binary" "$source"
else
  swiftc "$@" -g -o "$binary" "$source"
fi
