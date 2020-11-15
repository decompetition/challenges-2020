#include <stdio.h>
#include <stdlib.h>

int is_prime(int n)
{
    if (n <= 1) return 0;
    if (n == 2 || n == 3) return 1;
    if (n % 2 == 0 || n % 3 == 0) return 0;

    for (int i = 5; i*i < n; i+=6)
        if (n % i == 0 || n % (i+2) == 0)
            return 0;

    return 1;
}

int main(int argc, char** argv){
    if (argc != 2) {
        fprintf(stderr, "USAGE: %s <num>\n", argv[0]);
        exit(1);
    }

    int a = atoi(argv[1]);
    printf("is_prime(%d) = %d\n", a, is_prime(a));
}
