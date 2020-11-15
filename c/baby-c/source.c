#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int foo(int a, int b) {
  while(a != b) {
    if(a > b) {
      a -= b;
    }
    else if(a < b) {
      b -= a;
    }
  }

  return a;
}

int main(int argc, char** argv) {
  if(argc != 3) {
    fprintf(stderr, "USAGE: %s <num1> <num2>\n", argv[0]);
    exit(1);
  }

  int a = atoi(argv[1]);
  int b = atoi(argv[2]);
  printf("foo(%d, %d) = %d\n", a, b, foo(a, b));
  return 0;
}
